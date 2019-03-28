class Point(object):
    def __init__(self, point_x, point_y):
        self.point_x = point_x
        self.point_y = point_y

    def __eq__(self, another_point):
        return (self.point_y == another_point.point_y) & (self.point_x == another_point.point_x)

    def __repr__(self):
        return "Point Class"

    def __str__(self):
        dummy = "This point is located at X: " + str(self.point_x) + " and Y: " + str(self.point_y)
        return dummy


class Graph(object):
    def __init__(self, graph_height, graph_width):
        self.point_array = set()
        self.graph_height = graph_height
        self.graph_width = graph_width

    def __contains__(self, point):
        if self.point_array:
            for existingPoint in self.point_array:
                if point == existingPoint:
                    return True
        return False


if __name__ == "__main__":
    # Testing Functions, you should run on main.py
    firstPoint = Point(10, 15)
    print(firstPoint)
    secondPoint = Point(10, 15)
    print(secondPoint)
    print(firstPoint == secondPoint)

    newGraph = Graph(10, 10)
    print(firstPoint in newGraph)
