#Simple adding program using tkinter gui

from tkinter import Tk
from tkinter import Button
from tkinter import Label
from tkinter import Entry

class Adder:

    def display(self):

        root = Tk(screenName="adder")

        def redden_entry(entry):
            entry.config(background="red")

        def whiten_entry(entry):
            entry.config(background="white")

        first_number_label = Label(root, text = "First Number")
        first_number_label.grid(sticky="E", padx=5, pady=5, row=0, column=0)

        first_number_entry = Entry(root, width=10)
        first_number_entry.grid(padx=5, pady=5, row=0, column=1)

        second_number_label = Label(root, text = "Second Number")
        second_number_label.grid(sticky="E", padx=5, pady=5, row=1, column=0)

        second_number_entry = Entry(root, width=10)
        second_number_entry.grid(padx=5, pady=5, row=1, column=1)

        result_label = Label(root, text="Result")
        result_label.grid(sticky="EW", padx=5, pady=5, columnspan=2, row=3, column=0)

        def add_event():

            error_message = ""
            first_number_text = first_number_entry.get()
            second_number_text = second_number_entry.get()
            try:
                first_number = float(first_number_text)
                whiten_entry(first_number_entry)
            except ValueError:
                redden_entry(first_number_entry)
                error_message += "First number invalid.\n"   

            try:
                second_number = float(second_number_text)
                whiten_entry(second_number_entry)
            except ValueError:
                redden_entry(second_number_entry)
                error_message += "Second number invalid."
            
            if error_message != "":
                result = error_message
            else:
                result = first_number+second_number
                
            result_label.config(text=str(result))

        add_button = Button(root, text="Add", command=add_event)
        add_button.grid(sticky="EW", row=2, column=0, columnspan=2, padx=5, pady=5)        

        root.mainloop()


if __name__ == '__main__':
    app = Adder()
    app.display()
