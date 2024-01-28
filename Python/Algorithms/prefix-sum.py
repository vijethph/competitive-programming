class PrefixSum:
    def __init__(self, array: list[int]) -> None:
        len_array = len(array)
        self.prefix_sum = [0] * len_array

        if len_array > 0:
            self.prefix_sum[0] = array[0]

        for i in range(1, len_array):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + array[i]

    def get_sum(self, start: int, end: int) -> int:
        if start == 0:
            return self.prefix_sum[end]

        return self.prefix_sum[end] - self.prefix_sum[start - 1]

    def contains_sum(self, target_sum: int) -> bool:
        sums = {0}
        for sum_item in self.prefix_sum:
            if sum_item - target_sum in sums:
                return True

            sums.add(sum_item)
        return False

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    prefix_sum = PrefixSum(array)
    print(prefix_sum.get_sum(0, 4))
    print(prefix_sum.get_sum(1, 3))