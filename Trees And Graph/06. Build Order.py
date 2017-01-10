projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [['a','d'], ['f','b'], ['b','d'], ['f','a'], ['d','c']]


def build_order(projects, dependencies):
    graph = {}
    for i in projects:
        graph[i] = {'dependent_for':[], 'depends_on':[]}
    for i,j in dependencies:
        graph[j]['depends_on'].append(i)
        graph[i]['dependent_for'].append(j)
    print(graph)
    not_end = True
    res = []
    while len(graph) > 0:
        rem_list = []
        for i in graph.keys():
            if len(graph[i]['depends_on']) == 0:
                for j in graph[i]['dependent_for']:
                    graph[j]['depends_on'].remove(i)
                res.append(i)
        for i in res:
            if i in graph:
                graph.pop(i)
    return res

print(build_order(projects, dependencies))
