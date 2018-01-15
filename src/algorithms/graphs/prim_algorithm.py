import graphviz as gv


def get_parent(index):
    return (index-1)//2


def get_right(index):
    return 2*index + 2


def get_left(index):
    return 2*index + 1


# def edge_equals(edge1, edge2):
#     if edge1.get_v() == edge2.get_v() and edge1.get_w() == edge2.get_v():
#         return True
#
#
# def is_list_contain_edge(list_of_edges, x):
#     for i in range(len(list_of_edges)):
#         element = list_of_edges[i]
#         if edge_equals(element, x):
#             return True
#     return False


class Queue:

    def __init__(self):
        self._data = []

    def is_empty(self):
        return not len(self._data) > 0

    def push(self, edge):
        self._data.append(edge)
        self._up_heap()

    def pop(self):
        element = self._data[0]
        last_index = len(self._data) - 1

        self._data[0] = self._data[last_index]
        del self._data[last_index]
        if len(self._data) > 0:
            self._down_heap()
        return element

    def _up_heap(self):
        e_index = len(self._data) - 1
        e_value = self._data[e_index].get_weight()

        while e_index > 0:
            p_index = get_parent(e_index)
            p_value = self._data[p_index].get_weight()

            if p_value <= e_value:
                break

            self._swap(e_index, p_index)
            e_index = p_index

    def _down_heap(self):
        size = len(self._data)
        element = self._data[0]
        v_value = element.get_weight()
        i = 0
        j = 1
        while j < size:
            if j + 1 < size and self._data[j+1].get_weight() < self._data[j].get_weight():
                j += 1
            if v_value <= self._data[j].get_weight():
                break

            self._data[i] = self._data[j]
            i = j
            j = 2 * j + 1

        self._data[i] = element

    def _swap(self, index1, index2):
        tmp = self._data[index1]
        self._data[index1] = self._data[index2]
        self._data[index2] = tmp

    def _is_r_exist(self, index):
        return get_right(index) <= len(self._data) - 1

    def _is_l_exist(self, index):
        return get_right(index) < len(self._data) - 1

    def print(self):
        for edge in self._data:
            print("Edge v: " + str(edge._v) + ", w: " + str(edge._w) + ", weight: " + str(edge._weight))


class Edge:

    def __init__(self, v, w, weight):
        self._v = v
        self._w = w
        self._weight = weight
        self._index = None
        self._spanning = False

    def get_v(self):
        return self._v

    def get_w(self):
        return self._w

    def get_other(self, v):
        if v == self._v:
            return self._w
        else:
            return self._v

    def get_weight(self):
        return self._weight

    def get_index(self):
        return self._index

    def set_index(self, new_index):
        self._index = new_index

    def print(self):
        print('|' + str(self._v) + '-' + str(self._w) + '|' + ", weight: " + str(self._weight))

    def add_to_spanning(self):
        self._spanning = True

    def is_spanning(self):
        return self._spanning


class Graph:

    def __init__(self, size):
        self._vertex_count = size
        self._edge_count = 0
        self._neighbors = [[] for _ in range(size+1)]
        self._edges = []

    def add_edge(self, edge):
        # change
        self._edges.append(edge)
        # change

        v = edge.get_v()
        w = edge.get_w()
        self._neighbors[v].append(edge)
        self._neighbors[w].append(edge)

        self._edge_count += 1

    def get_neighbors(self, v):
        return self._neighbors[v]

    def print(self):
        for i in range(self._vertex_count):
            tab = self._neighbors[i+1]
            print('vertex no. ' + str(i+1))
            for edge in tab:
                edge.print()

    def get_size(self):
        return self._vertex_count

    def get_edges(self):
        return self._edges


class SpanningTree:

    def __init__(self, graph):
        self._graph = graph
        self._visited = [False for _ in range(graph.get_size()+1)]
        self._queue = Queue()
        self._spanning_tree = []

    def get_spanning_tree(self, start_v):
        if start_v > len(self._visited) + 1 or start_v < 0:
            raise ValueError

        self._visit(start_v)
        while not self._queue.is_empty():
            edge = self._queue.pop()
            v = edge.get_v()
            w = edge.get_w()

            if self._visited[v] and self._visited[w]:
                continue

            self._spanning_tree.append(edge)
            edge.add_to_spanning()

            if not self._visited[v]:
                self._visit(v)
            if not self._visited[w]:
                self._visit(w)

    def print(self):
        for edge in self._spanning_tree:
            edge.print()

    def _visit(self, v):
        self._visited[v] = True

        v_neighbors = self._graph.get_neighbors(v)
        for edge in v_neighbors:
            if not self._visited[edge.get_other(v)]:
                self._queue.push(edge)

    def get_edges(self):
        return self._spanning_tree


g = Graph(8)
g.add_edge(Edge(1, 2, 2))
g.add_edge(Edge(1, 4, 4))
g.add_edge(Edge(1, 6, 5))
g.add_edge(Edge(1, 3, 3))
g.add_edge(Edge(2, 5, 2))
g.add_edge(Edge(5, 3, 1))
g.add_edge(Edge(5, 4, 1))
g.add_edge(Edge(5, 6, 1))
g.add_edge(Edge(4, 7, 1))
g.add_edge(Edge(7, 8, 2))
g.add_edge(Edge(8, 6, 3))

spanning_tree = SpanningTree(g)
spanning_tree.get_spanning_tree(6)
spanning_tree.print()

# graph = graphx.Graph()
# for _ in range(9):
#     graph.insert_node()
#
# graph.add_edge(1, 2, directed=0)
# graph.add_edge(1, 4, directed=0)
# graph.add_edge(1, 6, directed=0)
# graph.add_edge(1, 3, directed=0)
# graph.add_edge(2, 5, directed=0)
# graph.add_edge(5, 3, directed=0)
# graph.add_edge(5, 4, directed=0)
# graph.add_edge(5, 6, directed=0)
# graph.add_edge(4, 7, directed=0)
# graph.add_edge(7, 8, directed=0)
# graph.add_edge(8, 6, directed=0)
#
# draw_graph.draw_net(graph.adj_mat)


graphEdges = g.get_edges()
resultTree = spanning_tree.get_edges()

vertexCount = g.get_size()

g2 = gv.Graph(format='svg')

for i in range(vertexCount):
    g2.node(str(i+1))

for i in range(len(graphEdges)):
    edge = graphEdges[i]
    if edge.is_spanning():
        g2.edge(str(edge.get_v()), str(edge.get_w()), label=str(edge.get_weight()), color="red")
    else:
        g2.edge(str(edge.get_v()), str(edge.get_w()), label=str(edge.get_weight()))

g2.render('img/g4')




