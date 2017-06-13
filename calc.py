'''
Created on May 14, 2017

@author: luciachen
'''
from tkinter import Tk, Frame, Button, Entry, RIGHT, END

class Calculator(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.textbox = Entry(self, justify = RIGHT)
        self.textbox.grid(row = 0, column = 0, columnspan = 4)
        self.textbox.insert(0, "0")

        # Buttons
        Button(self, text = 'AC', width = 8, command = self.clear).grid(row = 1, column = 0, columnspan = 2, )
        Button(self, text = '%', width = 3, command = lambda:self.numpress('%')).grid(row = 1, column = 2, columnspan = 1)
        Button(self, text = '/', width = 3, command = lambda:self.numpress('/')).grid(row = 1, column = 3, columnspan = 1)
        Button(self, text = '7', width = 3, command = lambda:self.numpress(7)).grid(row = 2, column = 0, columnspan = 1)
        Button(self, text = '8', width = 3, command = lambda:self.numpress(8)).grid(row = 2, column = 1, columnspan = 1)
        Button(self, text = '9', width = 3, command = lambda:self.numpress(9)).grid(row = 2, column = 2, columnspan = 1)
        Button(self, text = '*', width = 3, command = lambda:self.numpress('*')).grid(row = 2, column = 3, columnspan = 1)
        Button(self, text = '4', width = 3, command = lambda:self.numpress(4)).grid(row = 3, column = 0, columnspan = 1)
        Button(self, text = '5', width = 3, command = lambda:self.numpress(5)).grid(row = 3, column = 1, columnspan = 1)
        Button(self, text = '6', width = 3, command = lambda:self.numpress(6)).grid(row = 3, column = 2, columnspan = 1)
        Button(self, text = '-', width = 3, command = lambda:self.numpress('-')).grid(row = 3, column = 3, columnspan = 1)
        Button(self, text = '1', width = 3, command = lambda:self.numpress(1)).grid(row = 4, column = 0, columnspan = 1)
        Button(self, text = '2', width = 3, command = lambda:self.numpress(2)).grid(row = 4, column = 1, columnspan = 1)
        Button(self, text = '3', width = 3, command = lambda:self.numpress(3)).grid(row = 4, column = 2, columnspan = 1)
        Button(self, text = '+', width = 3, command = lambda:self.numpress('+')).grid(row = 4, column = 3, columnspan = 1)
        Button(self, text = '0', width = 8, command = lambda:self.numpress(0)).grid(row = 5, column = 0, columnspan = 2)
        Button(self, text = '.', width = 3, command = lambda:self.numpress('.')).grid(row = 5, column = 2, columnspan = 1)
        Button(self, text = '=', width = 3, command = self.equals).grid(row = 5, column = 3, columnspan = 1)
        
    def numpress(self, num):
        self.expression = self.textbox.get()
        if self.expression == '0':
            self.textbox.delete(0, END)
            self.textbox.insert(0, num)
        else:
            self.textbox.insert(END, num)
    
    def clear(self):
        self.textbox.delete(0, END)
        self.textbox.insert(0, "0")

    def equals(self):
        self.expression = self.textbox.get()
        self.expression = self.expression.replace('%', '/100 ')
        try:
            self.value = eval(self.expression)
        except:
            self.textbox.delete(0,END)
            self.textbox.insert(0,'ERROR')
        else:
            self.textbox.delete(0,END)
            self.textbox.insert(0,self.value)
    
def main():
    root = Tk()
    Calculator(root)
    root.mainloop()

if __name__ == '__main__': main()
