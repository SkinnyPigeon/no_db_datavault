def add_id_values(links):
    for link_name in links:
        link = links[link_name]
        max_key = max(link, key=lambda x: len(set(link[x])))
        for i, value in enumerate(link[max_key]):
            link['id'].append(i + 1)
