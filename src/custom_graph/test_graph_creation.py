import core as Graphs



def get_complete_graph(num_vertices):
    simple_graph = Graphs.Graph()
    for i in range(num_vertices):
        simple_graph.add_node(Graphs.Vertex(str(i)))
    for i in range(num_vertices - 1):
        for j in range(i+1, num_vertices):
            simple_graph.add_edge(Graphs.Edge(Graphs.Vertex(str(i)), Graphs.Vertex(str(j)), directed=False))
    return simple_graph


def get_turan_graph(num_vertices, num_partitions):
    nEach = int()
    nLeft = 0
    if num_vertices % num_partitions == 0:
        nEach = num_vertices // num_partitions
    else:
        nLeft = num_vertices % num_partitions
        nEach = num_vertices // num_partitions

    turan_graph = Graphs.Graph()
    for i in range(num_vertices):
        turan_graph.add_node(Graphs.Vertex(str(i)))

    partitions = []
    available_vertices = [v.label for v in turan_graph.nodes]
    for i in range(num_partitions):
        partition = []
        for j in range(nEach):
            vertex_label = available_vertices.pop(0)
            partition.append(vertex_label)
        if nLeft > 0:
            vertex_label = available_vertices.pop(0)
            partition.append(vertex_label)
            nLeft -= 1
        partitions.append(partition)

    for i in range(num_partitions):
        for j in range(i + 1, num_partitions):
            for v1 in partitions[i]:
                for v2 in partitions[j]:
                    turan_graph.add_edge(Graphs.Edge(Graphs.Vertex(v1), Graphs.Vertex(v2), directed=False))

    return turan_graph


# simple_graph = get_complete_graph(8)
# simple_graph.describe()
# simple_graph.visualise()

# simple_graph.get_complement().visualise()

# turan_graph = get_turan_graph(12, 3)
# turan_graph.describe()
# turan_graph.visualise()

# turan_complement = turan_graph.get_complement()
# turan_complement.describe()
# turan_complement.visualise()

simple_graph = Graphs.Graph()
for i in range(4):
    simple_graph.add_node(Graphs.Vertex(str(i)))
simple_graph.add_edge(Graphs.Edge(Graphs.Vertex("0"), Graphs.Vertex("1"), directed=False))
simple_graph.add_edge(Graphs.Edge(Graphs.Vertex("1"), Graphs.Vertex("3"), directed=False))
simple_graph.add_edge(Graphs.Edge(Graphs.Vertex("2"), Graphs.Vertex("3"), directed=False))
print(simple_graph.get_degree_sequence())
simple_graph.visualise()
simple_graph.get_complement().visualise()

