# time: O(n), unstable sort
# space: O(n + k), where k is the number of buckets
# some constraints: all elements should be within a finite range
# every value within the range is allocated a frequency bucket and elements are put into them

class BucketSort:
    def bucket_sort(arr):
        counts = [0, 0, 0] # if the array contains only 0, 1, 2
        for n in arr:
            counts[n] += 1
        
        i = 0
        for n in range(len(counts)):
            for j in range(counts[n]):
                arr[i] = n
                i += 1
        
        return arr 