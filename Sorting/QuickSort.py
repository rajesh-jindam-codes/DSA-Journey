class Solution:
    # Function to sort a list using quick sort algorithm.
    def quickSort(self, arr, low, high):
        if low < high:
            # Partition the array and get the pivot index
            p_index = self.partition(arr, low, high)
            # Recursively sort elements before and after partition
            self.quickSort(arr, low, p_index - 1)
            self.quickSort(arr, p_index + 1, high)
        return arr

    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low
        j = high

        while i < j:
            while i <= high - 1 and arr[i] <= pivot:
                i += 1
            while j >= low + 1 and arr[j] > pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[low], arr[j] = arr[j], arr[low]
        return j
nums=[6,3,54,9,5,6,2,65,54]
obj=Solution()
print(obj.quickSort(nums,0,len(nums)-1))