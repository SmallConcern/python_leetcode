

class MedianSortedArrayFinder(object):
    @staticmethod
    def find_median(arr1, arr2):
        new_arr = list()
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                new_arr.append(arr1[i])
                i += 1
            else:
                new_arr.append(arr2[j])
                j += 1
            if  i + j > (len(arr1) + len(arr2) - 2):
                early_exit = True
        new_arr += arr1[i:] + arr2[j:]
        if len(new_arr)% 2 == 0:
            return (float(new_arr[len(new_arr)/2]) + new_arr[len(new_arr)/2-1])/2
        else:
            return float(new_arr[len(new_arr)/2])


class Solution(object):
    @staticmethod
    def findMedianSortedArrays(nums1, nums2):
        return MedianSortedArrayFinder.find_median(nums1, nums2)