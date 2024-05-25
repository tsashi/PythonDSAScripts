class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        arr = []
        heapsize = 0

        def MinHeapify(i: int):
            nonlocal heapsize, arr
            l = (2*i+1)
            r = (2*i+2)
            min = i
            if l < heapsize and arr[l] < arr[i]:
                min = l
            if r < heapsize and arr[r] < arr[min]:
                min = r
            if min != i:
                arr[i], arr[min] = arr[min], arr[i]
                MinHeapify(min)

        def createminheap(num):
            nonlocal heapsize, arr
            arr.append(num)
            heapsize += 1
            i = heapsize-1

            while i!=0 and arr[(i-1)//2]>arr[i]:
                arr[i], arr[(i-1)//2] = arr[(i-1)//2], arr[i]
                i = (i-1)//2

        def removemin()->int:
            nonlocal heapsize, arr
            if heapsize <=0:
                return None
            if heapsize == 1:
                heapsize -= 1
                return arr.pop()

            temp = arr[0]
            arr[0] = arr.pop()
            heapsize -= 1
            MinHeapify(0)
            return temp

        for i in range(k):
            createminheap(nums[i])
        
        for i in range(k, len(nums),1):
            if nums[i] > arr[0]:
                removemin()
                createminheap(nums[i])
        
        return arr[0]
    
myobj = Solution()
nums = [-1,2,0]
print(myobj.findKthLargest(nums,1))

#use heapq methods
