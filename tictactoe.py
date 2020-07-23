
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe ")
root.geometry("360x210")
root.configure(background="grey")
root.iconbitmap("C:/Users/Golu/PycharmProjects/tkinter/images/tic-tac-toe.ico")

lbl1 = Label(root, text="Tic Tac Toe Game", bg="grey", fg="white", font=('Helvetica', '15'))
lbl1.grid(row=0, column=0)
lbl2 = Label(root, text="Player 1: X", bg="grey", fg="white", font=('Helvetica', '10'))
lbl2.grid(row=1, column=0)
lbl3 = Label(root, text="Player 2: O", bg="grey", fg="white", font=('Helvetica', '10'))
lbl3.grid(row=2, column=0)

turn = 1


def click1():
    global turn
    if btn1["text"] == " ":
        if turn == 1:
            turn = 2
            btn1["text"] = "X"
        elif turn == 2:
            turn = 1
            btn1["text"] = "O"
        check_winner()


def click2():
    global turn
    if btn2["text"] == " ":
        if turn == 1:
            turn = 2
            btn2["text"] = "X"
        elif turn == 2:
            turn = 1
            btn2["text"] = "O"
        check_winner()


def click3():
    global turn
    if btn3["text"] == " ":
        if turn == 1:
            turn = 2
            btn3["text"] = "X"
        elif turn == 2:
            turn = 1
            btn3["text"] = "O"
        check_winner()


def click4():
    global turn
    if btn4["text"] == " ":
        if turn == 1:
            turn = 2
            btn4["text"] = "X"
        elif turn == 2:
            turn = 1
            btn4["text"] = "O"
        check_winner()


def click5():
    global turn
    if btn5["text"] == " ":
        if turn == 1:
            turn = 2
            btn5["text"] = "X"
        elif turn == 2:
            turn = 1
            btn5["text"] = "O"
        check_winner()


def click6():
    global turn
    if btn6["text"] == " ":
        if turn == 1:
            turn = 2
            btn6["text"] = "X"
        elif turn == 2:
            turn = 1
            btn6["text"] = "O"
        check_winner()


def click7():
    global turn
    if btn7["text"] == " ":
        if turn == 1:
            turn = 2
            btn7["text"] = "X"
        elif turn == 2:
            turn = 1
            btn7["text"] = "O"
        check_winner()


def click8():
    global turn
    if btn8["text"] == " ":
        if turn == 1:
            turn = 2
            btn8["text"] = "X"
        elif turn == 2:
            turn = 1
            btn8["text"] = "O"
        check_winner()


def click9():
    global turn
    if btn9["text"] == " ":
        if turn == 1:
            turn = 2
            btn9["text"] = "X"
        elif turn == 2:
            turn = 1
            btn9["text"] = "O"
        check_winner()


flag = 1


def check_winner():
    global flag
    b1 = btn1["text"]
    b2 = btn2["text"]
    b3 = btn3["text"]
    b4 = btn4["text"]
    b5 = btn5["text"]
    b6 = btn6["text"]
    b7 = btn7["text"]
    b8 = btn8["text"]
    b9 = btn9["text"]

    flag = flag+1
    
    if b1 == b2 and b1 == b3 and b1 == "O" or b1 == b2 and b1 == b3 and b1 == "X":
        win(btn1["text"])
    if b4 == b5 and b4 == b6 and b4 == "O" or b4 == b5 and b4 == b6 and b4 == "X":
        win(btn4["text"])
    if b7 == b8 and b7 == b9 and b7 == "O" or b7 == b8 and b7 == b9 and b7 == "X":
        win(btn7["text"])
    if b1 == b4 and b1 == b7 and b1 == "O" or b1 == b4 and b1 == b7 and b1 == "X":
        win(btn1["text"])
    if b2 == b5 and b2 == b8 and b2 == "O" or b2 == b5 and b2 == b8 and b2 == "X":
        win(btn2["text"])
    if b3 == b6 and b3 == b9 and b3 == "O" or b3 == b6 and b3 == b9 and b3 == "X":
        win(btn3["text"])
    if b1 == b5 and b1 == b9 and b1 == "O" or b1 == b5 and b1 == b9 and b1 == "X":
        win(btn1["text"])
    if b7 == b5 and b7 == b3 and b7 == "O" or b7 == b5 and b7 == b3 and b7 == "X":
        win(btn7["text"])
    if flag == 10:
        messagebox.showinfo("It's a Draw, Play Again!")
        root.destroy()


def win(player):
    msg = "Game complete " + player + " wins "
    messagebox.showinfo("Congratulations", msg)
    root.destroy()


btn1 = Button(root, text=" ", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=click1)
btn1.grid(column=1, row=1)
btn2 = Button(root, text=" ", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=click2)
btn2.grid(column=2, row=1)
btn3 = Button(root, text=" ", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=click3)
btn3.grid(column=3, row=1)
btn4 = Button(root, text=" ", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=click4)
btn4.grid(column=1, row=2)
btn5 = Button(root, text=" ", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=click5)
btn5.grid(column=2, row=2)
btn6 = Button(root, text=" ", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=click6)
btn6.grid(column=3, row=2)
btn7 = Button(root, text=" ", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=click7)
btn7.grid(column=1, row=3)
btn8 = Button(root, text=" ", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=click8)
btn8.grid(column=2, row=3)
btn9 = Button(root, text=" ", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=click9)
btn9.grid(column=3, row=3)

root.mainloop()
