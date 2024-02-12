import folium
import networkx as nx
import osmnx as ox
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


def associate_clusters_with_points(clusters_list, points):
    res = []

    for i in range(len(clusters_list)):
        res.append((points[i], clusters_list[i]))
    return res


def form_graph(points):
    graph = nx.Graph()

    graph.add_nodes_from(points)

    for node_1 in points:
        for node_2 in points:
            graph.add_edge(node_1, node_2)

    return graph


def find_shortest_path(points):
    graph = form_graph(points)
    p = []
    for i in range(len(points)-1):
        p.append(nx.bellman_ford_path(graph, points[i], points[i+1]))

    return p


def draw_map(path, i):
    map = folium.Map(root)
    for p in path:
        for pt in p:
            map.add_child(folium.Marker([pt[0], pt[1]]))
        map.add_child(folium.PolyLine(p))

    map.save(f'path_{i}.html')


n_cl = 3
cl = find_clusters(n_cl, coordinates)
points_with_clusters = associate_clusters_with_points(cl, coordinates)

root = mahachkala

p = []
for i in range(n_cl):

    coord = []
    for point in points_with_clusters:
        if point[1] == i:
            coord.append(point[0])

    coord.append(root)
    path = find_shortest_path(coord)

    draw_map(path, i)
