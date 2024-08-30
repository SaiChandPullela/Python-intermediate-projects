from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=30)

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    print(original_data)
    words_dictionary_list = original_data.to_dict(orient="records")
else:
    words_dictionary_list = data.to_dict(orient="records")

# Getting hold of words

random_entry = {}


# Function to display french words from the list every time we click either of the buttons
def random_word():
    global random_entry, flip_time
    window.after_cancel(flip_time)
    random_entry = random.choice(words_dictionary_list)
    canvas.itemconfig(title_text, text='french', fill='black')
    canvas.itemconfig(word_text, text=random_entry['French'], fill='black')
    canvas.itemconfig(card_background, image=card_front_image)
    flip_time = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=random_entry['English'], fill='white')
    canvas.itemconfig(card_background, image=card_back_image)


def is_known():
    words_dictionary_list.remove(random_entry)
    data = pd.DataFrame(words_dictionary_list)
    data.to_csv('data/words_to_learn')
    random_word()


flip_time = window.after(3000, func=flip_card)
front_image = PhotoImage(file='../flash_card_project/images/card_front.png')
right_image = PhotoImage(file='../flash_card_project/images/right.png')
wrong_image = PhotoImage(file='../flash_card_project/images/wrong.png')

# Flip cards
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_image = PhotoImage(file='images/card_back.png')
card_front_image = PhotoImage(file='images/card_front.png')
card_background = canvas.create_image(410, 275, image=front_image)
canvas.after(3000, flip_card)

title_text = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
word_text = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# Right and wrong buttons
right_button = Button(image=right_image, highlightthickness=0, padx=50, pady=50, command=is_known)
right_button.grid(row=1, column=0)

wrong_button = Button(image=wrong_image, highlightthickness=0, padx=50, pady=50, command=random_word)
wrong_button.grid(row=1, column=1)

random_word()

window.mainloop()
