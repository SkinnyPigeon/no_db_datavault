zmc_wearable_1 = {'tag': 'wearable', 'source': 'zmc.wearable', 'fields': ['patnr', 'date', 'w_time', 'w_steps', 'w_cad', 'sst', 'sst_time', 'cyc_time', 'cyc_steps', 'cyc_cad'], 'key_lookup': {}, 'table': True, 'graph': True, 'image': False}
zmc_wearable_2 = {'tag': 'wearable', 'source': 'zmc.medical_aids_and_tools', 'fields': ['patnr', 'product_description'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_wearable_3 = {'tag': 'wearable', 'source': 'zmc.patient_details', 'fields': ['patnr' ,'nname' ,'nnams' ,'vname' ,'titel' ,'gschl' ,'gbdat' ,'natio'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

zmc_diagnostic_1 = {'tag': 'diagnostic', 'source': 'zmc.complaints_and_diagnosis', 'fields': ['patnr', 'complaints_and_diagnosis', 'status', 'specialism', 'type', 'name_of_diagnosis_or_complaint', 'anatomical_location', 'laterality', 'begin_date', 'end_date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_diagnostic_2 = {'tag': 'diagnostic', 'source': 'zmc.bloodpressure', 'fields': ['patnr', 'value', 'position', 'description', 'date', 'systolic_bloodpressure', 'diastolic_bloodpressure', 'measurement_method', 'manchette_type', 'measurement_location', 'description'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_diagnostic_3 = {'tag': 'diagnostic', 'source': 'zmc.weight', 'fields': ['patnr', 'measurement', 'clothes', 'description', 'date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_diagnostic_4 = {'tag': 'diagnostic', 'source': 'zmc.length', 'fields': ['patnr', 'measurement', 'description', 'date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_diagnostic_5 = {'tag': 'diagnostic', 'source': 'zmc.registered_events', 'fields': ['patnr', 'type', 'method', 'anatomical_location', 'laterality', 'start_date', 'end_date', 'indication', 'requested_by', 'date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}        
zmc_diagnostic_6 = {'tag': 'diagnostic', 'source': 'zmc.functional_or_mental_state', 'fields': ['patnr', 'name', 'value', 'date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_diagnostic_7 = {'tag': 'diagnostic', 'source': 'zmc.patient_details', 'fields': ['patnr' ,'nname' ,'nnams' ,'vname' ,'titel' ,'gschl' ,'gbdat' ,'natio'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

zmc_medication_1 = {'tag': 'medication', 'source': 'zmc.complaints_and_diagnosis', 'fields': ['patnr', 'complaints_and_diagnosis', 'status', 'specialism', 'type', 'name_of_diagnosis_or_complaint', 'begin_date', 'end_date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_medication_2 = {'tag': 'medication', 'source': 'zmc.medication_agreements', 'fields': ['patnr', 'medicines', 'prescribed_by', 'description'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_medication_3 = {'tag': 'medication', 'source': 'zmc.medication_use', 'fields': ['patnr', 'product', 'use', 'reason'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_medication_4 = {'tag': 'medication', 'source': 'zmc.medical_aids_and_tools', 'fields': ['patnr', 'product_description', 'anatomical_location', 'description'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_medication_5 = {'tag': 'medication', 'source': 'zmc.functional_or_mental_state', 'fields': ['patnr', 'name', 'value', 'date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_medication_6 = {'tag': 'medication', 'source': 'zmc.allergies', 'fields': ['patnr', 'caustive_substance', 'critical', 'description'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_medication_7 = {'tag': 'medication', 'source': 'zmc.patient_details', 'fields': ['patnr' ,'nname' ,'nnams' ,'vname' ,'titel' ,'gschl' ,'gbdat' ,'natio'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

zmc_operations_1 = {'tag': 'operations', 'source': 'zmc.complaints_and_diagnosis', 'fields': ['patnr', 'complaints_and_diagnosis', 'status', 'specialism', 'type', 'name_of_diagnosis_or_complaint', 'anatomical_location', 'laterality', 'begin_date', 'end_date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_operations_2 = {'tag': 'operations', 'source': 'zmc.medical_aids_and_tools', 'fields': ['patnr', 'product_description', 'anatomical_location'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_operations_3 = {'tag': 'operations', 'source': 'zmc.registered_events', 'fields': ['patnr', 'type'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_operations_4 = {'tag': 'operations', 'source': 'zmc.warning', 'fields': ['patnr', 'alerts', 'begindate', 'type'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_operations_5 = {'tag': 'operations', 'source': 'zmc.patient_details', 'fields': ['patnr' ,'nname' ,'nnams' ,'vname' ,'titel' ,'gschl' ,'gbdat' ,'natio'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

zmc_documents_1 = {'tag': 'documents', 'source': 'zmc.complaints_and_diagnosis', 'fields': ['patnr', 'complaints_and_diagnosis', 'status', 'specialism', 'type', 'name_of_diagnosis_or_complaint', 'anatomical_location', 'laterality', 'begin_date', 'end_date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_documents_2 = {'tag': 'documents', 'source': 'zmc.medical_aids_and_tools', 'fields': ['patnr', 'product_description', 'anatomical_location', 'description'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_documents_3 = {'tag': 'documents', 'source': 'zmc.registered_events', 'fields': ['patnr', 'type', 'method', 'anatomical_location', 'laterality', 'start_date', 'end_date', 'indication', 'executor', 'requested_by', 'location', 'description', 'date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_documents_4 = {'tag': 'documents', 'source': 'zmc.warning', 'fields': ['patnr', 'alerts', 'begindate', 'type'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_documents_5 = {'tag': 'documents', 'source': 'zmc.documents', 'fields': ['patnr', 'document_title', 'type', 'date', 'document'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': True}
zmc_documents_6 = {'tag': 'documents', 'source': 'zmc.images', 'fields': ['patnr', 'image_title', 'type', 'date', 'image'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': True}
zmc_documents_7 = {'tag': 'documents', 'source': 'zmc.patient_details', 'fields': ['patnr' ,'nname' ,'nnams' ,'vname' ,'titel' ,'gschl' ,'gbdat' ,'natio'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

zmc_treatments_1 = {'tag': 'treatments', 'source': 'zmc.complaints_and_diagnosis', 'fields': ['patnr', 'complaints_and_diagnosis', 'status', 'specialism', 'type', 'name_of_diagnosis_or_complaint', 'anatomical_location', 'laterality', 'begin_date', 'end_date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_treatments_2 = {'tag': 'treatments', 'source': 'zmc.medication_agreements', 'fields': ['patnr', 'medicines', 'prescribed_by'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_treatments_3 = {'tag': 'treatments', 'source': 'zmc.medical_aids_and_tools', 'fields': ['patnr', 'product_description', 'anatomical_location', 'description'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_treatments_4 = {'tag': 'treatments', 'source': 'zmc.warning', 'fields': ['patnr', 'alerts', 'begindate', 'type'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_treatments_5 = {'tag': 'treatments', 'source': 'zmc.functional_or_mental_state', 'fields': ['patnr', 'name', 'value', 'date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_treatments_6 = {'tag': 'treatments', 'source': 'zmc.living_situation', 'fields': ['patnr', 'house_type', 'description'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_treatments_7 = {'tag': 'treatments', 'source': 'zmc.drug_use', 'fields': ['patnr', 'substance', 'quantity'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_treatments_8 = {'tag': 'treatments', 'source': 'zmc.alcohol_use', 'fields': ['patnr', 'usage_status', 'quantity'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_treatments_9 = {'tag': 'treatments', 'source': 'zmc.tobacco_use', 'fields': ['patnr', 'substance', 'quantity'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_treatments_10 = {'tag': 'treatments', 'source': 'zmc.allergies', 'fields': ['patnr', 'caustive_substance', 'critical', 'description'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_treatments_11 = {'tag': 'treatments', 'source': 'zmc.patient_details', 'fields': ['patnr' ,'nname' ,'nnams' ,'vname' ,'titel' ,'gschl' ,'gbdat' ,'natio'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

zmc_healthcare_providers_1 = {'tag': 'healthcare_providers', 'source': 'zmc.medication_agreements', 'fields': ['patnr', 'prescribed_by'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_healthcare_providers_2 = {'tag': 'healthcare_providers', 'source': 'zmc.registered_events', 'fields': ['patnr', 'executor'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_healthcare_providers_3 = {'tag': 'healthcare_providers', 'source': 'zmc.patient_details', 'fields': ['patnr' ,'nname' ,'nnams' ,'vname' ,'titel' ,'gschl' ,'gbdat' ,'natio'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

zmc_allergies_1 = {'tag': 'allergies', 'source': 'zmc.medication_agreements', 'fields': ['patnr', 'medicines'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_allergies_2 = {'tag': 'allergies', 'source': 'zmc.allergies', 'fields': ['patnr', 'caustive_substance', 'critical', 'description'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_allergies_3 = {'tag': 'allergies', 'source': 'zmc.patient_details', 'fields': ['patnr' ,'nname' ,'nnams' ,'vname' ,'titel' ,'gschl' ,'gbdat' ,'natio'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

zmc_personal_1 = {'tag': 'personal', 'source': 'zmc.weight', 'fields': ['patnr', 'measurement', 'clothes', 'description', 'date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_personal_2 = {'tag': 'personal', 'source': 'zmc.length', 'fields': ['patnr', 'measurement', 'description', 'date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_personal_3 = {'tag': 'personal', 'source': 'zmc.functional_or_mental_state', 'fields': ['patnr', 'name', 'value', 'date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_personal_4 = {'tag': 'personal', 'source': 'zmc.living_situation', 'fields': ['patnr', 'house_type', 'description'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_personal_5 = {'tag': 'personal', 'source': 'zmc.drug_use', 'fields': ['patnr', 'substance', 'quantity', 'description'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_personal_6 = {'tag': 'personal', 'source': 'zmc.alcohol_use', 'fields': ['patnr', 'usage_status', 'quantity', 'description'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_personal_7 = {'tag': 'personal', 'source': 'zmc.tobacco_use', 'fields': ['patnr', 'substance', 'quantity', 'description'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_personal_8 = {'tag': 'personal', 'source': 'zmc.allergies', 'fields': ['patnr', 'caustive_substance', 'critical', 'description'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_personal_9 = {'tag': 'personal', 'source': 'zmc.patient_details', 'fields': ['patnr' ,'nname' ,'nnams' ,'vname' ,'titel' ,'gschl' ,'gbdat' ,'natio'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

zmc_patient_appointments_1 = {'tag': 'patient_appointments', 'source': 'zmc.registered_events', 'fields': ['patnr', 'type', 'executor', 'location', 'date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_patient_appointments_2 = {'tag': 'patient_appointments', 'source': 'zmc.patient_details', 'fields': ['patnr' ,'nname' ,'nnams' ,'vname' ,'titel' ,'gschl' ,'gbdat' ,'natio'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

zmc_drugs_and_alcohol_1 = {'tag': 'drugs_and_alcohol', 'source': 'zmc.drug_use', 'fields': ['patnr', 'substance', 'quantity', 'description'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_drugs_and_alcohol_2 = {'tag': 'drugs_and_alcohol', 'source': 'zmc.alcohol_use', 'fields': ['patnr', 'usage_status', 'quantity', 'description'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_drugs_and_alcohol_3 = {'tag': 'drugs_and_alcohol', 'source': 'zmc.tobacco_use', 'fields': ['patnr', 'substance', 'quantity', 'description'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_drugs_and_alcohol_4 = {'tag': 'drugs_and_alcohol', 'source': 'zmc.patient_details', 'fields': ['patnr' ,'nname' ,'nnams' ,'vname' ,'titel' ,'gschl' ,'gbdat' ,'natio'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

zmc_all_1 = {'tag': 'all', 'source': 'zmc.wearable', 'fields': ['patnr', 'date', 'w_time', 'w_steps', 'w_cad', 'sst', 'sst_time', 'cyc_time', 'cyc_steps', 'cyc_cad'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_all_2 = {'tag': 'all', 'source': 'zmc.complaints_and_diagnosis', 'fields': ['patnr', 'complaints_and_diagnosis', 'status', 'specialism', 'type', 'name_of_diagnosis_or_complaint', 'anatomical_location', 'laterality', 'begin_date', 'end_date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_all_3 = {'tag': 'all', 'source': 'zmc.medication_agreements', 'fields': ['patnr', 'medicines', 'prescribed_by', 'description'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_all_4 = {'tag': 'all', 'source': 'zmc.medication_use', 'fields': ['patnr', 'product', 'use', 'reason'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_all_5 = {'tag': 'all', 'source': 'zmc.medical_aids_and_tools', 'fields': ['patnr', 'product_description', 'anatomical_location', 'description'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_all_6 = {'tag': 'all', 'source': 'zmc.bloodpressure', 'fields': ['patnr', 'value', 'position', 'description', 'date', 'systolic_bloodpressure', 'diastolic_bloodpressure', 'measurement_method', 'manchette_type', 'measurement_location', 'description'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_all_7 = {'tag': 'all', 'source': 'zmc.weight', 'fields': ['patnr', 'measurement', 'clothes', 'description', 'date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_all_8 = {'tag': 'all', 'source': 'zmc.length', 'fields': ['patnr', 'measurement', 'description', 'date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_all_9 = {'tag': 'all', 'source': 'zmc.registered_events', 'fields': ['patnr', 'type', 'method', 'anatomical_location', 'laterality', 'start_date', 'end_date', 'indication', 'executor', 'requested_by', 'location', 'description', 'date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_all_10 = {'tag': 'all', 'source': 'zmc.warning', 'fields': ['patnr', 'alerts', 'begindate', 'type'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_all_11 = {'tag': 'all', 'source': 'zmc.functional_or_mental_state', 'fields': ['patnr', 'name', 'value', 'date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_all_12 = {'tag': 'all', 'source': 'zmc.living_situation', 'fields': ['patnr', 'house_type', 'description'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_all_13 = {'tag': 'all', 'source': 'zmc.drug_use', 'fields': ['patnr', 'substance', 'quantity', 'description'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_all_14 = {'tag': 'all', 'source': 'zmc.alcohol_use', 'fields': ['patnr', 'usage_status', 'quantity', 'description'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_all_15 = {'tag': 'all', 'source': 'zmc.tobacco_use', 'fields': ['patnr', 'substance', 'quantity', 'description'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_all_16 = {'tag': 'all', 'source': 'zmc.allergies', 'fields': ['patnr', 'caustive_substance', 'critical', 'description'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_all_17 = {'tag': 'all', 'source': 'zmc.documents', 'fields': ['patnr', 'document_title', 'type', 'date', 'document'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': True}
zmc_all_18 = {'tag': 'all', 'source': 'zmc.images', 'fields': ['patnr', 'image_title', 'type', 'date', 'image'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': True}
zmc_all_19 = {'tag': 'all', 'source': 'zmc.patient_details', 'fields': ['patnr' ,'nname' ,'nnams' ,'vname' ,'titel' ,'gschl' ,'gbdat' ,'natio'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

zmc_tags = [
    zmc_wearable_1,
    zmc_wearable_2,
    zmc_wearable_3,
    zmc_diagnostic_1,
    zmc_diagnostic_2,
    zmc_diagnostic_3,
    zmc_diagnostic_4,
    zmc_diagnostic_5,
    zmc_diagnostic_6,
    zmc_diagnostic_7,
    zmc_medication_1,
    zmc_medication_2,
    zmc_medication_3,
    zmc_medication_4,
    zmc_medication_5,
    zmc_medication_6,
    zmc_medication_7,
    zmc_operations_1,
    zmc_operations_2,
    zmc_operations_3,
    zmc_operations_4,
    zmc_operations_5,
    zmc_documents_1,
    zmc_documents_2,
    zmc_documents_3,
    zmc_documents_4,
    zmc_documents_5,
    zmc_documents_6,
    zmc_documents_7,
    zmc_treatments_1,
    zmc_treatments_2,
    zmc_treatments_3,
    zmc_treatments_4,
    zmc_treatments_5,
    zmc_treatments_6,
    zmc_treatments_7,
    zmc_treatments_8,
    zmc_treatments_9,
    zmc_treatments_10,
    zmc_treatments_11,
    zmc_healthcare_providers_1,
    zmc_healthcare_providers_2,
    zmc_healthcare_providers_3,
    zmc_allergies_1,
    zmc_allergies_2,
    zmc_allergies_3,
    zmc_personal_1,
    zmc_personal_2,
    zmc_personal_3,
    zmc_personal_4,
    zmc_personal_5,
    zmc_personal_6,
    zmc_personal_7,
    zmc_personal_8,
    zmc_personal_9,
    zmc_patient_appointments_1,
    zmc_patient_appointments_2,
    zmc_drugs_and_alcohol_1,
    zmc_drugs_and_alcohol_2,
    zmc_drugs_and_alcohol_3,
    zmc_drugs_and_alcohol_4,
    zmc_all_1,
    zmc_all_2,
    zmc_all_3,
    zmc_all_4,
    zmc_all_5,
    zmc_all_6,
    zmc_all_7,
    zmc_all_8,
    zmc_all_9,
    zmc_all_10,
    zmc_all_11,
    zmc_all_12,
    zmc_all_13,
    zmc_all_14,
    zmc_all_15,
    zmc_all_16,
    zmc_all_17,
    zmc_all_18,
    zmc_all_19
]
