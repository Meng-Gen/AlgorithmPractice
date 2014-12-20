import itertools
import math
import Median
import sys

class LaggedFibonacciGenerator():
    def generate(self, length):
        s = [None]
        for k in range(1, 55 + 1):
            s.append((100003 - 200003 * (k+1) + 300007 * (k+1)**3) % 1000000)
        for k in range(56, length + 1):
            s.append((s[k - 24] + s[k - 55]) % 1000000)
        return s[1:length + 1]

class Dataset():
    def get(self, max_size=2000):
        random_numbers = LaggedFibonacciGenerator().generate(2 * max_size)
        return [(random_numbers[i], random_numbers[i + 1]) for i in range(0, len(random_numbers), 2)]

class Problem():
    def __init__(self):
        self.INFINITY = 10**100

    def solve(self):
        points = Dataset().get()
        print("brute_force =>", self.get_by_brute_force(points))
        print("divide_and_conquer =>", self.get(points))

    def get_by_brute_force(self, points):
        n = len(points)
        min_delta2_so_far = self.INFINITY
        for i, j in itertools.combinations(range(n), 2):
            delta2 = self.__get_distance2(points[i], points[j])
            if delta2 < min_delta2_so_far:
                min_delta2_so_far = delta2
        return min_delta2_so_far

    def get(self, points):
        n = len(points)
        if n <= 1:
            return self.INFINITY
        elif n == 2:
            return self.__get_distance2(points[0], points[1])

        pivot = Median.Median().get(points)
        halves = self.__partition(points, pivot)
        delta2 = min(self.get(halves[0]), self.get(halves[1]))
        delta2_between_halves = self.__get_delta_between_halves(pivot[1], halves, delta2)
        return min(delta2, delta2_between_halves)

    def __get_distance2(self, one_point, another_point):
        dim = len(one_point)
        return sum([(one_point[i] - another_point[i])**2 for i in range(dim)])

    def __partition(self, points, pivot):
        partition = [], []
        for point in points:
            if point < pivot:
                partition[0].append(point)
            else:
                partition[1].append(point)
        return partition

    def __get_delta_between_halves(self, cut_y, halves, cut_width2):
        left_points = [point for point in halves[0] if abs(point[1] - cut_y) < cut_width2]
        right_points = [point for point in halves[1] if abs(point[1] - cut_y) < cut_width2]
        sorted_left_points = self.__sort_by_y(left_points)
        sorted_right_points = self.__sort_by_y(right_points)

        # merge and find closest pair between two lists
        left_point_count, right_point_count = len(sorted_left_points), len(sorted_right_points)
        if left_point_count == 0 or right_point_count == 0:
            return self.INFINITY

        min_delta2_so_far = self.INFINITY
        left_pos, right_pos = 0, 0
        while left_pos < left_point_count and right_pos < right_point_count:
            left_point = sorted_left_points[left_pos]
            right_point = sorted_right_points[right_pos]
            delta2 = self.__get_distance2(left_point, right_point)
            if delta2 < min_delta2_so_far:
                min_delta2_so_far = delta2
            if left_point[1] < right_point[1]:
                left_pos += 1
            else:
                right_pos += 1
        return min_delta2_so_far

    def __sort_by_y(self, points):
        return sorted(points, key=lambda point:point[1])

def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
