def get_map(places=["Dhaka District, Dhaka Division, Bangladesh"]):

    G = ox.graph_from_place(places, network_type="all", simplify=True)
    return G
