import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyttsx3
import speech_to_text as stt
import percentage_finder as pf
import emoji
import os

engine=pyttsx3.init()

engine.setProperty("rate",200)
engine.setProperty("volume",1)

voices=engine.getProperty('voices')
engine.setProperty("voice",voices[0].id)

window=tk.Tk()
window.geometry("900x600")
window.title("Speech Impediment Helper")


#notebooks(for tabs)
notebook=ttk.Notebook(window)

tab1=tk.Frame(notebook)
tab2=tk.Frame(notebook)
notebook.add(tab1,text="TTS")
notebook.add(tab2,text="STT")

notebook.pack(expand=True,fill="both")

#for background images
script_dir=os.path.dirname(os.path.abspath(__file__))

image_path_tab1=os.path.join(script_dir,"colourful_circle.png")
bg_image_tab1=tk.PhotoImage(file=image_path_tab1)

bg_label_tab1=tk.Label(tab1,image=bg_image_tab1)
bg_label_tab1.place(relwidth=1,relheight=1)
bg_label_tab1=bg_image_tab1

image_path_tab2=os.path.join(script_dir,"nature_scenery.png")
bg_image_tab2=tk.PhotoImage(file=image_path_tab2)

bg_label_tab2=tk.Label(tab2,image=bg_image_tab2)
bg_label_tab2.place(relwidth=1,relheight=1)
bg_label_tab2=bg_image_tab2

def choose_voice():
    if(x.get()==0):
        engine.setProperty("voice", voices[0].id)
    elif(x.get()==1):
        engine.setProperty("voice", voices[1].id)
    else:
        pass

"""def choose_volume():
    engine.setProperty("volume",scale_vol.get())
def choose_rate():
    engine.setProperty("rate",scale_rate.get())"""

def set_voice():
    global x
    x = tk.IntVar()
    settings_window = tk.Toplevel(window)
    settings_window.geometry("400x300")
    settings_window.title("Voice Settings")

    emoji_woman=emoji.emojize(":woman:")
    emoji_man=emoji.emojize(":man:")

    op_voi=[emoji_man+"Male Voice",emoji_woman+"Female Voice"]

    for i in range(len(op_voi)):
        radiobutton=tk.Radiobutton(settings_window,
                                   text=op_voi[i],
                                   variable=x,
                                   value=i,
                                   font=("Helvetica",12)
                                   )
        radiobutton.pack(anchor="w")

    apply_button = tk.Button(settings_window, text="Apply", command=choose_voice)
    apply_button.pack(pady=1)
""""
    scale_vol = tk.Scale(settings_window, from_=1, to=0,resolution=0.1,orient="horizontal")
    scale_vol.pack(padx=10)
    button_vol = tk.Button(settings_window, text="Apply", command=choose_volume())
    button_vol.pack()

    scale_rate=tk.Scale(settings_window,from_=300,to=100,orient="horizontal")
    scale_rate.pack(pady=20)
    button=tk.Button(settings_window,text="Apply",command=choose_rate())
    button.pack()"""


#menu_bar
menubar=tk.Menu(window)
window.config(menu=menubar)
filemenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Settings",command=set_voice)
filemenu.add_command(label="Exit",command=quit)

#buttons oooo
def speak_out():
    filled_in=entry.get()
    engine.say(filled_in)
    engine.runAndWait()

def clear():
    entry.delete(0,tk.END)
    custom_phrase.delete(0,tk.END)

def add_phrase(a):
    current_text=entry.get()
    new_text=current_text+" "+a
    entry.delete(0, tk.END)
    entry.insert(0,new_text)

def save_custom_phrase():
    given_entry=custom_phrase.get()
    if given_entry:
        given_entry_button=tk.Button(phrases_frame,text=given_entry,command=lambda p=given_entry: add_phrase(p))
        given_entry_button.pack(side=tk.LEFT,padx=5,pady=5)
    custom_phrase.delete(0,tk.END)

