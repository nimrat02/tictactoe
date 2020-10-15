from tkinter.messagebox import showinfo
from tkinter import *
from tkmacosx import Button


class demo:


    def reset(self):
        self.play=0
        self.bt1["text"]=""
        self.bt1["state"]="normal"

        self.bt2["text"]=""
        self.bt2["state"]="normal"

        self.bt3["text"]=""
        self.bt3["state"]="normal"

        self.bt4["text"]=""
        self.bt4["state"]="normal"

        self.bt5["text"]=""
        self.bt5["state"]="normal"

        self.bt6["text"]=""
        self.bt6["state"]="normal"

        self.bt7["text"]=""
        self.bt7["state"]="normal"

        self.bt8["text"]=""
        self.bt8["state"]="normal"

        self.bt9["text"]=""
        self.bt9["state"]="normal"

    def checkwin(self):
        if self.bt1["text"]=="X" and self.bt2["text"]=="X" and self.bt3["text"]=="X":
            self.bt1["highlightbackground"] = "red"
            self.bt2["bg"] = "red"
            self.bt3["bg"] = "red"
            showinfo("TIC TAC TOE","X Wins")
            self.reset()


        elif self.bt4["text"]=="X" and self.bt5["text"]=="X" and self.bt6["text"]=="X":
            self.bt4["bg"] = "red"
            self.bt5["bg"] = "red"
            self.bt6["bg"] = "red"
            showinfo("TIC TAC TOE","X Wins")
            self.reset()
        elif self.bt7["text"]=="X" and self.bt8["text"]=="X" and self.bt9["text"]=="X":
            self.bt7["bg"] = "red"
            self.bt8["bg"] = "red"
            self.bt9["bg"] = "red"
            showinfo("TIC TAC TOE","X Wins")
            self.reset()
        elif self.bt1["text"]=="X" and self.bt2["text"]=="X" and self.bt3["text"]=="X":
            self.bt1["bg"] = "red"
            self.bt2["bg"] = "red"
            self.bt3["bg"] = "red"
            showinfo("TIC TAC TOE","X Wins")
            self.reset()
        elif self.bt1["text"]=="X" and self.bt4["text"]=="X" and self.bt7["text"]=="X":
            self.bt1["bg"] = "red"
            self.bt4["bg"] = "red"
            self.bt7["bg"] = "red"
            showinfo("TIC TAC TOE","X Wins")
            self.reset()
        elif self.bt2["text"]=="X" and self.bt5["text"]=="X" and self.bt8["text"]=="X":
            self.bt2["bg"] = "red"
            self.bt5["bg"] = "red"
            self.bt8["bg"] = "red"
            showinfo("TIC TAC TOE","X Wins")
            self.reset()
        elif self.bt3["text"]=="X" and self.bt6["text"]=="X" and self.bt9["text"]=="X":
            self.bt3["bg"] = "red"
            self.bt6["bg"] = "red"
            self.bt9["bg"] = "red"
            showinfo("TIC TAC TOE","X Wins")
            self.reset()
        elif self.bt1["text"]=="X" and self.bt5["text"]=="X" and self.bt9["text"]=="X":
            self.bt1["bg"] = "red"
            self.bt5["bg"] = "red"
            self.bt9["bg"] = "red"
            showinfo("TIC TAC TOE","X Wins")
            self.reset()
        elif self.bt3["text"]=="X" and self.bt5["text"]=="X" and self.bt7["text"]=="X":
            self.bt3["bg"] = "red"
            self.bt5["bg"] = "red"
            self.bt7["bg"] = "red"
            showinfo("TIC TAC TOE","X Wins")
            self.reset()
        if self.bt1["text"]=="0" and self.bt2["text"]=="0" and self.bt3["text"]=="0":
            self.bt1["bg"] = "red"
            self.bt2["bg"] = "red"
            self.bt3["bg"] = "red"
            showinfo("TIC TAC TOE","0 Wins")
            self.reset()
        elif self.bt4["text"]=="0" and self.bt5["text"]=="0" and self.bt6["text"]=="0":
            self.bt4["bg"] = "red"
            self.bt5["bg"] = "red"
            self.bt6["bg"] = "red"
            showinfo("TIC TAC TOE","0 Wins")
            self.reset()
        elif self.bt7["text"]=="0" and self.bt8["text"]=="0" and self.bt9["text"]=="0":
            self.bt7["bg"] = "red"
            self.bt8["bg"] = "red"
            self.bt9["bg"] = "red"
            showinfo("TIC TAC TOE","0 Wins")
            self.reset()
        elif self.bt1["text"]=="0" and self.bt2["text"]=="0" and self.bt3["text"]=="0":
            self.bt1["bg"] = "red"
            self.bt2["bg"] = "red"
            self.bt3["bg"] = "red"
            showinfo("TIC TAC TOE","0 Wins")
            self.reset()
        elif self.bt1["text"]=="0" and self.bt4["text"]=="0" and self.bt7["text"]=="0":
            self.bt1["bg"] = "red"
            self.bt4["bg"] = "red"
            self.bt7["bg"] = "red"
            showinfo("TIC TAC TOE","0 Wins")
            self.reset()
        elif self.bt2["text"]=="0" and self.bt5["text"]=="0" and self.bt8["text"]=="0":
            self.bt2["bg"] = "red"
            self.bt5["bg"] = "red"
            self.bt8["bg"] = "red"
            showinfo("TIC TAC TOE","0 Wins")
            self.reset()
        elif self.bt3["text"]=="0" and self.bt6["text"]=="0" and self.bt9["text"]=="0":
            self.bt3["bg"] = "red"
            self.bt6["bg"] = "red"
            self.bt9["bg"] = "red"
            showinfo("TIC TAC TOE","0 Wins")
            self.reset()
        elif self.bt1["text"]=="0" and self.bt5["text"]=="0" and self.bt9["text"]=="0":
            self.bt1["bg"] = "red"
            self.bt5["bg"] = "red"
            self.bt9["bg"] = "red"
            showinfo("TIC TAC TOE","0 Wins")
            self.reset()
        elif self.bt3["text"]=="0" and self.bt5["text"]=="0" and self.bt7["text"]=="0":
            self.bt3["bg"] = "red"
            self.bt5["bg"] = "red"
            self.bt7["bg"] = "red"
            showinfo("TIC TAC TOE","0 Wins")
            self.reset()

