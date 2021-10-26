zmc_keys = ["patnr"]
zmc_sats = {
    "zmc.wearable": {
        "sat_time_wearable_details": {
            "columns": ["date"],
            "hub": "hub_time"
        },
        "sat_event_wearable_details": {
            "columns": ["w_time", "w_steps", "w_cad", "sst", "sst_time", "cyc_time", "cyc_steps", "cyc_cad"],
            "hub": "hub_event"
        },
        "links": ["time_event_link"]
    },
    "zmc.complaints_and_diagnosis": {
        "sat_time_complaints_and_diagnosis": {
            "columns": ["begin_date", "end_date"],
            "hub": "hub_time"
        },
        "sat_event_complaints_and_diagnosis": {
            "columns": ["complaints_and_diagnosis", "status", "specialism", "type", "name_of_diagnosis_or_complaint", "anatomical_location", "laterality"],
            "hub": "hub_event"
        },
        "links": ["time_event_link"]
    },
    "zmc.medication_agreements": {
        "sat_person_medication_agreements": {
            "columns": ["prescribed_by"],
            "hub": "hub_person"
        },
        "sat_object_medication_agreements": {
            "columns": ["medicines", "description"],
            "hub": "hub_object"
        },
        "links": ["person_object_link"]
    },
    "zmc.medication_use": {
        "sat_object_medication_use": {
            "columns": ["product", "use", "reason"],
            "hub": "hub_object"
        },
        "links": []
    },
    "zmc.medical_aids_and_tools": {
        "sat_object_medical_aids_and_tools": {
            "columns": ["product_description", "anatomical_location", "description"],
            "hub": "hub_object"
        },
        "links": []
    },
    "zmc.bloodpressure": {
        "sat_time_bloodpressure_details": {
            "columns": ["date"],
            "hub": "hub_time"
        },
        "sat_location_bloodpressure_details": {
            "columns": ["position"],
            "hub": "hub_location"
        },
        "sat_event_bloodpressure_details": {
            "columns": ["value", "description", "systolic_bloodpressure", "diastolic_bloodpressure", "measurement_method", "manchette_type", "measurement_location", "description"],
            "hub": "hub_event"
        },
        "links": ["time_location_link", "time_event_link", "location_event_link"]
    },
    "zmc.weight": {
        "sat_time_weight_details": {
            "columns": ["date"],
            "hub": "hub_time"
        },
        "sat_event_weight_details": {
            "columns": ["measurement", "clothes", "description"],
            "hub": "hub_event"
        },
        "links": ["time_event_link"]
    },
    "zmc.length": {
        "sat_time_length_details": {
            "columns": ["date"],
            "hub": "hub_time"
        },
        "sat_event_length_details": {
            "columns": ["measurement", "description"],
            "hub": "hub_event"
        },
        "links": ["time_event_link"]
    },
    "zmc.registered_events": {
        "sat_time_registered_events": {
            "columns": ["start_date", "end_date", "date"],
            "hub": "hub_time"
        },
        "sat_location_registered_events": {
            "columns": ["location"],
            "hub": "hub_location"
        },
        "sat_event_registered_events": {
            "columns": ["type", "method", "anatomical_location", "laterality", "indication", "executor", "requested_by", "description"],
            "hub": "hub_event"
        },
        "links": ["time_location_link", "time_event_link", "location_event_link"]
    },
    "zmc.warning": {
        "sat_time_warning_details": {
            "columns": ["begindate"],
            "hub": "hub_time"
        },
        "sat_event_warning_details": {
            "columns": ["alerts", "type"],
            "hub": "hub_event"
        },
        "links": ["time_event_link"]
    },
    "zmc.functional_or_mental_state": {
        "sat_time_functional_or_mental_state": {
            "columns": ["date"],
            "hub": "hub_time"
        },
        "sat_event_functional_or_mental_state": {
            "columns": ["name", "value"],
            "hub": "hub_event"
        },
        "links": ["time_event_link"]
    },
    "zmc.living_situation": {
        "sat_person_living_situation": {
            "columns": ["house_type", "description"],
            "hub": "hub_person"
        },
        "links": []
    },
    "zmc.drug_use": {
        "sat_person_drug_use": {
            "columns": ["substance", "quantity", "description"],
            "hub": "hub_person"
        },
        "links": []
    },
    "zmc.alcohol_use": {
        "sat_person_alcohol_use": {
            "columns": ["usage_status", "quantity", "description"],
            "hub": "hub_person"
        },
        "links": []
    },
    "zmc.tobacco_use": {
        "sat_person_tobacco_use": {
            "columns": ["substance", "quantity", "description"],
            "hub": "hub_person"
        },
        "links": []
    },
    "zmc.allergies": {
        "sat_person_allergies_details": {
            "columns": ["caustive_substance", "critical", "description"],
            "hub": "hub_person"
        },
        "links": []
    },
    "zmc.documents": {
        "sat_time_documents_details": {
            "columns": ["date"],
            "hub": "hub_time"
        },
        "sat_object_documents_details": {
            "columns": ["document_title", "type", "document"],
            "hub": "hub_object"
        },
        "links": ["time_object_link"]
    },
    "zmc.images": {
        "sat_time_images_details": {
            "columns": ["date"],
            "hub": "hub_time"
        },
        "sat_object_images_details": {
            "columns": ["image_title", "type", "image"],
            "hub": "hub_object"
        },
        "links": ["time_object_link"]
    },
    "zmc.patient_details": {
        "sat_person_patient_details": {
            "columns": ["nname", "nnams", "vname", "titel", "gschl", "gbdat", "natio"],
            "hub": "hub_person"
        },
        "links": []
    }
}