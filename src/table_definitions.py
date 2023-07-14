TABLES = """
CREATE TABLE v1__vehicle  # All vehicles and their attributes
(
    `vin` String,
    `fleet` String,
    `external_id` String,
    `sale_dealer_name` String,
    `sale_dealer_code` String,
    `repair_dealer_code` String,
    `sale_intended_service` String,
    `vehicle_make` String,  # can be Buick, Chevrolet, GMC
    `vehicle_model` String,  # can be Colorado, Traverse C1, Enclave C1, Blazer, Acadia C1, Canyon
    `vehicle_model_year` Int,  # can be 2021, 2022
    `vehicle_gvwr` String,  # can be "2,800 KG/6173 LBS", "6,001 LBS", "5,500 LBS", "6,000 LBS", "5,800 LBS", "5,400 LBS", "5,700 LBS", "5,600 LBS", "5,900 LBS", "6,200 LBS", "6,100 LBS"
    `vehicle_manufactured_at` Date,
    `engine_model` String,  # can be LGZ, LCV, LWN, LFY, LSY, LGX
    `engine_model_year` Int32,
    `engine_horsepower` Int32,
    `engine_on_time_total` Float64,
    `idle_rate` Float64,
    `fuel_consumption` Float64,
    `fuel_consumption_unit` String,
    `engine_manufactured_at` Date,
    `mileage` Float64,
    `mileage_unit` String,
    `vehicle_started_driving_at` Date,
    `vehicle_category_id` String,
    `transport_category_id` String,
    `engine_certification` String,
    `manufacture_plant_name` String,  # can be "Lansing Delta", "Ramos Arizpe", "Wentzville", "Spring Hill - Truck"
    `drivetrain` String,  # can be "AWD", "FWD", "FWD/AWD", "4WD", "2WD"
    `trim_level` String,
    `luxury_edition` Bool,
    `atcu_part_num` String,
    `frrad_part_num` String,
    `evtc_part_num` String,
    `scu_part_num` String,
    `cdm_part_num` String,
    `hfm_part_num` String,
    `eps_part_num` String,
    `usm_part_num` String,
    `srrr_part_num` String,
    `acu_part_num` String,
    `srrl_part_num` String,
    `sonar_part_num` String,
    `ecm_part_num` String,
    `gwd4_part_num` String,
    `bcm_part_num` String,
    `frcam_part_num` String,
    `meter_part_num` String,
    `adas_part_num` String,
    `abs_part_num` String,
    `nav_part_num` String,
    `hvac_part_num` String,
    `hvac_version` String,
    `infotainment_version` String,
    `platform` String,  # can be "Crossover SUV", "Global Midsize Trucks"
    `body` String,  # can be "Crew Cab", "Extended Cab", "4 Door Utility"
    `country` String,
    `purpose` String,
    `infotainment_code` String,
    `infotainment_desc` String,
    `transmission_supplier_code` String,
    `transmission_number` String,
    `transmission_model` String,
    `engine_supplier_code` String,
    `engine_number` String,
    `vppc_code` String
)

CREATE TABLE v1__claim  # All claim incidents and their attributes
(
    `id` String,
    `vin` String,
    `date` Date,
    `mileage` Float64,  # Mileage at the time of the claim
    `mileage_unit` String,
    `cost_labor` Float64  # Cost of labor for the claim,
    `cost_parts` Float64  # Cost of parts for the claim,
    `cost_total` Float64  # Total cost of the claim,
    `currency_code` String,
    `repair_order_number` String,
    `failed_part_number` String,
    `labor_code` String,
    `parts` Array(String),
    `status` String,
    `external_id` String,
    `external_url` String,
    `dealer_id` String,
    `campaign_ids` Array(String),
    `incident_category` String,
    `incident_condition` String,
    `incident_failure_mode` String,
    `incident_location` String,
    `incident_supplier` String,
    `customer_service_complaint` String,
    `bom` String,
    `bom_description` String,
    `causal_description` String,
    `labor_operation_detail` String,
    `probable_cause` String,
    `incident_related_issue_description` String,
    `notes` String,  # general notes
    `notes_causal` String,  # notes about the cause of the claim
    `notes_causal_part` String,  # notes about the part that caused the claim
    `notes_correction` String,  # notes about the action taken to correct the claim
    `notes_customer` String,  # notes from the customer
    `claim_group` String,  # claim group category. Can be referred to as SMT or SMT code as well
    `claim_subgroup` String,  # claim subgroup category. Can be referred to as QRD or QRD code as well
    `transaction_category` String,
    `months_in_service` Int32
)

CREATE TABLE v1__signal_event_occurrence
(
    `tenant` String,
    `signal_event_type` String,
    `signal_event_id` String,
    `vin` String,
    `recorded_at` DateTime64(3),
    `spn` Float64,
    `fmi` Float64,
    `obd2_code` String,
    `ext_code` String,
    `occurrence_count` Int32,
    `mil_lamp_status` String,
    `red_lamp_status` String,
    `amber_lamp_status` String,
    `protect_lamp_status` String,
    `ecu_family` String,
    `ecu_version` String,
    `symptom` String,
    `status` String,
    `current_fault` String,
    `description` String
)
""".strip()
