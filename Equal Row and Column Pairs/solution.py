class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count=0
        rowHash={}
        for i in grid:
            x=','.join(str(i))
            if x in rowHash:
                rowHash[x]+=1
            else:
                rowHash[x]=1
        l=len(grid)
        for i in range(l):
            x=[]
            for j in range(l):
                x.append(grid[j][i])
            x=','.join(str(x))
            if x in rowHash:
                count+=rowHash[x]

        return count