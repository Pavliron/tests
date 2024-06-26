def find_path(n, m):
    array = list(range(1, n+1))
    path = []
    current_index = 0
    while True:
        path.append(array[current_index])
        if len(path) > 1 and path[0] == path[-1]:
            break
        current_index = (current_index + m - 1) % n
    return path[:-1]  

n = int(input("Введите n: "))
m = int(input("Введите m: "))
path = find_path(n, m)
print("Путь:", path)