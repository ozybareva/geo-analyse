import folium
import networkx as nx
from sklearn.cluster import KMeans


def find_clusters(n_clust, points):
    kmeans = KMeans(n_clusters=n_clust)
    kmeans.fit(points)
    return kmeans.labels_


def associate_clusters_with_points(clusters_list, points):
    return [(points[n_clust], clusters_list[n_clust]) for n_clust in range(len(clusters_list))]


def form_graph(points):
    graph = nx.Graph()

    graph.add_nodes_from(points)

    for node_1 in points:
        for node_2 in points:
            graph.add_edge(node_1, node_2)

    return graph


def find_shortest_path(points: list):
    graph = form_graph(points)
    path = [nx.bellman_ford_path(graph, points[i], points[i+1]) for i in range(len(points)-1)]
    return path


def draw_map(path: list, n_clust: int):
    map = folium.Map()
    for p in path:
        for pt in p:
            map.add_child(folium.Marker([pt[0], pt[1]]))
        map.add_child(folium.PolyLine(p))

    map.save(f'path_{n_clust}.html')


def build_routes_by_coordinates(point_coordinates: list):
    n_clust = 3
    clusters = find_clusters(n_clust, point_coordinates)
    points_with_clusters = associate_clusters_with_points(clusters, point_coordinates)

    for i in range(n_clust):
        coord = [(point[0]) for point in points_with_clusters if point[1] == i]
        path = find_shortest_path(coord)

        draw_map(path, i)
