"""
Out of a set of points, find the two points that are closest together.

Connecting two points effectively turns them into one. 
- Either corrdinate can be used for the connection. 

We want to find the size of the three largest circuits multiplied together.


How to find every combination of values in a list
[1, 2, 3, 4, 5]

Use a nested for loop to iterate through all combinations of points in the list and store those distances.

sort the distances from smallest to largest. 

Pop the next smallest distance. See if either of the points that form that distance are
already in one of the sets that represent the circuit. 
    - If so add those points to that circuit. 
    - Otherwise those points now form their own circuits. 

Do this for 1000 iterations.
sort the list of sets to find the three largest and multiply to find the answer. 



""" 


import math


type Point = tuple[int, ...]

class UnionFind:
    def __init__(self, points: list[Point]):
        """Since I'm using this to track sets of points, the key in the dictionary
        is the point, and the value at the dictionary is the representative point for that point."""
        self.parent: dict[Point, Point] = {point: point for point in points}
        self.size: dict[Point, int] = {point: 1 for point in points}
        self.num_components = len(points)

    def find(self, x: Point) -> Point:
        """Returns the representative point (aka the root of the tree representing
        the set) for the given point. """
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, p1: Point, p2: Point) -> bool:
        """Merge the sets containing ``p1`` and ``p2``. 
        If they belong to the same set return true. Otherwise, 
        merge and return false. 
        """
        root_1 = self.find(p1)
        root_2 = self.find(p2)

        if root_1 == root_2:
            return True
        
        # make the root of the smaller tree
        # point to the root of the larger tree.
        # unioning the smaller tree under the larger
        # tree minimizes the numbe of nodes that get
        # "pushed deeper" down the tree. That's why this
        # optimization works. See: https://chatgpt.com/share/69e2521a-0f3c-83e8-8b42-d5c2e4b39d35
        # for an explanation
        if self.size[root_1] > self.size[root_2]:
            root_1, root_2 = root_2, root_1

        self.parent[root_1] = root_2
        self.num_components -= 1
        self.size[root_2] += self.size[root_1]
        return False
    
    def num_items(self, p: Point) -> int:
        """Return the number of items in this point's set.
        Only the root (representative point) will have an accurate size. Since we don't
        update the sizes of all the points in the ``union`` function. 
        """
        root = self.find(p)
        return self.size[root]


class Distance:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1 = p1
        self.p2 = p2
        self.distance = math.dist(p1, p2)

def day_08() -> None:
    points: list[Point] = []
    with open("./day08.txt") as f:
        for line in f:
            point: Point = tuple([int(val) for val in line.strip().split(",")])
            points.append(point)
        
    uf = UnionFind(points=points)

    distances: list[Distance] = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distances.append(Distance(points[i], points[j]))
    
    distances.sort(key=lambda d: d.distance)

    for i in range(1000):
        closest = distances[i]
        uf.union(closest.p1, closest.p2)

    circuit_lengths = sorted(uf.size.values(), reverse=True)

    print(circuit_lengths[0] * circuit_lengths[1] * circuit_lengths[2])

    # part 2
    uf = UnionFind(points=points)
    last_p1, last_p2 = 0, 0
    for dist in distances:
        if not uf.union(dist.p1, dist.p2):
            last_p1, last_p2 = dist.p1[0], dist.p2[0]

    if not last_p1 or not last_p2:
        raise RuntimeError("These values should not be zero")
    
    print(last_p1 * last_p2)

day_08()