#--------------------------------------------------
    def fire1(self):
        if self.play%2==0:
            self.bt1["text"]="X"
        else:
            self.bt1["text"]="0"
        self.play=self.play+1
        self.bt1["state"]="disabled"
        self.checkwin()

    def fire2(self):
        if self.play%2==0:
            self.bt2["text"]="X"
        else:
            self.bt2["text"]="0"
        self.play=self.play+1
        self.bt2["state"]="disabled"
        self.checkwin()


    def fire3(self):
        if self.play % 2 == 0:
            self.bt3["text"] = "X"
        else:
            self.bt3["text"] = "0"
        self.play = self.play + 1
        self.bt3["state"]="disabled"
        self.checkwin()


    def fire4(self):
        if self.play % 2 == 0:
            self.bt4["text"] = "X"
        else:
            self.bt4["text"] = "0"
        self.play = self.play + 1
        self.bt4["state"]="disabled"
        self.checkwin()


    def fire5(self):
        if self.play % 2 == 0:
            self.bt5["text"] = "X"
        else:
            self.bt5["text"] = "0"
        self.play = self.play + 1
        self.bt5["state"]="disabled"
        self.checkwin()


    def fire6(self):
        if self.play % 2 == 0:
            self.bt6["text"] = "X"
        else:
            self.bt6["text"] = "0"
        self.play = self.play + 1
        self.bt6["state"]="disabled"
        self.checkwin()


    def fire7(self):
        if self.play % 2 == 0:
            self.bt7["text"] = "X"
        else:
            self.bt7["text"] = "0"
        self.play = self.play + 1
        self.bt7["state"]="disabled"
        self.checkwin()


    def fire8(self):
        if self.play % 2 == 0:
            self.bt8["text"] = "X"
        else:
            self.bt8["text"] = "0"
        self.play = self.play + 1
        self.bt8["state"]="disabled"
        self.checkwin()


    def fire9(self):
        if self.play % 2 == 0:
            self.bt9["text"] = "X"
        else:
            self.bt9["text"] = "0"
        self.play = self.play + 1
        self.bt9["state"]="disabled"
        self.checkwin()






    def __init__(self):
        self.play=0
        self.root=Tk()
        self.root.title("tic tac toe")

        self.root.geometry("400x400")

        self.bt1=Button(self.root,text="",width=10,command=self.fire1)
        self.bt2=Button(self.root,text="",width=10,command=self.fire2)
        self.bt3=Button(self.root,text="",width=10,command=self.fire3)

        self.bt4=Button(self.root,text="",width=10,command=self.fire4)
        self.bt5=Button(self.root,text="",width=10,command=self.fire5)
        self.bt6=Button(self.root,text="",width=10,command=self.fire6)

        self.bt7=Button(self.root,text="",width=10,command=self.fire7)
        self.bt8=Button(self.root,text="",width=10,command=self.fire8)
        self.bt9=Button(self.root,text="",width=10,command=self.fire9)


        self.bt1.grid(row=0,column=0)
        self.bt2.grid(row=0,column=1)
        self.bt3.grid(row=0,column=2)

        self.bt4.grid(row=1,column=0)
        self.bt5.grid(row=1,column=1)
        self.bt6.grid(row=1,column=2)

        self.bt7.grid(row=2,column=0)
        self.bt8.grid(row=2,column=1)
        self.bt9.grid(row=2,column=2)

        self.root.mainloop()
#-------------------------------

x=demo()
