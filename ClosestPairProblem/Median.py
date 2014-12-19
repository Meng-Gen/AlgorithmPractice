class Median():
    def __init__(self):
        self.chunk_size = 5

    def get_by_sorting(self, elements):
        return self.__get_median_naive(elements)

    def get(self, elements):
        return self.select(elements, (len(elements) + 1) // 2)
        
    def select(self, unsorted_list, kth):
        n = len(unsorted_list)
        if n <= self.chunk_size:
            return self.__get_kth_smallest_elements_naive(unsorted_list, kth)
        
        # split into chunks of five elements
        chunks = self.__split_chunks(unsorted_list, self.chunk_size)
        
        # get medians of every group
        medians = [self.__get_median_naive(chunk) for chunk in chunks]

        # median of medians
        median_of_medians = self.select(medians, (len(medians) + 1) // 2)

        # partition
        smaller_list, larger_list = self.__partition(unsorted_list, median_of_medians)

        median_pos = len(smaller_list)
        if kth - 1 < median_pos:
            return self.select(smaller_list, kth)
        elif kth - 1 == median_pos:
            return median_of_medians
        elif kth - 1 > median_pos:
            return self.select(larger_list, kth - median_pos - 1)

    def __get_kth_smallest_elements_naive(self, unsorted_list, kth):
        return sorted(unsorted_list)[kth - 1]

    def __split_chunks(self, element_list, chunk_size):
        return [element_list[i:i + chunk_size] for i in range(0, len(element_list), chunk_size)]

    def __get_median_naive(self, unsorted_list):
        n = len(unsorted_list)
        median_pos = (n + 1) // 2
        return self.__get_kth_smallest_elements_naive(unsorted_list, median_pos)

    def __partition(self, unsorted_list, pivot):
        smaller_list = []
        larger_list = []
        for value in unsorted_list:
            if value < pivot:
                smaller_list.append(value)
            elif value > pivot:
                larger_list.append(value)
        return smaller_list, larger_list

