from tkinter import *

def clearAll() :
    numberField.delete(0, END);Lb1.delete(0,END)
def multiplication():
    num = int(numberField.get())
    Lb1.insert(0, '{} X 1 = {}'.format(num,1*num))
    Lb1.insert(1, '{} X 2 = {}'.format(num,2*num))
    Lb1.insert(2, '{} X 3 = {}'.format(num,3*num))
    Lb1.insert(3, '{} X 4 = {}'.format(num,4*num))
    Lb1.insert(4, '{} X 5 = {}'.format(num,5*num))
    Lb1.insert(5, '{} X 6 = {}'.format(num,6*num))
    Lb1.insert(6, '{} X 7 = {}'.format(num,7*num))
    Lb1.insert(7, '{} X 8 = {}'.format(num,8*num))
    Lb1.insert(8, '{} X 9 = {}'.format(num,9*num))
    Lb1.insert(9,'{} X 10 = {}'.format(num,10*num))
if __name__=="__main__" :
    gui = Tk()
    gui.configure(background = "light green")
    gui.title("multiplication table")
    gui.geometry("400x300")
    label=Label(gui,text='multiplication table \
                on button click').pack(side=TOP,fill=BOTH)
    number = Label(gui, text = "Give number", bg = "#00ffff").pack(fill=BOTH)
    numberField = Entry(gui)
    numberField.pack()
    resultbutton = Button(gui, text = "Result button",
                fg = "Black", bg = "gray",command=multiplication).pack()

Lb1 = Listbox(gui,fg='yellow',width=30,bg='gray',bd=1,activestyle='dotbox')

clearAllEntry = Button(gui, text = "Clear All",
            fg = "Black", bg = "gray", command = clearAll).pack(side=BOTTOM)

Lb1.pack()
gui.mainloop()
