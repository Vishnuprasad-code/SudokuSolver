import pandas as pd
import numpy as np
import time,random
class Sudoku_board():
    def __init__(self,rows,cols):
        self.rows=rows
        self.cols=cols   
        self.board=np.zeros((self.rows,self.cols))
        self.create_board()

    def create_board(self,blanks=57):
        count=0
        while count<10:
            xy=self.check_empty()
            s,e=random.randint(1,4),random.randint(6,9)
            num=random.randint(s,e)
            if self.check_possible(num,xy):
                self.board[xy]=num
            xy=self.check_empty()
            count+=1
        self.solution()
        while blanks:
            self.board[random.randint(0,8),random.randint(0,8)]=0
            blanks-=1

            

    def print_board(self):
        print(self.board)

    def check_empty(self):

        if len(np.where(self.board==0)[0])==0 and len(np.where(self.board==0)[1])==0:
            return None
        return np.where(self.board==0)[0][0], np.where(self.board==0)[1][0]

    def check_possible(self,num ,xy):   
        
        if num in self.board[xy[0],:] :
        # and self.board[xy[0],:][xy[1]] != num:
            return False
        if num in self.board[:,xy[1]] :
            # and self.board[:,xy[1]][xy[0]] != num:
            return False
        row=xy[0]//3
        col=xy[1]//3
        if num in self.board[row*3:row*3+3,col*3:col*3+3]:
            #  and self.board[row*3:row*3+3,col*3:col*3+3][xy[0]%3,xy[1]%3] != num:
            return False
        return True

    def solution(self):
        xy=self.check_empty()
        if xy==None:
            return True    
        for num in range(1,10):
            if self.check_possible(num, xy):
                self.board[xy[0],xy[1]] = num

                if self.solution():
                    return True
                
                self.board[xy[0],xy[1]] = 0 
                
        return False
            
# s=Sudoku_board(9,9)
# s.board=np.asarray([[7, 8, 0, 4, 0, 9, 0, 2, 0],
#  [6, 0, 2, 0, 0, 5, 0, 4, 9],
#  [4, 0, 3, 6, 2, 1, 0, 0, 0],
#  [5, 5, 7, 0, 0, 3, 2, 0, 1],
#  [2, 0, 1, 7, 0, 8, 0, 3, 4],
#  [9, 3, 4, 0, 6, 2, 7, 0, 5],
#  [5, 0, 0, 3, 0, 4, 0, 1, 2],
#  [0, 2, 6, 0, 8, 0, 4, 0, 3],
#  [0, 4, 9, 0, 1, 0, 8, 0, 0]])


# start = time.time()
s=Sudoku_board(9,9)
# s.create_board()
print(s.board,"\n\n")
# s.solution()
# print(s.board,"\n\n")
# end = time.time()
# print(end-start)



