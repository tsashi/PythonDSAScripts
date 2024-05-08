import numpy as np
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        curx = A[0]
        cury = B[0]
        totaldistance = 0
        numpoints = len(A)
        if numpoints<=1:
            return totaldistance
        
        for i in range(1, numpoints):
            nextx = A[i]
            nexty = B[i]
            
            distx = abs(curx-nextx)
            disty = abs(cury-nexty)
            dist = min(distx,disty)+abs(distx-disty)
            totaldistance += dist
            curx = A[i]
            cury = B[i]
        return totaldistance
            