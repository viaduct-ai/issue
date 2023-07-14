import json
import streamlit as st

import gen
from table_definitions import TABLES


system_content = f"""
You have access to the following ClickHouse SQL tables `v1__vehicle`, `v1__claim`, `v1__signal_event_occurrence` with the following definitions:
[TABLES]
{TABLES}
[END TABLES]
Your task is to generates the specs for a new issue based on the user's input. An issue's definition consists of `AT_RISK_VEHICLE_POPULATION`, `CLAIMS", `SIGNAL_EVENTS`, a `DESCRIPTION`.
- `AT_RISK_VEHICLE_POPULATION` is defined by a set of SQL filter expressions on vehicle attributes in the `v1__vehicle` table.
- `CLAIMS` is defined by a set of SQL filter expressions on claim attributes in the `v1__claim` table.
- `SIGNAL_EVENTS` is defined either by a set of `signal_event_id`s or by a set of SQL filter expressions on signal event attributes in the `v1__signal_event_occurrence` table.
- `DESCRIPTION` is a natural language description of the issue as a markdown string highlighting important keywords as bold..

Given the user's input, generate the issue specs as a json string. Make sure to map the user's input to the correct table and column names. Ones you generate the results, double check you work to make sure columns referenced in the issue spec are present in the corresponding table and fix the results if neccessary.
""".strip()

print(system_content)

examples = gen.Example(
    "Colorado with LWN engine and 4025070 labor code and ac in causal parts",
    response="""
    {
        "at_risk_population_filter": [
            "vehicle_make = 'Chevrolet'",
            "vehicle_model = 'Colorado'",
            "engine_model = 'LWN'"
        ],
        "claim_filters": [
            "labor_code = '4025070'",
            "notes_causal_part LIKE '%ac%'"
        ],
        "signal_event_filters": [],
        "description": "**Chevy Colorado** vehicles with **LWN** engine model that filled claims with **4025070** labor code."
    }
    """,
).get()

print(examples)

@st.cache_data
def get_res(issue_def):
    res = gen.get_chat_completion(
        issue_def,
        system_content=system_content,
        examples=examples,
    )

    return res


def main():
    st.title("Issues")

    # get question
    issue_def = st.text_input("Create an issue", value="", placeholder="Colorado vins with LWN engine and claims with 4025070 labor code...")

    if issue_def != "":
        
        res = get_res(issue_def)
        print(f"Results:\n{res}")

        # extract ``` from res
        res_stripped = res.strip("```")
        issue_spec = gen.IssueSpec(**json.loads(res_stripped))

        st.header("Description")
        st.write(issue_spec.description)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("At-risk vehicle population")
            # create a markdown item for each filter
            for filter in issue_spec.at_risk_population_filter:
                st.markdown(f"- `{filter}`")

        with col2:
            st.subheader("Related Claims")
            for filter in issue_spec.claim_filters:
                st.markdown(f"- `{filter}`")

        with col3:
            st.subheader("Relevant Signal Events")
            for filter in issue_spec.signal_event_filters:
                st.markdown(f"- `{filter}`")


        expander = st.expander("Show JSON")
        expander.code(res_stripped, language="json")
    

if __name__ == "__main__":
    main()
        