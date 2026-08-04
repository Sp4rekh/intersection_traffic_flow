import custom_graph.core as Graphs

simple_graph = Graphs.Graph()
simple_graph.add_node(Graphs.Vertex("A"))
simple_graph.add_node(Graphs.Vertex("B"))
simple_graph.add_edge(Graphs.Edge(Graphs.Vertex("A"), Graphs.Vertex("B"), directed=False))

def test_simple_graph_nodes():
    assert len(simple_graph.nodes) == 2
    
def test_simple_graph_edges():    
    assert len(simple_graph.edges) == 1

def test_simple_graph_describe(capsys):
    simple_graph.describe()
    captured = capsys.readouterr()
    assert "Nodes:" in captured.out
    assert "Edges:" in captured.out
    assert "A" in captured.out
    assert "B" in captured.out
    assert "--" in captured.out