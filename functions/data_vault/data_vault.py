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
    boilerplate['hubs'] = {hub: [] for hub in hubs}
    boilerplate['links'] = {link: [] for link in links}
    return boilerplate

def get_id_columns(link):
    id_columns = {
        'time_person_link': ['time_id', 'person_id'], 
        'time_object_link': ['time_id', 'object_id'], 
        'time_location_link': ['time_id', 'location_id'], 
        'time_event_link': ['time_id', 'event_id'],
        'person_object_link': ['person_id', 'object_id'], 
        'person_location_link': ['person_id', 'location_id'], 
        'person_event_link': ['person_id', 'event_id'],
        'object_location_link': ['object_id', 'location_id'], 
        'object_event_link': ['object_id', 'event_id'],
        'location_event_link': ['location_id', 'event_id']
    }
    return id_columns[link]

def create_data_vault(satellites):
    sats = copy.deepcopy(satellites)
    boilerplate = generate_boilerplate()
    results = {}
    for hospital in sats:
        for table in sats[hospital]:
            satellite_definitions = sats[hospital][table]
            links = sats[hospital][table]['links']
            print(links)
            for satellite_name in satellite_definitions:
                if satellite_name != 'links':
                    print(satellite_name)
                    print(satellite_definitions[satellite_name])
                    hub = satellite_definitions[satellite_name]['hub']
                    for row in satellite_definitions[satellite_name]['data']:
                        next_hub_val = len(boilerplate['hubs'][hub]) + 1
                        boilerplate['hubs'][hub].append(next_hub_val)
                        row.update({f'{hub}_id': next_hub_val})
                        print(row)
            print('\n')
    print(boilerplate)