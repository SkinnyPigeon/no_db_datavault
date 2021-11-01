ustan_keys = ["chi"]
ustan_sats = {
    "ustan.cycles": {
        "sat_time_cycle_details": {
            "columns": ["init_appointment_date", "elapsed_days", "interval_days", "appointment_date"],
            "hub": "hub_time"
        },
        "sat_event_cycle_details": {
            "columns": ["regime_id", "intention_id", "cycle_id", "drug_names", "diagnosis", "intention", "regime", "cycle", "p_ps", "ps", "nausea", "vomiting", "diarrhoea", "constipation", "oralMucositis", "oesophagitis", "neurotoxicity", "handFoot", "skin", "hypersensitivity", "fatigue", "required_doses"],
            "hub": "hub_event"
        },
        "links": ["time_event_link"]
    },
    "ustan.general": {
        "sat_time_general_details": {
            "columns": ["incidence_date", "first_seen_date", "survival_days", "dat_death"],
            "hub": "hub_time"
        },
        "sat_person_general_patient": {
            # "columns": ["name", "date_of_birth", "dob", "age", "gender", "age_at_diagnosis", "weight", "bmi", "height", "religion", "civil_st", "postcode_pre", "postcode_suf", "postcode"],
            "columns": ["name", "date_of_birth", "dob", "age", "gender", "age_at_diagnosis", "weight", "bmi", "height", "religion", "civil_st", "postcode_pre", "postcode_suf", "postcode", "gp_name", "gp_id"],
            "hub": "hub_person"
        },
        # "sat_person_general_gp": {
        #     "columns": ["gp_name", "gp_id"],
        #     "hub": "hub_person"
        # },
        "sat_location_general_details": {
            "columns": ["ref_hospital"],
            "hub": "hub_location"
        },
        "sat_event_general_details": {
            "columns": ["site_icd_10", "site", "histology", "primary", "metastasis1", "metastasis2", "metastasis3", "smid", "smid1", "cong_heart_fail_flag", "con_tiss_disease_rheum_flag", "dementia_flag", "pulmonary_flag", "con_tiss_flag", "diabetes_flag", "para_hemiplegia_flag", "renal_flag", "liver_flag", "aids_hiv_flag", "cancer_flag", "charlson_score", "simd", "simd1", "side", "stage", "stage_detail", "tnm_t", "tnm_t_detail", "tnm_n", "tnm_n_detail", "tnm_m", "perf_stat", "smr01_flag", "death_flag"],
            "hub": "hub_event"
        },
        "links": ["time_person_link", "time_location_link", "time_event_link", "person_location_link", "person_event_link", "location_event_link"]
    },
    "ustan.intentions": {
        "sat_time_intentions_details": {
            "columns": ["init_appointment_date", "elapsed_days", "appointment_date"],
            "hub": "hub_time"
        },
        "sat_person_intentions_details": {
            "columns": ["patient_id"],
            "hub": "hub_person"
        },
        "sat_event_intentions_details": {
            "columns": ["intention_id", "intention_seq", "first_intention", "regime_ratio", "cycle_ratio", "intention", "first_regime"],
            "hub": "hub_event"
        },
        "links": ["time_person_link", "time_event_link", "person_event_link"]
    },
    "ustan.patients": {
        "sat_time_patients_details": {
            "columns": ["appointment_date"],
            "hub": "hub_time"
        },
        "sat_person_patients_details": {
            "columns": ["patient_id"],
            "hub": "hub_person"
        },
        "sat_event_patients_details": {
            "columns": ["first_intention"],
            "hub": "hub_event"
        },
        "links": ["time_person_link", "time_event_link", "person_event_link"]
    },
    "ustan.regimes": {
        "sat_time_regimes_details": {
            "columns": ["init_appointment_date", "appointment_date", "interval_days", "elapsed_days"],
            "hub": "hub_time"
        },
        "sat_event_regimes_details": {
            "columns": ["intention_id", "regime_id", "regime_seq", "regime_ratio", "cycle_ratio", "intention", "prev_regime", "first_regime", "regime"],
            "hub": "hub_event"
        },
        "links": ["time_event_link"]
    },
    "ustan.smr01": {
        "sat_time_smr01_details": {
            "columns": ["incidence_date", "admission_date", "length_of_stay", "discharge_date"],
            "hub": "hub_time"
        },
        "sat_person_smr01_details": {
            "columns": ["marital_status", "ethnic_group"],
            "hub": "hub_person"
        },
        "sat_event_smr01_details": {
            "columns": ["other_condition1", "other_condition2", "other_condition3", "main_operation_b", "waiting_list_type", "main_condition", "main_operation_a"],
            "hub": "hub_event"
        },
        "links": ["time_person_link", "time_event_link", "person_event_link"]
    },
    "ustan.smr06": {
        "sat_time_smr06_details": {
            "columns": ["incidence_date"],
            "hub": "hub_time"
        },
        "sat_event_smr06_details": {
            "columns": ["er_status", "her2_status", "stage_clinical_t", "stage_clinical_n", "stage_clinical_m", "num_positive", "pathological_tum_size"],
            "hub": "hub_event"
        },
        "links": ["time_event_link"]
    }
}