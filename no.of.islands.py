class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid  #setting the grid globally
        self.m = len(grid)  #calculating the n o.of.rows
        self.n = len(grid[0]) #calculating the no.of.columns
        self.count = 0  #setting counter to 0
        self.dirs = [[0,1],[1,0],[-1,0],[0,-1]]  #directions array
        
        for i in range(self.m):  #traversing through the entire grid tocheck the no.of.islands
            for j in range(self.n):  
                if grid[i][j] =='1':  #if the grid is equal to 1 we are callimng the dfs function
                    self.dfs(i,j)  #passing the index of the grid in the dfs function
                    self.count+=1  #calculating the no.of.islands
                    
        return self.count  #retuning the count of islands
    
    def dfs(self,i,j):
        if self.grid[i][j] == "0":  #if the grid is 0 then function will unfold
            return
        
    
        self.grid[i][j]="0"  #changing the grid to 0 
        
        for x,y in self.dirs:  #itertaing through the grid using direction array
            nr = x+i  #row
            nc = y+j #column
            
            if nr>=0 and nr<self.m and nc>=0 and nc<self.n: #boundary check
                self.dfs(nr,nc)  #recurrsion function