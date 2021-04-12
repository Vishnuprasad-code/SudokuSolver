from tkinter import *
import sudoku,time

new_sudoku = sudoku.Sudoku_board(9, 9)

cell_width = 9
def create_board_window():
    mm=hr=sec=0

    for cells in range(81):
        row = cells // 9
        col = cells % 9

        if (row < 3 or row > 5) and (col < 3 or col > 5):
            color = 'white'
        elif (row >= 3 and row < 6) and (col >= 3 and col < 6):
            color = 'white'
        else:
            color = 'dark goldenrod'

        board[row][col].delete(0, END)
        board[row][col].insert(END,(int(new_sudoku.board[row,col]) if new_sudoku.board[row,col]>0 else ""))
        if new_sudoku.board[row, col] > 0:
            board[row][col].configure(state=DISABLED,disabledbackground=color,disabledforeground='gray1')
        board[row][col].configure(bg=color,fg='gray1')

def reset_puzzle_window():
    for cells in range(81):
        row = cells // 9
        col = cells % 9
        board[row][col].configure(state=NORMAL)
        board[row][col].delete(0, END)
def upload_puzzle_window():
    for cells in range(81):
        row = cells // 9
        col = cells % 9
        new_sudoku.board[row][col]=int(board[row][col].get()) if board[row][col].get()!="" else 0
    print("hello")
    print(new_sudoku.board)


def solve_puzzle_window():
    new_sudoku.solution()
    create_board_window()

def callback(input):
    if input=="":
        return True
    else:
        try:
            num=int(input)
        except:
            return False
        if num < 10 and num > 0 :
            return True
    return False
window = Tk()
print(window.geometry('460x500'))

board = nums = []

for row in range(9):
    board += [["", "", "", "", "", "", "", "", ""]]

font = ('Arial', 20)

for cells in range(81):
    row=cells // 9
    col=cells % 9

    if (row < 3 or row > 5) and (col < 3 or col > 5):
        color = 'white'
    elif (row >= 3 and row < 6) and (col >= 3 and col < 6):
        color = 'white'
    else:
        color = 'dark goldenrod'

    board[row][col] = Entry(window, width=3, borderwidth=2,
                            bg=color,font=font, justify=CENTER)
    board[row][col].grid(row=row, column=col, ipady=1)
    reg = window.register(callback)
    board[row][col].config(validate="key", validatecommand=(reg, '%P'))

b1=Button(window,text="Create Puzzle",command=create_board_window)
b1.grid(row=10,column=0,columnspan=2,padx=0,pady=3,ipadx=8)

b2=Button(window,text="Solve Puzzle",command=solve_puzzle_window)
b2.grid(row=11,column=0,columnspan=2,padx=0,pady=3,ipadx=8)

b3=Button(window,text="Upload",command=upload_puzzle_window)
b3.grid(row=10,column=4,columnspan=2,padx=0,pady=3,ipadx=8)

b4=Button(window,text="Reset",command=reset_puzzle_window)
b4.grid(row=11,column=4,columnspan=2,padx=0,pady=3,ipadx=8)
window.mainloop()