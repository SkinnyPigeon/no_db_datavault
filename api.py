import json
from functions.get_source_data import get_patient_data
from functions.data_vault.satellites import process_satellites
from functions.data_vault.data_vault import create_data_vault
from functions.data_vault.hub_post_processing import hub_equalizer
from functions.data_vault.link_post_processing import add_id_values

body = {
  "serums_id": 364,
  "rule_id": "RULE_0df8eb8b-a469-46ae-8119-fbf98fa05b92",
  "tags": [
    "all"
  ],
  "hospital_ids": [
    "USTAN",
    "FCRB",
    "ZMC"
  ],
  "public_key": "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCDM+DNCybR7LdizOcK1gH2P7dD\nsajGUEIoPFp7wjhgKykYkCGVQCvl55g/zdh6UI9Cd/i2IEf5wo+Ct9oihy9SnJSp\n3sOp1KESV+ElwdK3vkaIo1AUuj+E8LTe7llyJ61JJdZaozyT0PxM8jB2vIaNEdbO\nbURHcIsIDc64L0e1ZQIDAQAB\n-----END PUBLIC KEY-----"
}

data = get_patient_data(body)
print(data['USTAN']['data']['ustan.general'])
print('\n')
satellites = process_satellites(data)
data_vault = create_data_vault(satellites)
print(data_vault['satellites'])
print('\n')
add_id_values(data_vault['links'])
print(data_vault['links'])
print('\n')
hub_equalizer(data_vault['hubs'])
print(data_vault['hubs'])