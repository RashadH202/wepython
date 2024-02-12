from tkinter import Tk, Label, Button, Entry

#functionaility button push

def button_clicked():
    new_text = input_entry.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My first GUI Program")
window.geometry("500x300")
window.config(padx=100, pady=200)

# label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"), padx=50, pady=50)
my_label.grind(column=0, row=0)

# button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# New Button

new_button = button(text="New Button")

# Entry
input_entry = Entry(width=10)
input_entry.grid(column=3, row=2)

window.mainloop()
