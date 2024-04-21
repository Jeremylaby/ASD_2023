from egz1btesty import runtests
from math import inf

def wideentall(T):
    def dfs(node, level):
        if node is None:
            return 0, 0, 0  # Liczba liści, szerokość, wysokość

        if node in dp:
            return dp[node]

        left_leaves, left_width, left_height = dfs(node.left, level + 1)
        right_leaves, right_width, right_height = dfs(node.right, level + 1)

        leaves = left_leaves + right_leaves

        # Oblicz szerokość i wysokość dla tego węzła
        width = left_width + right_width
        height = max(left_height, right_height) + 1

        # Jeśli liść, to zwracamy 1 liść, szerokość 1 i wysokość 0
        if node.left is None and node.right is None:
            result = 1, 1, 0
        else:
            result = leaves, width, height

        dp[node] = result
        return result

    dp = {}  # Pamięć podręczna dla efektywnego przetwarzania
    _, width, height = dfs(T, 0)
    
    # Sortowanie zgodnie z kolejnością kryteriów
    results = sorted([(width, -height, _), (width, height, _)])
    
    return results[0][2]  # Liczba krawędzi do usunięcia

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = False )