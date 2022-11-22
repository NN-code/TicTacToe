from tkinter import *
import tkinter.messagebox as mb

check = True
board = [-1, -1, -1,
         -1, -1, -1,
         -1, -1, -1]

def printVisualBoard():
    tab = 0
    for i in board:
        if tab == 3:
            print()
            tab = 0
        print(board[i], end='')
        tab += 1

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initButtons()
        self.initUI()

    def initUI(self):
        self.parent.title("TicTacToe")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

    def initButtons(self):
        btn1 = Button(self, name='0', text='', height=8, width=16, bd=1, relief=SUNKEN, command=lambda: self.turn(btn1))
        btn1.grid(column=1, row=0)
        btn2 = Button(self, name='1', text='', height=8, width=16, bd=1, relief=SUNKEN, command=lambda: self.turn(btn2))
        btn2.grid(column=2, row=0)
        btn3 = Button(self, name='2', text='', height=8, width=16, bd=1, relief=SUNKEN, command=lambda: self.turn(btn3))
        btn3.grid(column=3, row=0)
        btn4 = Button(self, name='3', text='', height=8, width=16, bd=1, relief=SUNKEN, command=lambda: self.turn(btn4))
        btn4.grid(column=1, row=1)
        btn5 = Button(self, name='4', text='', height=8, width=16, bd=1, relief=SUNKEN, command=lambda: self.turn(btn5))
        btn5.grid(column=2, row=1)
        btn6 = Button(self, name='5', text='', height=8, width=16, bd=1, relief=SUNKEN, command=lambda: self.turn(btn6))
        btn6.grid(column=3, row=1)
        btn7 = Button(self, name='6', text='', height=8, width=16, bd=1, relief=SUNKEN, command=lambda: self.turn(btn7))
        btn7.grid(column=1, row=2)
        btn8 = Button(self, name='7', text='', height=8, width=16, bd=1, relief=SUNKEN, command=lambda: self.turn(btn8))
        btn8.grid(column=2, row=2)
        btn9 = Button(self, name='8', text='', height=8, width=16, bd=1, relief=SUNKEN, command=lambda: self.turn(btn9))
        btn9.grid(column=3, row=2)

    def centerWindow(self):
        w = 359
        h = 387

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def turn(self, button):
        global check, board
        if button.cget('text') == '':
            if check:
                button.configure(text="X")
                board[int(button.winfo_name())] = 1
                self.fullCheck(1)
            else:
                button.configure(text="O")
                board[int(button.winfo_name())] = 0
                self.fullCheck(0)
        check = not check

    def horizontalCheck(self, sign):
        multiply = streak = 0
        for i in range(3):
            streak = 0
            for j in range(0+multiply, 3+multiply, 1):
                if j == 2+multiply:
                    multiply += 3
                if board[j] == sign:
                    streak += 1
                if streak == 3:
                    return 1

    def verticalCheck(self, sign):
        streak = 0
        for i in range(3):
            streak = 0
            for j in range(i, 7+i, 3):
                if board[j] == sign:
                    streak += 1
                if streak == 3:
                    return 1

    def diagonalCheck(self, sign):
        if (board[0] == sign and board[4] == sign and board[8] == sign) or \
           (board[6] == sign and board[4] == sign and board[2] == sign):
            return 1

    def drawCheck(self):
        if not -1 in board:
            return 1

    def fullCheck(self, sign):
        correct_sign = ''
        if sign == 1:
            correct_sign = 'X'
        else:
            correct_sign = 'O'
        if self.drawCheck() == 1:
            self.drawMessage()
        elif (self.verticalCheck(sign) == 1 or
            self.horizontalCheck(sign) == 1 or
            self.diagonalCheck(sign) == 1):
            self.winnerMessage(correct_sign)

    def winnerMessage(self, sign):
        msg = "Победили - " + sign
        mb.showinfo("Победа!", msg)
        self.resetGame()

    def drawMessage(self):
        msg = "Ничья"
        mb.showinfo("Ничья!", msg)
        self.resetGame()

    def resetGame(self):
        global board
        self.initButtons()
        for i, num in enumerate(board):
            board[i] = -1

def main():
    root = Tk()
    root.resizable(width=False, height=False)
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()