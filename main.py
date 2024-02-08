import networkx as nx
import folium
from sklearn.cluster import KMeans


mahachkala = (42.976400, 47.502400)
sulak = (43.0374789, 46.8058487)
tobot = (42.555510, 46.718823)
hansky = (42.605005, 46.572823)
goor = (42.607455, 46.568507)
kahib = (42.429077, 46.596539)
karadah = (42.456050, 46.891464)
gamsutl = (42.303910, 46.996741)
mayak = (42.401175, 46.8785923)
saltynskii = (42.402544, 47.062999)
lun = (41.940875, 48.379311)
derb_krep = (42.052582, 48.274079)
sarykym = (43.008100, 47.235200)
troll = (42.607455, 46.568507)
naryn_kala = (42.052850, 48.274300)
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


def find_clusters(n_clust, points):
    kmeans = KMeans(n_clusters=n_clust)
    kmeans.fit(points)
    return kmeans.labels_


def form_graph(points):
    graph = nx.Graph()

    graph.add_nodes_from(points)

    for node_1 in points:
        for node_2 in points:
            graph.add_edge(node_1, node_2)

    return graph


def find_shortest_path(start_point, points):
    graph = form_graph(points)
    return nx.single_source_dijkstra(graph, start_point)


def draw_map(path):
    map = folium.Map((coordinates[0][0], coordinates[0][1]))
    for pt in coordinates:
        marker = folium.Marker([pt[0], pt[1]])
        map.add_child(marker)
        map.add_to(folium.Polygon(path))
    map.save('points.html')
