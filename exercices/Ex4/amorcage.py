def parse_input():
    nums = list(map(int, input("Entrez les nombres (ex: 1 1 1 2 2 3) : ").split()))
    k = int(input("Entrez k (ex: 2) : "))
    return nums, k

def top_k_frequent(nums, k):
    # À implémenter
    pass

if __name__ == "__main__":
    nums, k = parse_input()
    result = top_k_frequent(nums, k)
    print("Éléments les plus fréquents :", result)
