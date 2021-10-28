def boilerplate():
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
    print(boilerplate)

def create_data_vault(satellites):
    print(satellites)
    boilerplate()