from collections import Counter

def top_k_frequent(nums, k):
    count = Counter(nums)
    return [item for item, _ in sorted(count.items(), key=lambda x: -x[1])[:k]]
