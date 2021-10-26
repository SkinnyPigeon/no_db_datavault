from sources.keys_and_sats.zmc_keys_and_sats import zmc_sats

def hospital_picker(hospital):
    if hospital == 'ZMC':
        return zmc_sats

def process_satellites(data):
    for hospital in data:
        satellite_definitions = hospital_picker(hospital)
        # print(satellite_definitions)
        for table_name in data[hospital]['data']:
            table = data[hospital]['data'][table_name]
            print(table_name)
            print(table)
            print(satellite_definitions[table_name])
            print('\n')
            
