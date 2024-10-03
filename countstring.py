from tkinter import *
from tkinter import messagebox 

def clearAll() :
    str1Field.delete(0, END)
    char1Field.delete(0, END)
    resultField.delete(0, END)
    
def checkError() : 
    if (str1Field.get() == "" or char1Field.get() == "") :
        messagebox.showerror("Input Error")
        clearAll()
        return -1

def occurrences() :
    value = checkError()
    if value == -1 :
        return 
    else :
        String0 = (str1Field.get())
        char0 = (char1Field.get())
        
        i=0
        count=0
        while(i<len(String0)):
            if(String0[i]==char0):
                count=count+1
            i=i+1
        
        resultField.insert(10, str(count))
        
if __name__ == "__main__" :

    gui = Tk()
    gui.configure(background = "light green")
    gui.title("occurrences of a character in a string")
    gui.geometry("525x260")
 
 
 
    Stringin = Label(gui, text = " given String", bg = "#00ffff") 
    char = Label(gui, text = "given character", bg = "#00ffff") 
    str1 = Label(gui, text = "String", bg = "light green")
    char1 = Label(gui, text = "character", bg = "light green")
    
    occurrenceslabel = Label(gui, text = "occurrences \n character",
    bg = "light green")
    
    result = Button(gui, text = "Result", fg = "Black",
    bg = "gray", command = occurrences)
    clearAllEntry = Button(gui, text = "Clear All", fg = "Black",
    bg = "Red", command = clearAll) 

    str1Field = Entry(gui)
    char1Field = Entry(gui)
    resultField = Entry(gui)

Stringin.grid(row = 0, column = 1)
str1.grid(row = 1, column = 0)
str1Field.grid(row = 1, column = 1)
    
    
char.grid(row = 0, column = 4)
char1.grid(row = 1, column = 3)
char1Field.grid(row = 1, column = 4)
    
result.grid(row = 4, column = 2)
occurrenceslabel.grid(row = 5, column = 2)
resultField.grid(row = 6, column = 2)
clearAllEntry.grid(row = 12, column = 2)
gui.mainloop()
