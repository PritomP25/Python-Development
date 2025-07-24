import tkinter
from tkinter import Entry

def conversation():
    mi = float(miles_input.get())
    km = round(mi * 1.609,2)
    km_result_label.config(text=f"{km}")


#windows configurations
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

#Entry
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)


#Label
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to = tkinter.Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

km_result_label = tkinter.Label(text="0")
km_result_label.grid(column=1, row=1)

#Button
calculation_button = tkinter.Button(text="Calculate", command=conversation)
calculation_button.grid(column=1, row=2)


window.mainloop()