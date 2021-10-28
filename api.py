import json
from functions.get_source_data import get_patient_data
from functions.data_vault.satellites import process_satellites
from functions.data_vault.data_vault import create_data_vault
body = {
  "serums_id": 364,
  "rule_id": "RULE_0df8eb8b-a469-46ae-8119-fbf98fa05b92",
  "tags": [
    "all"
  ],
  "hospital_ids": [
    "ZMC",
    "FCRB",
    "USTAN"
  ],
  "public_key": "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCDM+DNCybR7LdizOcK1gH2P7dD\nsajGUEIoPFp7wjhgKykYkCGVQCvl55g/zdh6UI9Cd/i2IEf5wo+Ct9oihy9SnJSp\n3sOp1KESV+ElwdK3vkaIo1AUuj+E8LTe7llyJ61JJdZaozyT0PxM8jB2vIaNEdbO\nbURHcIsIDc64L0e1ZQIDAQAB\n-----END PUBLIC KEY-----"
}

data = get_patient_data(body)
satellites = process_satellites(data)
# print(satellites)
# print('\n')
data_vault = create_data_vault(satellites)
# print(data_vault)
print(data_vault['satellites'])
print('\n')
print(data_vault['links'])
print('\n')
print(data_vault['hubs'])
print('\n')

d = data_vault['hubs']['hub_time']
max_key = max(d, key= lambda x: len(set(d[x])))
print(max_key)
print(len(d[max_key]))
for key in d:
  while len(d[key]) < len(d[max_key]):
    d[key].append(None)

for key in d:
  print(key)
  print(len(d[key]))
import pandas as pd

df = pd.DataFrame(d)
print(df)
df.to_csv('./check.csv')