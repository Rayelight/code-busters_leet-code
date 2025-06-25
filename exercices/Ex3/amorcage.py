def parse_input():
    n = int(input("Nombre d'intervalles : "))
    intervals = []
    for _ in range(n):
        start, end = map(int, input("Intervalle (ex: 1 3) : ").split())
        intervals.append([start, end])
    return intervals

def merge(intervals):
    # À implémenter
    pass

if __name__ == "__main__":
    intervals = parse_input()
    result = merge(intervals)
    print("Résultat fusionné :", result)
