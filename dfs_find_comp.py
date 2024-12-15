def dfs(graph, node, visited, component):
    visited.add(node)
    component.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, component)

def find_connected_components(graph):
    visited = set()
    components = []

    for node in graph:
        if node not in visited:
            component = []
            dfs(graph, node, visited, component)
            components.append(component)
    
    return components


graph = {

}


components = find_connected_components(graph)
print("Компоненты связности:")
for i, component in enumerate(components, start=1):
    print(f"Компонента {i}: {component}")
