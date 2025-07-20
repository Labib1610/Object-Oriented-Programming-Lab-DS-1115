from tkinter import *

class Calculator(Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculator')      #   tk er naam er jaegae likha hobe eita

        self.first_num = 0.0   #    +, - e kaj korbe.
        self.operator = ''



        self.e = Entry(self, width= 35, borderwidth= 5)
        self.e.grid(row= 0, column= 0, columnspan= 3, padx= 10, pady= 10)

        # Create the number button

        self.button_0 = Button(self, padx= 40, pady= 20, text= str(0), command= lambda: self.take_input(0))
        self.button_1 = Button(self, padx= 40, pady= 20, text= str(1), command= lambda: self.take_input(1))
        self.button_2 = Button(self, padx= 40, pady= 20, text= str(2), command= lambda: self.take_input(2))
        self.button_3 = Button(self, padx= 40, pady= 20, text= str(3), command= lambda: self.take_input(3))
        self.button_4 = Button(self, padx= 40, pady= 20, text= str(4), command= lambda: self.take_input(4))
        self.button_5 = Button(self, padx= 40, pady= 20, text= str(5), command= lambda: self.take_input(5))
        self.button_6 = Button(self, padx= 40, pady= 20, text= str(6), command= lambda: self.take_input(6))
        self.button_7 = Button(self, padx= 40, pady= 20, text= str(7), command= lambda: self.take_input(7))
        self.button_8 = Button(self, padx= 40, pady= 20, text= str(8), command= lambda: self.take_input(8))
        self.button_9 = Button(self, padx= 40, pady= 20, text= str(9), command= lambda: self.take_input(9))

        # Place the number button


        self.button_0.grid(row= 4, column= 0)


        self.button_1.grid(row= 3, column= 0)
        self.button_2.grid(row= 3, column= 1)
        self.button_3.grid(row= 3, column= 2)

        self.button_4.grid(row= 2, column= 0)
        self.button_5.grid(row= 2, column= 1)
        self.button_6.grid(row= 2, column= 2)

        self.button_7.grid(row= 1, column= 0)
        self.button_8.grid(row= 1, column= 1)
        self.button_9.grid(row= 1, column= 2)


        # Create the numerical buttons

        self.button_add = Button(self, text='+', padx= 40, pady= 20, command= self.add)
        self.button_sub = Button(self, text='-', padx= 40, pady= 20)
        self.button_mul = Button(self, text='X', padx= 40, pady= 20)
        self.button_div = Button(self, text='/', padx= 40, pady= 20)
        self.button_equal = Button(self, text='=', padx= 40, pady= 20, command=self.equal)
        self.button_clear = Button(self, text='Clear', padx= 40, pady= 20, command= self.clear)

        # Placing the numerical Buttons

        self.button_clear.grid(row= 4, column= 1, columnspan= 2)
        self.button_add.grid(row= 5, column= 0)
        self.button_equal.grid(row=5,column=1,columnspan=2)
        self.button_sub.grid(row= 6, column= 0)
        self.button_mul.grid(row= 6, column= 1)
        self.button_div.grid(row= 6, column= 2)
    def take_input(self,number):
        current = self.e.get()
        total = current + str(number)
        self.e.delete(0, END)
        self.e.insert(0, total)

    def clear(self):
        self.e.delete(0, END)

    def add(self):
        self.first_num = float(self.e.get())
        self.operator = '+'
        self.e.delete(0, END)



    def equal(self):
        second_num = float(self.e.get())
        self.e.delete(0, END)

        if self.operator == '+':
            self.e.insert(0, self.first_num + second_num)

if __name__ == '__main__':
    myApp = Calculator()
    myApp.mainloop()