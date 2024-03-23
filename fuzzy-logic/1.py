class FuzzySet:
    def __init__(self, values):
        self.values = values

    def union(self, other_set):
        result = []
        for i in range(len(self.values)):
            result.append(max(self.values[i], other_set.values[i]))
        return FuzzySet(result)

    def intersection(self, other_set):
        result = []
        for i in range(len(self.values)):
            result.append(min(self.values[i], other_set.values[i]))
        return FuzzySet(result)

    def difference(self, other_set):
        result = []
        for i in range(len(self.values)):
            result.append(max(self.values[i] - other_set.values[i], 0))
        return FuzzySet(result)

    def complement(self):
        result = []
        for i in range(len(self.values)):
            result.append(1 - self.values[i])
        return FuzzySet(result)


# Example usage
set1 = FuzzySet([0.2, 0.4, 0.6, 0.8])
set2 = FuzzySet([0.3, 0.5, 0.7, 0.9])

union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
complement_set = set1.complement()

print("Union:", union_set.values)
print("Intersection:", intersection_set.values)
print("Difference:", difference_set.values)
print("Complement:", complement_set.values)
