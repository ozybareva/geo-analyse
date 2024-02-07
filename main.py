import osmnx as ox
import networkx as nx
import folium


mahachkala = (42.9764, 47.5024)
sulak = (43.0374789, 46.8058487)
tobot = (42.55551, 46.718823)
hansky = (42.605005, 46.572823)
goor = (42.607455, 46.568507)
kahib = (42.429077, 46.596539)
karadah = (42.456050, 46.891464)
gamsutl = (42.303910, 46.996741)
mayak = (42.40117515832516, 46.878592382755656)
saltynskii = (42.402544749432, 47.0629996061325)
lun = (41.940875, 48.379311)
derb_krep = (42.052582, 48.274079)
sarykym = (43.0081, 47.2352)
troll = (42.607455, 46.568507)
naryn_kala = (42.05285, 48.27430)
chirk_ges = (42.984122, 46.869878)

coordinates = [
    mahachkala,
    sulak,
    tobot,
    hansky,
    goor,
    kahib,
    karadah,
    gamsutl,
    mayak,
    saltynskii,
    lun,
    derb_krep,
    sarykym,
    troll,
    naryn_kala,
    chirk_ges,
]

map = folium.Map((coordinates[0][0], coordinates[0][1]))
for pt in coordinates:
    marker = folium.Marker([pt[0], pt[1]])
    map.add_child(marker)
map.save('points.html')

root = mahachkala
G = ox.graph_from_point(root)
print(G)

path = []
for node_1, node_2 in zip(coordinates, coordinates[1:]):
    orig = ox.nearest_nodes(G, node_1[0], node_1[1])
    dest = ox.nearest_nodes(G, node_2[0], node_2[1])
    path.append(ox.shortest_path(G, orig, dest))

route_map = ox.plot_graph_routes(G, path, save=True, route_colors='g')




