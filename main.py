import tkinter
from tkinter import *
import random 
from tkinter import messagebox
import random

root = Tk()

letters_in_word = []
shuffled_word_list= []

score = 0
attempts = 0

word_bank = ["word","mango","apple","pineapple","banana","table","computer","code","python","bottle","clock","wall","painting","window","box","book","pencil"]



def shuffle():
    global jumbled_word,word
    word = random.choice(word_bank)
    for letter in word:
        letters_in_word.append(i)
    random.shuffle(letters_in_word)
    jumbled_word = ''.join(letters_in_word)
    print(word,jumbled_word)
    return jumbled_word

def reset():
    global jumbled_word, attempts, score
    shuffle()
    jumbled_word_label.config(text=jumbled_word)
    entry.delete(0,END)

def default():
    shuffle()
    jumbled_word_label.config(text=jumbled_word)

def checkans():
    if word == entry.get():
        messagebox.showinfo("You Won!","You Won!")
        score+=1
        attempts +=1
        reset()
    if word != entry.get():
        messagebox.showinfo("Wrong!","You got the word wrong!")
        attempts +=1

root.geometry("500x500")
root.title("Game")
root.configure(background="#000000")

Label(root,text ="JUMBLED WORD GAME",font=("Verdana",28), bg="#000000").pack(pady=5)
jumbled_word_label = Label(root,font= ("Verdana",22),bg="#000000", fg="#fff")
jumbled_word_label.pack(pady=30, ipady=10, ipadx=10)

ans = StringVar()
entry = Entry(root,font = ("Verdana", 20))
entry.pack

check_button = Button(root,text= "Check", font = ("Comic Sans ms",20), width = 10, bg = "#333945",fg="#45CE30",relief = GROOVE, command=checkans)
check_button.pack
reset_button = Button(root,text= "Reset", font = ("Comic Sans ms",20), width = 10, bg = "#333945",fg="#45CE30",relief = GROOVE, command=reset)
reset_button.pack
root.mainloop()


