ustan_chemotherapy = {'tag': 'chemotherapy', 'source': 'ustan.cycles', 'fields': ['chi', 'regime_id', 'intention_id', 'cycle_id', 'drug_names', 'diagnosis', 'init_appointment_date', 'elapsed_days', 'interval_days', 'appointment_date', 'intention', 'regime', 'cycle', 'p_ps', 'ps', 'nausea', 'vomiting', 'diarrhoea', 'constipation', 'oralMucositis', 'oesophagitis', 'neurotoxicity', 'handFoot', 'skin', 'hypersensitivity', 'fatigue', 'required_doses'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

ustan_medication_1 = {'tag': 'medication', 'source': 'ustan.cycles', 'fields': ['chi', 'drug_names', 'diagnosis', 'appointment_date', 'intention', 'regime', 'cycle', 'required_doses'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
ustan_medication_2 = {'tag': 'medication', 'source': 'ustan.intentions', 'fields': ['chi', 'intention_seq', 'first_intention', 'intention', 'first_regime', 'init_appointment_date', 'appointment_date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
ustan_medication_3 = {'tag': 'medication', 'source': 'ustan.regimes', 'fields': ['chi', 'regime_seq', 'intention', 'first_regime', 'regime', 'init_appointment_date', 'appointment_date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

ustan_patient_appointments_1 = {'tag': 'patient_appointments', 'source': 'ustan.cycles', 'fields': ['chi', 'regime_id', 'intention_id', 'cycle_id', 'drug_names', 'diagnosis', 'init_appointment_date', 'appointment_date', 'intention', 'regime', 'cycle', 'required_doses'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
ustan_patient_appointments_2 = {'tag': 'patient_appointments', 'source': 'ustan.intentions', 'fields': ['chi', 'intention_id', 'intention_seq', 'intention', 'appointment_date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
ustan_patient_appointments_3 = {'tag': 'patient_appointments', 'source': 'ustan.regimes', 'fields': ['chi', 'intention_id', 'regime_id', 'regime_seq', 'intention', 'first_regime', 'regime', 'init_appointment_date', 'appointment_date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

ustan_predictor_1 = {'tag': 'predictor', 'source': 'ustan.cycles', 'fields': ['chi', 'regime_id', 'intention_id', 'cycle_id', 'drug_names', 'diagnosis', 'init_appointment_date', 'elapsed_days', 'interval_days', 'appointment_date', 'intention', 'regime', 'cycle', 'p_ps', 'ps', 'required_doses'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
ustan_predictor_2 = {'tag': 'predictor', 'source': 'ustan.general', 'fields': ['chi', 'incidence_date', 'site_icd_10', 'name', 'date_of_birth', 'first_seen_date', 'site', 'histology', 'primary', 'metastasis1', 'metastasis2', 'metastasis3', 'smid', 'smid1', 'cong_heart_fail_flag', 'con_tiss_disease_rheum_flag', 'dementia_flag', 'pulmonary_flag', 'con_tiss_flag', 'diabetes_flag', 'para_hemiplegia_flag', 'renal_flag', 'liver_flag', 'aids_hiv_flag', 'cancer_flag', 'charlson_score', 'dob', 'age', 'simd', 'simd1', 'side', 'gender', 'age_at_diagnosis', 'weight', 'bmi', 'height', 'religion', 'civil_st', 'ref_hospital', 'postcode_pre', 'postcode_suf', 'stage', 'stage_detail', 'tnm_t', 'tnm_t_detail', 'tnm_n', 'tnm_n_detail', 'tnm_m', 'perf_stat', 'smr01_flag', 'postcode', 'gp_name', 'death_flag', 'survival_days', 'dat_death', 'gp_id'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

ustan_treatment_outcome = {'tag': 'treatment_outcome', 'source': 'ustan.cycles', 'fields': ['chi', 'regime_id', 'intention_id', 'cycle_id', 'drug_names', 'diagnosis', 'appointment_date', 'intention', 'regime', 'cycle', 'ps', 'nausea', 'vomiting', 'diarrhoea', 'constipation', 'oralMucositis', 'oesophagitis', 'neurotoxicity', 'handFoot', 'skin', 'hypersensitivity', 'fatigue'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

ustan_diagnostic = {'tag': 'diagnostic', 'source': 'ustan.general', 'fields': ['chi', 'incidence_date', 'site_icd_10', 'name', 'first_seen_date', 'site', 'histology', 'primary', 'metastasis1', 'metastasis2', 'metastasis3', 'cong_heart_fail_flag', 'con_tiss_disease_rheum_flag', 'dementia_flag', 'pulmonary_flag', 'con_tiss_flag', 'diabetes_flag', 'para_hemiplegia_flag', 'renal_flag', 'liver_flag', 'aids_hiv_flag', 'cancer_flag', 'charlson_score', 'age', 'side', 'gender', 'age_at_diagnosis', 'weight', 'bmi', 'height', 'ref_hospital', 'stage', 'stage_detail', 'tnm_t', 'tnm_t_detail', 'tnm_n', 'tnm_n_detail', 'tnm_m', 'perf_stat', 'smr01_flag', 'gp_name', 'survival_days', 'gp_id'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

ustan_patient_details = {'tag': 'patient_details', 'source': 'ustan.general', 'fields': ['chi', 'name', 'date_of_birth', 'first_seen_date', 'smid', 'smid1', 'dob', 'gender', 'religion', 'civil_st', 'ref_hospital', 'postcode', 'death_flag', 'dat_death'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

ustan_wearable_1 = {'tag': 'wearable', 'source': 'ustan.intentions', 'fields': ['chi', 'intention_id', 'intention_seq', 'first_intention', 'intention', 'first_regime', 'init_appointment_date', 'appointment_date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False} 
ustan_wearable_2 = {'tag': 'wearable', 'source': 'ustan.regimes', 'fields': ['chi', 'intention_id', 'regime_id', 'regime_seq', 'intention', 'prev_regime', 'first_regime', 'regime', 'init_appointment_date', 'appointment_date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

ustan_inpatient = {'tag': 'inpatient', 'source': 'ustan.smr01', 'fields': ['chi', 'incidence_date', 'admission_date', 'length_of_stay', 'other_condition1', 'other_condition2', 'other_condition3', 'main_operation_b', 'discharge_date', 'waiting_list_type', 'main_condition', 'main_operation_a', 'marital_status', 'ethnic_group'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

ustan_breast_cancer_information = {'tag': 'breast_cancer_information', 'source': 'ustan.smr06', 'fields': ['chi', 'incidence_date', 'er_status', 'her2_status', 'stage_clinical_t', 'stage_clinical_n', 'stage_clinical_m', 'num_positive', 'pathological_tum_size'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

ustan_all_1 = {'tag': 'all', 'source': 'ustan.cycles', 'fields': ['chi', 'regime_id', 'intention_id', 'cycle_id', 'drug_names', 'diagnosis', 'init_appointment_date', 'elapsed_days', 'interval_days', 'appointment_date', 'intention', 'regime', 'cycle', 'p_ps', 'ps', 'nausea', 'vomiting', 'diarrhoea', 'constipation', 'oralMucositis', 'oesophagitis', 'neurotoxicity', 'handFoot', 'skin', 'hypersensitivity', 'fatigue', 'required_doses'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
ustan_all_2 = {'tag': 'all', 'source': 'ustan.general', 'fields': ['chi', 'incidence_date', 'site_icd_10', 'name', 'date_of_birth', 'first_seen_date', 'site', 'histology', 'primary', 'metastasis1', 'metastasis2', 'metastasis3', 'smid', 'smid1', 'cong_heart_fail_flag', 'con_tiss_disease_rheum_flag', 'dementia_flag', 'pulmonary_flag', 'con_tiss_flag', 'diabetes_flag', 'para_hemiplegia_flag', 'renal_flag', 'liver_flag', 'aids_hiv_flag', 'cancer_flag', 'charlson_score', 'dob', 'age', 'simd', 'simd1', 'side', 'gender', 'age_at_diagnosis', 'weight', 'bmi', 'height', 'religion', 'civil_st', 'ref_hospital', 'postcode_pre', 'postcode_suf', 'stage', 'stage_detail', 'tnm_t', 'tnm_t_detail', 'tnm_n', 'tnm_n_detail', 'tnm_m', 'perf_stat', 'smr01_flag', 'postcode', 'gp_name', 'death_flag', 'survival_days', 'dat_death', 'gp_id'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
ustan_all_3 = {'tag': 'all', 'source': 'ustan.intentions', 'fields': ['chi', 'patient_id', 'intention_id', 'intention_seq', 'first_intention', 'regime_ratio', 'cycle_ratio', 'intention', 'first_regime', 'init_appointment_date', 'elapsed_days', 'appointment_date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
ustan_all_4 = {'tag': 'all', 'source': 'ustan.patients', 'fields': ['chi', 'patient_id', 'first_intention', 'appointment_date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
ustan_all_5 = {'tag': 'all', 'source': 'ustan.regimes', 'fields': ['chi', 'intention_id', 'regime_id', 'regime_seq', 'regime_ratio', 'cycle_ratio', 'intention', 'prev_regime', 'first_regime', 'regime', 'interval_days', 'elapsed_days', 'init_appointment_date', 'appointment_date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
ustan_all_6 = {'tag': 'all', 'source': 'ustan.smr01', 'fields': ['chi', 'incidence_date', 'admission_date', 'length_of_stay', 'other_condition1', 'other_condition2', 'other_condition3', 'main_operation_b', 'discharge_date', 'waiting_list_type', 'main_condition', 'main_operation_a', 'marital_status', 'ethnic_group'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
ustan_all_7 = {'tag': 'all', 'source': 'ustan.smr06', 'fields': ['chi', 'incidence_date', 'er_status', 'her2_status', 'stage_clinical_t', 'stage_clinical_n', 'stage_clinical_m', 'num_positive', 'pathological_tum_size'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}


ustan_tags = [
    ustan_chemotherapy, 
    ustan_medication_1, 
    ustan_medication_2, 
    ustan_medication_3, 
    ustan_patient_appointments_1, 
    ustan_patient_appointments_2, 
    ustan_patient_appointments_3, 
    ustan_predictor_1, 
    ustan_predictor_2, 
    ustan_treatment_outcome, 
    ustan_diagnostic, 
    ustan_patient_details, 
    ustan_wearable_1, 
    ustan_wearable_2, 
    ustan_inpatient, 
    ustan_breast_cancer_information, 
    ustan_all_1, 
    ustan_all_2, 
    ustan_all_3, 
    ustan_all_4, 
    ustan_all_5, 
    ustan_all_6, 
    ustan_all_7          
]
