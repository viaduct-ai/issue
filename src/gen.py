import json
from typing import List
import openai
from pydantic import BaseModel
import streamlit

openai.organization = streamlit.secrets.openai_org
openai.api_key = streamlit.secrets.openai_key

def get_chat_completion(question, system_content="", model="gpt-3.5-turbo", examples=[], temperature=.3):
    res = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": system_content},
            *examples,
            {"role": "user", "content": question},
        ],
        temperature=temperature,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return res["choices"][0]["message"]["content"]


class IssueSpec(BaseModel):
    at_risk_population_filter: List[str] = []
    claim_filters: List[str] = []
    signal_event_filters: List[str] = []
    description: str = ""


class Example:
    def __init__(
            self, 
            text: str, 
            issue_spec: IssueSpec = None,
            response: str = None,
    ):
        self.text = text
        
        if issue_spec is None:
            assert response is not None
            self.response = response
            self.issue_spec = IssueSpec(**json.loads(response))
        else:
            self.issue_spec = issue_spec
            self.response = response or json.dumps(issue_spec.dict(), indent=4)

    def get_response(self):
        return self.response

    def get(self):
        return [
            {"role": "user", "content": self.text},
            {"role": "assistant", "content": self.response},
        ]
    

