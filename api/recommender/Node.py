
class Node:
    def __init__(self, x_min, y_min, x_max, y_max, points):
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max
        self.points = points
        self.childrens = []

    def get_points(self):
        return self.points

    def get_x_len(self):
        return abs(self.x_max) + abs(self.x_min)

    def get_y_len(self):
        return abs(self.y_max) + abs(self.y_min)

    def get_x_min(self):
        return self.x_min

    def get_y_min(self):
        return self.y_min

    def get_x_max(self):
        return self.x_max

    def get_y_max(self):
        return self.y_max

    def get_number_points(self):
        return len(self.points)

    def get_childrens(self):
        return self.childrens

    def remove_pt(self, pt):
        self.points.remove(pt)