#just testing for a help dialog
def show_help():
    help_text = (
        "Instructions:\n"
        "- Click on the pre-made buttons to add phrases in the text box.\n"
        "- Use 'Speak' to vocalize the text.\n"
        "- Use 'Add Custom Phrase' to create and add your own phrases.\n"
        "- Click on File->Settings to change the settings of the vocalised text.\n"
        "- There are two different tabs, so try using both to practice.\n"
    )
    tk.messagebox.showinfo("Help", help_text)

def record_and_display_speech():
    text=stt.record_speech()
    if text:
        spoken_text.delete(0, tk.END)
        spoken_text.insert(0, text)

        primary_str=accuracy_check.get().lower()
        secondary_str=spoken_text.get().lower()

        user_perc = pf.calc_accuracy(primary_str,secondary_str)
        app_mess = tk.Label(tab2, text="You got:"+str(user_perc)+"% "+pf.acc_message(user_perc), font=("Arial", 16, "italic"))
        app_mess.pack()

        stt.output_speech(text)

    else:
        spoken_text.delete(0, tk.END)
        spoken_text.insert(0, "Speech recognition failed.")


#title on tab2
title=tk.Label(tab2,text="Accuracy Checker",font=("Arial",24,"bold"))
title.pack(padx=50,pady=50)

#title on tab1
title=tk.Label(tab1,text="Enter text and press 'Speak' to hear it!",font=("Arial",24,"bold"))
title.pack()

#text boxes
entry=tk.Entry(tab1,
               font=("Helvetica",24),
               fg="black",
               bg="white")
entry.pack(side=tk.TOP,expand=True,fill="x",padx=15,pady=15)

#for custom phrases
title=tk.Label(tab1,text="Add Your Own Custom Phrases!",font=("Arial",24,"bold"))
title.pack()

custom_phrase=tk.Entry(
    tab1,
    font=("Helvetica",16),
    fg="black",
    bg="yellow"
)
custom_phrase.pack(side=tk.TOP,padx=15,pady=15)

#tab1 custom phrase title
save_button =tk.Button(tab1, text="Add Custom Phrase", command=save_custom_phrase)
save_button.pack(pady=5)

#for accuracy checker
input_text=tk.Label(tab2,text="Input a phrase or word in here and then try speaking it:",font=("Arial",18,"italic"))
input_text.pack()

accuracy_check=tk.Entry(
    tab2,
    font=("Helvetica",20),
    fg="#228B22",
    bg="white"
)
accuracy_check.pack()

#for user's spoken text
user_text=tk.Label(tab2,text="This is your spoken text:",font=("Arial",16,"italic"))
user_text.pack()

spoken_text=tk.Entry(
    tab2,
    font=("Helvetica",16),
    fg="#054fb9",
    bg="white"
)
spoken_text.pack()


#buttons
speak_in_mic=tk.Button(tab2,text="Speak In Mic",command=record_and_display_speech)
speak_in_mic.pack(side=tk.BOTTOM,padx=10,pady=10)

speak_button=tk.Button(tab1,text="Speak Out",command=speak_out)
speak_button.pack(side=tk.BOTTOM,padx=10,pady=10)

clear_button=tk.Button(tab1,text="Clear \n(Clears both dialog boxes!)",command=clear)
clear_button.pack(side=tk.BOTTOM,padx=10,pady=10)

help_button=tk.Button(tab1,text="Click to see instructions!",command=show_help)
help_button.pack(pady=20)

# frame for the phrase buttons
phrases_frame=tk.Frame(tab1)
phrases_frame.pack(side=tk.TOP,anchor=tk.CENTER)

phrases=["Hello", "How are you?", "Yes", "No", "Thank You", "Help"]
for cu_phrase in phrases:
    phrases_button=tk.Button(phrases_frame,text=cu_phrase,command=lambda p=cu_phrase: add_phrase(p))
    phrases_button.pack(side=tk.LEFT,padx=5,pady=5)


window.mainloop()

if __name__ == "__main__":
    print("am so tired")