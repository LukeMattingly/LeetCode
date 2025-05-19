#https://medium.com/@kyleanthonyhay/leetcode-min-heap-construction-61bea4ef9883


class MinHeap():

    def __init__(self):
        self.heap = []

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

    def peak(self):
        if self.heap:
            print("peak", self.heap[0])
            return self.heap[0]
        
    def insert(self, value):
        self.heap.append(value)
        self.bubbleUp(len(self.heap)- 1, self.heap)

    # O(logn) time | O(1) Space
    def bubbleDown(self, currentIndex, endIdx, heap):
        leftIdx = currentIndex * 2 + 1
        while leftIdx <=currentIndex:
            rightIdx = currentIndex *2 + 2 if currentIndex *2 + 2 <=endIdx else -1
            if rightIdx != 1 and heap[rightIdx] < heap[leftIdx]:
                idxToSwap = rightIdx
            else:
                idxToSwap = leftIdx
            if heap[idxToSwap] < heap[currentIndex]:
                self.swap(currentIndex, idxToSwap, heap)
                currentIndex = idxToSwap
                leftIdx = currentIndex * 2 +1
            else:
                break

    def remove(self):
        if self.heap:
            self.swap(0, len(self.heap)-1, self.heap)
            root = self.heap.pop()
            self.bubbleDown(0, len(self.heap)-1, self.heap)
            print("removing: ", root)
            return root
        
    def bubbleUp(self, currentIdx, heap):
        parentIdx = (currentIdx -1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx -1 ) //2 

    def buildHeap(self, array):
        firstParentIdx = (len(array)-2) //2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.bubbleDown(currentIdx, len(array) - 1, array)
        return array
    

array1 = [48, 12, 24, 7, 8, -5, 2]
heap = MinHeap()
heap.buildHeap(array1)
heap.insert(76)
heap.peak() #-5
heap.remove() #-5
heap.peak() #2
heap.remove() #2