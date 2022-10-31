class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        
        self.dirs = [[0,1],[-1,0],[1,0],[0,-1]]  #direction to fill the paint
        self.color_tbc = image[sr][sc]  #storing the index of the pile to paint
        self.fillwith = color  #storing the color in a variable
        self.image = image  #setting the image as global
        self.m = len(image)  #len of the matrix for row
        self.n = len(image[0])  #len of the matrix for column
        
        
        if self.color_tbc ==color:  #if the pile colour is same as the to be change colur then we dont need to change anything
            return image
        
        self.dfs(sr,sc)  #calling the dfs recurrsion
        
        return self.image  #returning the given image after changing the color
    
    
    def dfs(self,sr,sc): #getting the parameter sr,sc
        self.image[sr][sc] =self.fillwith  #changing the pile colopur with the colour that need to change
        
        for x,y in self.dirs:  #looping through the direction of the pile
            nr = x+sr  #getting the row
            nc = y+sc  #getting the column
            if nr>=0 and nr<self.m and nc>=0 and nc<self.n and self.image[nr][nc] == self.color_tbc:  #boundary check
                self.dfs(nr,nc)  #calling the recurrsion function again
                
        return#function unfolding