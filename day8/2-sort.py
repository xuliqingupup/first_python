import random


class Sort():
    def __init__(self, n):
        self.n = n
        # self.arr = [3, 87, 2, 93, 78, 56, 61, 38, 12, 40]
        self.arr = [0] * n
        for i in range(self.n):
            # self.arr.append(random.randint(0, 99))
            self.arr[i] = random.randint(0, 99)

    # def __str__(self):
    #     print("我是小猫")
    #     return str(self.arr)

    def partition(self, left, right):
        arr = self.arr
        pivot = arr[left]
        while left < right:
            while left < right and self.arr[right] >= pivot:
                right -= 1
            arr[left], arr[right] = arr[right], arr[left]
            while left < right and self.arr[left] <= pivot:
                left += 1
            arr[left], arr[right] = arr[right], arr[left]
        arr[left] = pivot
        return left

    def quick_sort(self, left, right):
        """
        快排
        :param left:
        :param right:
        :return:
        """
        if left < right:
            mid = self.partition(left, right)
            self.quick_sort(left, mid - 1)
            self.quick_sort(mid + 1, right)

    def adjust_heap_max(self, pos, length):
        arr = self.arr
        dad = pos
        son = dad * 2 + 1
        while son < length:
            if son + 1 < length:
                if arr[son + 1] > arr[son]:
                    son = son + 1
            if arr[dad] < arr[son]:
                arr[dad], arr[son] = arr[son], arr[dad]
                dad = son
                son = son * 2 + 1
            else:
                break

    def heap_sort(self):
        """
        大根堆
        :param n:
        :return:
        """
        arr = self.arr
        for i in range((self.n - 1) // 2, -1, -1):
            self.adjust_heap_max(i, self.n)
        for i in range(self.n, 1, -1):
            arr[0], arr[i - 1] = arr[i - 1], arr[0]
            self.adjust_heap_max(0, i - 1)


if __name__ == '__main__':
    mysort = Sort(10)
    print(mysort)
    # print(mysort.arr)
    # mysort.quick_sort(0, len(mysort.arr) - 1)
    # print(mysort.arr)
    mysort.heap_sort()
    print(mysort.arr)
