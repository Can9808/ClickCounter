from tkinter import *
import mouse

rightclickamount = 0
leftclickamount = 0


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

root = Tk()
mouse.on_click(onleftclick)
mouse.on_right_click(onrightclick)


root.title("My Application")

label = Label(root, text="Hello World")
label.grid(column=0, row=0)

label1 = Label(root)
label1.grid(column=0, row=1)

label2 = Label(root)
label2.grid(column=0, row=2)

root.mainloop()
