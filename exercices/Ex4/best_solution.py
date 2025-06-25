from collections import Counter
import heapq

def top_k_frequent(nums, k):
    count = Counter(nums)
    return [item for item, _ in heapq.nlargest(k, count.items(), key=lambda x: x[1])]
