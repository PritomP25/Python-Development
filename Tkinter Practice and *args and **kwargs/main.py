import tkinter
from tkinter import Entry

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

#Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
#my_label.pack()
# my_label.pack(expand=True)

my_label["text"] = "New Text"
my_label.config(text="New Text")
#my_label.place(x=100,y=200)
my_label.grid(row=0,column=0)
my_label.config(padx=50, pady=50)

#Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = tkinter.Button(text="Click Me", command=button_clicked)
#button.pack()
button.grid(row=1,column=1)

new_button = tkinter.Button(text="New Button")
new_button.grid(row=0, column=2)


#Entry
input = Entry(width=10)
print(input.get())
#input.pack()
input.grid(row=3,column=3)











# This what leads the window to be on!
# ALWAYS has to be the last line 
window.mainloop()