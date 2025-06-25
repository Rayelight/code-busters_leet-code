def parse_input():
    nums = list(map(int, input("Entrez les nombres (ex: 2 7 11 15) : ").split()))
    target = int(input("Entrez la cible (ex: 9) : "))
    return nums, target

def two_sum(nums, target):
    # À implémenter
    pass

if __name__ == "__main__":
    nums, target = parse_input()
    result = two_sum(nums, target)
    print("Indices:", result)
