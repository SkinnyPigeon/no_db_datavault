def hub_equalizer(hubs):
    for hub_name in hubs:
        hub = hubs[hub_name]
        max_key = max(hub, key=lambda x: len(set(hub[x])))
        for key in hub:
            while len(hub[key]) < len(hub[max_key]):
                hub[key].append(None)