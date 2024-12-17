from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
import tkinter as tk
from tkinter import messagebox


window = Tk()
window.geometry("600x550")
window.title("Alien Invader HQ Control Panel")

def spaceship_color():
    color = colorchooser.askcolor()
    spaceship_color_display.config(bg=color[1])
    console_label.config(text="Color changed!")

def send_message():
    message = message_alien_pilots_text.get(1.0, END)
    print(f"Alien Message: {message}")
    console_label.config(text="Message sent!")

def file_upload():
    filename = filedialog.askopenfilename(title="Open File", filetypes=[("Text Files", "*.txt")], defaultextension=".txt")

    if filename:
        with open(filename, "r") as file:
            content = file.read()
            print(content)
            console_label.config(text="File uploaded to console.")

def launch_plan():
    selected = invasion_list.get(tk.ACTIVE)
    resp = messagebox.askyesno("Confirm Launch", f"Are you sure you want to launch {selected}?")
    if resp:
        messagebox.showinfo("Confirm Launch", "Plan Launched!")
    else:
        messagebox.showinfo("Confirm Launch", "Plan failed! Try again.")
    console_label.config(text=f"{selected} launched!")
    

logo = PhotoImage(file=r"images/alien_updated.png")

top_frame = Frame(window, bg="green")
top_frame_label = Label(top_frame, image=logo).pack()
top_frame.pack(anchor="n")

middle_frame = Frame(window)
middle_frame.pack()

spaceship_color_display = Label(middle_frame, bg='grey', padx=80, pady=25)
spaceship_color_display.grid(row=0, column=0)

color_changer = Button(middle_frame, text="Change Spaceship Color", command=spaceship_color)
color_changer.grid(row=0, column=0)


message_alien_pilots_text = Text(middle_frame, width=50, height=5)
message_alien_pilots_text.grid(row=0, column=1)

send_message_button = Button(middle_frame, text="Send Message", command=send_message)
send_message_button.grid(row=1, column=1)

upload_file_button = Button(middle_frame, text="Upload Secret File", command=file_upload)

upload_file_button.grid(row=2, column=0, pady=20)

select_invasion_text = Label(middle_frame, text="Select Invasion Plan:")

select_invasion_text.grid(row=2, column=1)

invasion_list = Listbox(middle_frame, width=25, height=8)

invasion_list.insert(1, "Plan A: Earth Takeover")
invasion_list.insert(2, "Plan B: Moon Domination")
invasion_list.insert(3, "Plan C: Mars Colinization")

invasion_list.grid(row=3, column=1)

launch_plan_button = Button(middle_frame, text="Launch Plan", command=launch_plan)

launch_plan_button.grid(row=4, column=1)


lower_frame = Frame(window, bg="green", highlightbackground="black", highlightthickness=1)

console_label = Label(lower_frame, text="Empty", width=550)
console_label.pack()

lower_frame.pack()


window.mainloop()