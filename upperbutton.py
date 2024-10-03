from tkinter import *
from tkinter import messagebox 

def clearAll() :
    str1Field.delete(0, END)
    altersField.delete(0, END)
    
def checkError() : 
    if (str1Field.get() == "" ) :
        messagebox.showerror("Input Error")
        clearAll()
        return -1

def upper() :
    value = checkError()
    if value == -1 :
        return 
    else :
        String0 = (str1Field.get())
        
        newstr=String0.upper()
        
        
        altersField.insert(20, str(newstr))
        
if __name__ == "__main__" :
    gui = Tk()
    gui.configure(background = "light green")
    gui.title("upper case")
    gui.geometry("250x200")
    
    Stringin = Label(gui, text = " given String", bg = "#00ffff")
    str1 = Label(gui, text = "String", bg = "light green")
    str1Field = Entry(gui)
    
    result = Button(gui, text = "Result", fg = "Black",
                bg = "gray", command = upper)
    
    alters = Label(gui, text = "upper case string", bg = "light green")
    altersField = Entry(gui)
    
    clearAllEntry = Button(gui, text = "Clear All", fg = "Black",
                bg = "Red", command = clearAll) 


Stringin.grid(row = 0, column = 1)
str1.grid(row = 1, column = 0)
str1Field.grid(row = 1, column = 1)
    

alters.grid(row = 2, column = 0)
altersField.grid(row = 2, column = 1)
clearAllEntry.grid(row = 3, column = 0)
result.grid(row = 3, column = 1)
gui.mainloop()
