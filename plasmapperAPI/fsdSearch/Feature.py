class Feature:
    def __init__(self, name, start, stop, legend):
        self.name = name
        self.start = start
        self.stop = stop
        self.legend = legend

    def getName(self):
        return self.name

    def getStart(self):
        return self.start

    def getStop(self):
        return self.stop

    def getLegend(self):
        return self.legend

    def setName(self, name):
        self.name = name

    def setStart(self, start):
        self.start = start

    def setStop(self, stop):
        self.stop = stop

    def setLegend(self, legend):
        self.legend = legend

    # Override representation method
    def __repr__(self):
        return "(" + str(self.start) + "," + str(self.stop) + "," + self.legend + ")"

    # Override toString method
    def __str__(self):
        return self.__repr__

    # Override equals method
    def __eq__(self, featureToCompare):
        legend = featureToCompare.getLegend()
        name = featureToCompare.getName()
        start = featureToCompare.getStart()
        stop = featureToCompare.getStop()
        if (self.legend == legend) and (self.name == name) and (self.start == start) and (self.stop == stop):
            return True
        else:
            return False

# Sort the list of features by start position
# Algorithm from: http://rosettacode.org/wiki/Sorting_algorithms/Quicksort#Python
def quicksort(features):
    less, equal, greater = [], [], []
    if len(features) > 1:
        pivot = features[0]
        for f in features:
            fStart = f.getStart()
            pivotStart = pivot.getStart()
            if fStart < pivotStart:
                less.append(f)
            if fStart == pivotStart:
                equal.append(f)
            if fStart > pivotStart:
                greater.append(f)
        less = quicksort(less)
        greater = quicksort(greater)
        return less + equal + greater
    else:
        return features

# Testing script
"""if __name__ == '__main__':
    f = Feature("name", 7, 2, "legend")
    f1 = Feature("name", 1, 2, "legend")
    f2 = Feature("name2", 3, 2, "legend2")
    f3 = Feature("name3", 6, 2, "legend3")
    f4 = Feature("name3", 6, 2, "legend3")
    l = [f,f1,f2,f3]
    print(l)
    l = quicksort(l)
    print(l)
    print(f4 == f3)
    print(f == f1)"""