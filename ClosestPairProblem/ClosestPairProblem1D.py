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
    def get(self, max_size=1000):
        generator = LaggedFibonacciGenerator()
        return list(set(generator.generate(max_size)))

class Problem():
    def __init__(self):
        self.INFINITY = 10**100

    def solve(self):
        dataset = Dataset()
        points = dataset.get()
        print("sorting =>", self.get_by_sorting(points))
        print("divide_and_conquer =>", self.get(points))

    def get_by_sorting(self, points):
        # cannot generalize to higher dimensions
        sorted_points = sorted(points)
        min_delta_so_far = abs(sorted_points[0] - sorted_points[1])
        for i in range(1, len(sorted_points) - 1):
            delta = abs(sorted_points[i] - sorted_points[i + 1])
            if delta < min_delta_so_far:
                min_delta_so_far = delta
        return min_delta_so_far

    def get(self, points):
        n = len(points)
        if n <= 1:
            return self.INFINITY
        elif n == 2:
            return abs(points[0] - points[1])

        pivot = Median.Median().get(points)
        halves = self.__partition(points, pivot)
        delta = min(self.get(halves[0]), self.get(halves[1]))
        delta_between_halves = self.get(self.__get_points_near_cut(points, pivot, delta))
        return min(delta, delta_between_halves)

    def __partition(self, points, pivot):
        partition = [], []
        for point in points:
            if point < pivot:
                partition[0].append(point)
            else:
                partition[1].append(point)
        return partition

    def __get_points_near_cut(self, points, cut, cut_width):
        return [point for point in points if abs(point - cut) < cut_width]

def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
