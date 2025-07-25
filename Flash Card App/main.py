import tkinter
import pandas
import random
from tkinter import Canvas, PhotoImage

BACKGROUND_COLOR = "#B1DDC6"

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image= card_back_img)

def is_known():
    to_learn_dict.remove(current_card)
    data = pandas.DataFrame(to_learn_dict)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()


if __name__ == "__main__":
    current_card = {}
    to_learn = {}
    try:
        data_file = pandas.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        original_data = pandas.read_csv("data/french_words.csv")
        to_learn = original_data.to_dict(orient="records")
    else:
        to_learn_dict = pandas.DataFrame(data_file).to_dict(orient="records")


    window = tkinter.Tk()
    window.title("Flashy")
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


    flip_timer = window.after(3000, func=flip_card)

    canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
    front_img = tkinter.PhotoImage(file="images/card_front.png")
    card_back_img = PhotoImage(file="images/card_back.png")
    card_background = canvas.create_image(400, 263, image=front_img)
    card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
    card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
    canvas.grid(column=0, row=0, columnspan=2)

    #Button
    right_img = tkinter.PhotoImage(file="images/right.png")
    check_button = tkinter.Button(image=right_img, highlightthickness=0, command=is_known)
    check_button.grid(column=1, row=1)

    wrong_img = tkinter.PhotoImage(file="images/wrong.png")
    wrong_button = tkinter.Button(image=wrong_img, highlightthickness=0, command=next_card)
    wrong_button.grid(column=0, row=1)

    next_card()

    window.mainloop()
