from tkinter import *
import mouse

rightclickamount = 0
leftclickamount = 0
middleclickamount = 0

def onrightclick():
    global rightclickamount
    rightclickamount += 1
    print("right: " + str(rightclickamount))
    label2.configure(text=f'Rightclicked: {rightclickamount} times!!!')

def onleftclick():
    global leftclickamount
    leftclickamount += 1
    print("left: " + str(leftclickamount))

    label1.configure(text=f'Leftclicked: {leftclickamount} times!!!')

def onmiddleclick():
    global middleclickamount
    middleclickamount += 1
    print("left: " + str(middleclickamount))

    label3.configure(text=f'middleclick: {middleclickamount} times!!!')

root = Tk()
mouse.on_click(onleftclick)
mouse.on_right_click(onrightclick)
mouse.on_middle_click(onmiddleclick)

root.title("My Application")

label = Label(root, text="Hello World")
label.grid(column=0, row=0)

label1 = Label(root)
label1.grid(column=0, row=1)

label2 = Label(root)
label2.grid(column=0, row=2)

label3 = Label(root)
label3.grid(column=0, row=3)

root.mainloop()
