def dfs_with_stack(graph, start) :
    stack = [start] # Стек для хранения вершин 
    visited = set() # Множество для отслеживания посещённых вершин 
    result = [] # Список для записи порядка обхода
    while stack:
        node = stack-pop() # Достать вершину из стека
        if node not in visited:
            visited. add (node)
            result. append (node)
            # Добавить в стек соседей в обратном порядке для корректного обхода
            stack. extend
    return result