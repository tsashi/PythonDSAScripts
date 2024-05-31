class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        m = len(potions)
        potions.sort()

        res = []
        for i in spells:
            low = 0
            high = m-1
            if success <= i*potions[low]:
                res.append(high+1)
                continue
            elif success > i*potions[high]:
                res.append(low)
                continue
            while low<=high:
                mid = (low+high)//2
                if success <= i*potions[mid]:
                    high = mid-1
                    if success > i*potions[mid-1]:
                        res.append(m-mid)
                        break
                else:
                    low = mid+1
                    if success <= i*potions[mid+1]:
                        res.append(m-mid-1)
                        break
        return res