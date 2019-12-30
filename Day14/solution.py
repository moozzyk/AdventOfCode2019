import math
import sys


def create_requirement_graph(lines):
    graph = dict()
    edges = dict()
    for l in lines:
        (ingredients, product) = l.split(" => ")
        (q, n) = product.split(" ")
        for i in ingredients.split(", "):
            (quantity, name) = i.split(" ")
            if name not in graph:
                graph[name] = []
            graph[name].append(n)
            edges[(name, n)] = (int(quantity), int(q))

    return (graph, edges)


def traverse(node, graph, edges):
    if node == 'FUEL':
        return 1

    required_total = 0
    for n in graph[node]:
        required = traverse(n, graph, edges)
        prod = edges[(node, n)]
        required_total += math.ceil(required / prod[1]) * prod[0]
    return required_total


def problem1(graph, edges):
    print(traverse("ORE", graph, edges))


with open(sys.argv[1], "r") as f:
    (graph, edges) = create_requirement_graph(f.read().splitlines())
    problem1(graph, edges)
