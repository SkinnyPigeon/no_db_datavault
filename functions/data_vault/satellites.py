from sources.keys_and_sats.zmc_keys_and_sats import zmc_sats
from sources.keys_and_sats.fcrb_keys_and_sats import fcrb_sats
from sources.keys_and_sats.ustan_keys_and_sats import ustan_sats

def hospital_picker(hospital):
    if hospital == 'ZMC':
        return zmc_sats
    elif hospital == 'FCRB':
        return fcrb_sats
    elif hospital == 'USTAN':
        return ustan_sats

def process_satellites(data):
    results = {}
    for hospital in data:
        results[hospital] = {}
        satellite_definitions = hospital_picker(hospital)
        for table_name in data[hospital]['data']:
            source_data = data[hospital]['data'][table_name]
            results[hospital][table_name] = {}
            results[hospital][table_name]['links'] = satellite_definitions[table_name]['links']
            for satellite_name in satellite_definitions[table_name]:
                if satellite_name != 'links':
                    columns = satellite_definitions[table_name][satellite_name]['columns']
                    results
                    results[hospital][table_name][satellite_name] = {}
                    results[hospital][table_name][satellite_name]['hub'] = satellite_definitions[table_name][satellite_name]['hub']
                    results[hospital][table_name][satellite_name]['data'] = [{k: row[k] for k in row if k in columns} for row in source_data]
    return results

            
