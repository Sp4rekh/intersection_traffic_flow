import matplotlib.pyplot as plt
import math
import numpy as np

class Vertex:
    def __init__(self, label: str):
        self.label = label

class Edge: 
    def __init__(self, v1: Vertex, v2: Vertex, directed: bool):
        self.v1 = v1
        self.v2 = v2
        self.weight = 0
        if directed:
            self.direction = (v1, v2)
        else:
            self.direction = None
        
    
    def set_weight(self, weight: float):
        self.weight = weight
    
    def contains_vertex(self, vertex: Vertex):
        return self.v1 == vertex or self.v2 == vertex

        
class Graph:
    def __init__(self):
        self.nodes = list()
        self.edges = list()

    def add_node(self, node: Vertex):
        self.nodes.append(node)
    
    def add_edge(self, edge: Edge):
        self.edges.append(edge)

    def get_nodes(self):
        return self.nodes

    def get_edges(self):
        return self.edges

    def get_neighbors(self, node: Vertex):
        neighbors = []
        for edge in self.edges:
            if edge.v1 == node:
                neighbors.append(edge.v2)
            elif edge.v2 == node:
                neighbors.append(edge.v1)
        return neighbors
    
    def count_edges(self):
        return len(self.edges)

    def count_nodes(self):
        return len(self.nodes)
    
    def get_degree(self, node: Vertex):
        degree = 0
        for edge in self.edges:
            if edge.v1.label == node.label or edge.v2.label == node.label:
                degree += 1
        return degree
    
    def get_degree_sequence(self):
        degree_sequence = []
        for node in self.nodes:
            degree_sequence.append(self.get_degree(node))
        degree_sequence.sort(reverse=True)
        return degree_sequence
    
    def get_max_degree(self):
        return max(self.get_degree_sequence())
    
    def get_min_degree(self):
        return min(self.get_degree_sequence())
    
    def get_average_degree(self):
        return sum(self.get_degree_sequence()) / len(self.nodes)
    

    
    def describe(self):
        print("Nodes:")
        for node in self.nodes:
            print(f" - {node.label}")
        print("Edges:")
        for edge in self.edges:
            direction = "->" if edge.direction else "--"
            print(f" - {edge.v1.label} {direction} {edge.v2.label} (weight: {edge.weight})")

    def visualise(self, node_states=None):
        coordinates = {}
        num_nodes = len(self.nodes)

        for v_index in range(num_nodes):
            vertex = list(self.nodes)[v_index].label
            angle = 2 * math.pi * v_index / num_nodes
            coordinates[vertex] = (math.cos(angle), math.sin(angle))

        # 2. Plot EACH node individually with its custom color
        for v in self.nodes:
            x, y = coordinates[v.label]
            
            # Determine color based on the RL state dictionary mapping
            if node_states is not None and v in node_states:
                state = node_states[v]
                if state == 1:
                    color = 'green'   # Part of the Maximum Independent Set
                elif state == -1:
                    color = 'red'     # Banned node (neighbor of a chosen node)
                else:
                    color = 'blue'    # Unselected but eligible (state == 0)
            else:
                color = 'blue'        # Default color if no states are passed
                
            # Plot this single vertex marker with the specified color
            plt.plot(x, y, 'o', color=color, markersize=10)
            
            # Add the text label
            plt.text(x, y + 0.05, v.label, fontsize=12, ha='center', va='bottom')

        for edge in list(self.edges):
            

            v1 = edge.v1.label
            v2 = edge.v2.label
            
            x_values = [coordinates[v1][0], coordinates[v2][0]]
            y_values = [coordinates[v1][1], coordinates[v2][1]]
            plt.plot(x_values, y_values, 'k-', alpha=0.3)

        plt.show()




    def get_complement(self):
        complement_graph = Graph()
        for node in self.nodes:
            complement_graph.add_node(node)
        
        currentEdges = self.edges
        i = 0
        edge_tuples = []
        for i in range(len(self.nodes)):
            for j in range(i + 1, len(self.nodes)):
                v1 = self.nodes[i]
                v2 = self.nodes[j]
                
                edge_tuples.append((v1.label, v2.label))

        print("\n\n")
        for edge in currentEdges:
            if (edge.v1.label, edge.v2.label) in edge_tuples:
                edge_tuples.remove((edge.v1.label, edge.v2.label))
                
        for (i,j) in edge_tuples:
            complement_graph.add_edge(Edge(Vertex(i), Vertex(j), directed=False))
        print(len(complement_graph.edges))
        print(i)

                
        
        return complement_graph

    def delete_nodes(self, nodes_to_delete:set):
        new_graph = Graph()
        for node in self.get_nodes():
            if node not in nodes_to_delete:
                new_graph.add_node(node)

        for edge in self.get_edges():
            if edge.v1 not in nodes_to_delete and edge.v2 not in nodes_to_delete:
                new_graph.add_edge(edge)

        return new_graph



        
    