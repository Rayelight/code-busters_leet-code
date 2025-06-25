def merge(intervals):
    merged = []
    while intervals:
        current = intervals.pop(0)
        i = 0
        while i < len(intervals):
            if not (current[1] < intervals[i][0] or current[0] > intervals[i][1]):
                current = [min(current[0], intervals[i][0]), max(current[1], intervals[i][1])]
                intervals.pop(i)
            else:
                i += 1
        merged.append(current)
    return merged
