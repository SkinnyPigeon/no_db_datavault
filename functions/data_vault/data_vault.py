import copy

def generate_boilerplate():
    hubs = ['hub_time', 'hub_person', 'hub_object', 'hub_location', 'hub_event']
    links = [
        'time_person_link', 'time_object_link', 'time_location_link', 'time_event_link',
        'person_object_link', 'person_location_link', 'person_event_link',
        'object_location_link', 'object_event_link',
        'location_event_link'
    ]
    boilerplate = {}
    boilerplate['hubs'] = {hub: {'id': []} for hub in hubs}
    boilerplate['links'] = {link: get_id_columns(link) for link in links}
    return boilerplate

def get_id_columns(link):
    id_columns = {
        'time_person_link': {'id': [], 'time_id': [], 'person_id': []}, 
        'time_object_link': {'id': [], 'time_id': [], 'object_id': []}, 
        'time_location_link': {'id': [], 'time_id': [], 'location_id': []}, 
        'time_event_link': {'id': [], 'time_id': [], 'event_id': []},
        'person_object_link': {'id': [], 'person_id': [], 'object_id': []}, 
        'person_location_link': {'id': [], 'person_id': [], 'location_id': []}, 
        'person_event_link': {'id': [], 'person_id': [], 'event_id': []},
        'object_location_link': {'id': [], 'object_id': [], 'location_id': []}, 
        'object_event_link': {'id': [], 'object_id': [], 'event_id': []},
        'location_event_link': {'id': [], 'location_id': [], 'event_id': []}
    }
    return id_columns[link]

# def create_data_vault(satellites):
#     sats = copy.deepcopy(satellites)
#     boilerplate = generate_boilerplate()
#     results = {}
#     for hospital in sats:
#         results = {}
#         results['satellites'] = {}
#         results['hubs'] = {}
#         results['links'] = {}
#         for table in sats[hospital]:
#             satellite_definitions = sats[hospital][table]
#             links = sats[hospital][table]['links']
#             for satellite_name in satellite_definitions:
#                 if satellite_name != 'links':
#                     hub = satellite_definitions[satellite_name]['hub']
#                     keys = satellite_definitions[satellite_name]['keys']
#                     hub_class = hub.split('_')[1] + '_id'
#                     for i, row in enumerate(satellite_definitions[satellite_name]['data']):
#                         next_hub_val = len(boilerplate['hubs'][hub]['id']) + 1
#                         for key in keys[i]:
#                             try:
#                                 while len(boilerplate['hubs'][hub][key]) < len(boilerplate['hubs'][hub]['id']):
#                                     boilerplate['hubs'][hub][key].append(None)
#                                 boilerplate['hubs'][hub][key].append(keys[i][key])
#                             except:
#                                 boilerplate['hubs'][hub][key] = []
#                                 while len(boilerplate['hubs'][hub][key]) < len(boilerplate['hubs'][hub]['id']):
#                                     boilerplate['hubs'][hub][key].append(None)
#                                 boilerplate['hubs'][hub][key].append(keys[i][key])
#                         row.update({f'{hub}_id': next_hub_val})
#                         boilerplate['hubs'][hub]['id'].append(next_hub_val)
#                         for link in links:
#                             if hub_class in boilerplate['links'][link]:
#                                 boilerplate['links'][link][hub_class].append(next_hub_val)
#                     results['satellites'][f'{hospital.lower()}_{satellite_name}'] = satellite_definitions[satellite_name]['data']
#     results['hubs'] = boilerplate['hubs']
#     results['links'] = boilerplate['links']
#     return results

def create_data_vault(satellites):
    sats = copy.deepcopy(satellites)
    boilerplate = generate_boilerplate()
    results = {}
    for hospital in sats:
        results = {}
        results['satellites'] = {}
        results['hubs'] = {}
        results['links'] = {}
        for table in sats[hospital]:
            if table == "ustan.general":
                satellite_definitions = sats[hospital][table]
                links = sats[hospital][table]['links']
                for satellite_name in satellite_definitions:
                    if satellite_name != 'links':
                        hub = satellite_definitions[satellite_name]['hub']
                        keys = satellite_definitions[satellite_name]['keys']
                        hub_class = hub.split('_')[1] + '_id'
                        for i, row in enumerate(satellite_definitions[satellite_name]['data']):
                            next_hub_val = len(boilerplate['hubs'][hub]['id']) + 1
                            for key in keys[i]:
                                try:
                                    while len(boilerplate['hubs'][hub][key]) < len(boilerplate['hubs'][hub]['id']):
                                        boilerplate['hubs'][hub][key].append(None)
                                    boilerplate['hubs'][hub][key].append(keys[i][key])
                                except:
                                    boilerplate['hubs'][hub][key] = []
                                    while len(boilerplate['hubs'][hub][key]) < len(boilerplate['hubs'][hub]['id']):
                                        boilerplate['hubs'][hub][key].append(None)
                                    boilerplate['hubs'][hub][key].append(keys[i][key])
                            row.update({f'{hub}_id': next_hub_val})
                            boilerplate['hubs'][hub]['id'].append(next_hub_val)
                            for link in links:
                                if hub_class in boilerplate['links'][link]:
                                    boilerplate['links'][link][hub_class].append(next_hub_val)
                        results['satellites'][f'{hospital.lower()}_{satellite_name}'] = satellite_definitions[satellite_name]['data']
    results['hubs'] = boilerplate['hubs']
    results['links'] = boilerplate['links']
    return results