fcrb_diagnostic_1 = {'tag': 'diagnostic', 'source': 'fcrb.diagnostic', 'fields': ['einri', 'patnr', 'falnr', 'pernr', 'lfdnr', 'dkey1'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
fcrb_diagnostic_2 = {'tag': 'diagnostic', 'source': 'fcrb.episode', 'fields': ['patnr', 'falnr'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

# fcrb_patient_details_1 = {'tag': 'patient_details', 'source': 'fcrb.diagnostic', 'fields': ['patnr'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
# fcrb_patient_details_2 = {'tag': 'patient_details', 'source': 'fcrb.episode', 'fields': ['patnr'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
fcrb_patient_details_3 = {'tag': 'patient_details', 'source': 'fcrb.medication', 'fields': ['patnr', 'falnr'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
# fcrb_patient_details_4 = {'tag': 'patient_details', 'source': 'fcrb.monitoring_params', 'fields': ['patnr'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
# fcrb_patient_details_5 = {'tag': 'patient_details', 'source': 'fcrb.order_entry', 'fields': ['patnr'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
# fcrb_patient_details_6 = {'tag': 'patient_details', 'source': 'fcrb.patient_address', 'fields': ['patnr'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
fcrb_patient_details_7 = {'tag': 'patient_details', 'source': 'fcrb.patient', 'fields': ['patnr', 'gschl', 'nname', 'vname', 'gbdat', 'gbnam', 'namzu', 'glrand', 'famst', 'telf1', 'rvnum'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
fcrb_patient_details_8 = {'tag': 'patient_details', 'source': 'fcrb.vital_signs', 'fields': ['patnr', 'falnr', 'vppid', 'dttyp', 'erdat', 'typevs', 'vwert', 'vbem'], 'key_lookup': {}, 'table': True, 'graph': True, 'image': False}

fcrb_healthcare_providers_1 = {'tag': 'healthcare_providers', 'source': 'fcrb.diagnostic', 'fields': ['patnr', 'einri', 'falnr', 'pernr'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
fcrb_healthcare_providers_2 = {'tag': 'healthcare_providers', 'source': 'fcrb.episode', 'fields': ['patnr', 'pernr', 'einri', 'einzg', 'casetx'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
# fcrb_healthcare_providers_3 = {'tag': 'healthcare_providers', 'source': 'fcrb.medical_specialty', 'fields': ['orgid', 'orgna'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
fcrb_healthcare_providers_4 = {'tag': 'healthcare_providers', 'source': 'fcrb.medication', 'fields': ['patnr', 'falnr', 'einri'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
fcrb_healthcare_providers_5 = {'tag': 'healthcare_providers', 'source': 'fcrb.monitoring_params', 'fields': ['patnr', 'pernr'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
fcrb_healthcare_providers_6 = {'tag': 'healthcare_providers', 'source': 'fcrb.order_entry', 'fields': ['patnr', 'einri', 'pernr', 'orgid'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
# fcrb_healthcare_providers_7 = {'tag': 'healthcare_providers', 'source': 'fcrb.professional', 'fields': ['pernr', 'orgid', 'erdat'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

fcrb_patient_appointments_1 = {'tag': 'patient_appointments', 'source': 'fcrb.episode', 'fields': ['patnr', 'pernr', 'falar', 'statu', 'enddt', 'storn', 'begdt', 'casetx', 'fatxt'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
fcrb_patient_appointments_2 = {'tag': 'patient_appointments', 'source': 'fcrb.monitoring_params', 'fields': ['patnr', 'falnr'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
fcrb_patient_appointments_3 = {'tag': 'patient_appointments', 'source': 'fcrb.order_entry', 'fields': ['patnr', 'idodr', 'falnr'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
fcrb_patient_appointments_4 = {'tag': 'patient_appointments', 'source': 'fcrb.vital_signs', 'fields': ['patnr', 'falnr', 'erdat'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

fcrb_treatments = {'tag': 'treatments', 'source': 'fcrb.episode', 'fields': ['patnr', 'bekat'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

fcrb_medication = {'tag': 'medication', 'source': 'fcrb.medication', 'fields': ['patnr', 'mpresnr', 'motx', 'mostx', 'motypid', 'erdat'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

fcrb_documents = {'tag': 'documents', 'source': 'fcrb.medication', 'fields': ['patnr', 'mostx'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

fcrb_additional_information_1 = {'tag': 'additional_information', 'source': 'fcrb.medication', 'fields': ['patnr', 'erdat', 'storn', 'stusr', 'stdat', 'stoid'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
fcrb_additional_information_2 = {'tag': 'additional_information', 'source': 'fcrb.monitoring_params', 'fields': ['patnr', 'vbem'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
fcrb_additional_information_3 = {'tag': 'additional_information', 'source': 'fcrb.order_entry', 'fields': ['patnr', 'erdat'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
# fcrb_additional_information_4 = {'tag': 'additional_information', 'source': 'fcrb.professional', 'fields': ['erusr', 'orgid', 'gbdat', 'begdt', 'enddt'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

fcrb_wearable_1 = {'tag': 'wearable', 'source': 'fcrb.monitoring_params', 'fields': ['patnr', 'vppid', 'vbem', 'datyp', 'wertogr', 'wertugr', 'wertmax', 'wertmin'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
fcrb_wearable_2 = {'tag': 'wearable', 'source': 'fcrb.vital_signs', 'fields': ['patnr', 'idvs', 'vppid', 'dttyp', 'typevs', 'vwert', 'vbem'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

fcrb_patient_address = {'tag': 'patient_address', 'source': 'fcrb.patient_address', 'fields': ['patnr', 'pstlz', 'stras', 'land', 'ort', 'deck', 'adrnr'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

fcrb_personal = {'tag': 'personal', 'source': 'fcrb.patient', 'fields': ['patnr', 'gschl', 'nname', 'vname', 'gbdat', 'gbnam', 'namzu', 'glrand', 'famst', 'telf1'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

fcrb_all_1 =  {'tag': 'all', 'source': 'fcrb.diagnostic', 'fields': ['einri', 'patnr', 'falnr', 'pernr', 'lfdnr', 'dkey1'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
fcrb_all_2 =  {'tag': 'all', 'source': 'fcrb.episode', 'fields': ['falnr', 'pernr', 'einri', 'falar', 'patnr', 'bekat', 'einzg', 'statu', 'krzan', 'enddt', 'erdat', 'storn', 'begdt', 'casetx', 'fatxt', 'enddtx'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
# fcrb_all_3 =  {'tag': 'all', 'source': 'fcrb.medical_specialty', 'fields': ['orgid', 'orgna'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
fcrb_all_4 =  {'tag': 'all', 'source': 'fcrb.medication', 'fields': ['mpresnr', 'patnr', 'falnr', 'pernr', 'einri', 'motx', 'mostx', 'motypid', 'erdat', 'storn', 'stusr', 'stdat', 'stoid'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
fcrb_all_5 =  {'tag': 'all', 'source': 'fcrb.monitoring_params', 'fields': ['patnr', 'falnr', 'vppid', 'pernr', 'vbem' , 'datyp', 'wertogr', 'wertugr', 'wertmax', 'wertmin'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
fcrb_all_6 =  {'tag': 'all', 'source': 'fcrb.order_entry', 'fields': ['idodr', 'einri', 'falnr', 'patnr', 'pernr', 'erdat', 'orgid'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
fcrb_all_7 =  {'tag': 'all', 'source': 'fcrb.patient_address', 'fields': ['patnr', 'pstlz', 'stras', 'land', 'ort', 'deck', 'adrnr'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
fcrb_all_8 =  {'tag': 'all', 'source': 'fcrb.patient', 'fields': ['patnr', 'gschl', 'nname', 'vname', 'gbdat', 'gbnam', 'namzu', 'glrand', 'famst', 'telf1', 'rvnum'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
# fcrb_all_9 =  {'tag': 'all', 'source': 'fcrb.professional', 'fields': ['pernr', 'erusr', 'orgid', 'gbdat', 'begdt', 'enddt', 'erdat', 'rank'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
fcrb_all_10 =  {'tag': 'all', 'source': 'fcrb.vital_signs', 'fields': ['idvs', 'patnr', 'falnr', 'vppid', 'dttyp', 'erdat', 'typevs', 'vwert', 'vbem'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}


fcrb_tags = [
    fcrb_diagnostic_1, 
    fcrb_diagnostic_2, 
    # fcrb_patient_details_1, 
    # fcrb_patient_details_2, 
    fcrb_patient_details_3, 
    # fcrb_patient_details_4, 
    # fcrb_patient_details_5, 
    # fcrb_patient_details_6, 
    fcrb_patient_details_7, 
    fcrb_patient_details_8, 
    fcrb_healthcare_providers_1, 
    fcrb_healthcare_providers_2, 
    # fcrb_healthcare_providers_3, 
    fcrb_healthcare_providers_4, 
    fcrb_healthcare_providers_5, 
    fcrb_healthcare_providers_6, 
    # fcrb_healthcare_providers_7, 
    fcrb_patient_appointments_1, 
    fcrb_patient_appointments_2, 
    fcrb_patient_appointments_3, 
    fcrb_patient_appointments_4, 
    fcrb_treatments, 
    fcrb_medication, 
    fcrb_documents, 
    fcrb_additional_information_1, 
    fcrb_additional_information_2, 
    fcrb_additional_information_3, 
    # fcrb_additional_information_4, 
    fcrb_wearable_1, 
    fcrb_wearable_2, 
    fcrb_patient_address, 
    fcrb_personal, 
    fcrb_all_1, 
    fcrb_all_2, 
    # fcrb_all_3, 
    fcrb_all_4, 
    fcrb_all_5, 
    fcrb_all_6, 
    fcrb_all_7, 
    fcrb_all_8, 
    # fcrb_all_9, 
    fcrb_all_10
]
