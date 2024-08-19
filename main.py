import tkinter as tk
from tkinter import messagebox
import pickle
from PIL import Image, ImageTk

def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open("tasks.pkl", "wb") as task_file:
        pickle.dump(tasks, task_file)
    messagebox.showinfo("Info", "Tasks saved successfully.")

def load_tasks():
    try:
        with open("tasks.pkl", "rb") as task_file:
            tasks = pickle.load(task_file)
            task_listbox.delete(0, tk.END)
            for task in tasks:
                task_listbox.insert(tk.END, task)
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No saved tasks found.")

root = tk.Tk()
root.title("To-Do List")

checklist_image_original = Image.open("images/checklist.png")
checklist_image_resized = checklist_image_original.resize((50, 50), Image.ANTIALIAS)
checklist_image = ImageTk.PhotoImage(checklist_image_resized)

checklist_label = tk.Label(root, image=checklist_image)

task_entry = tk.Entry(root, width=30)

add_task_button = tk.Button(root, text="Add Task", command=add_task)

task_listbox = tk.Listbox(root, width=50, height=15)

button_frame = tk.Frame(root)

icon_width = 40
icon_height = 40

delete_image_original = Image.open("images/delete.png")
delete_image_resized = delete_image_original.resize((icon_width, icon_height), Image.ANTIALIAS)
delete_image = ImageTk.PhotoImage(delete_image_resized)
delete_task_button = tk.Button(button_frame, image=delete_image, command=delete_task)
delete_task_button.pack(side=tk.LEFT, padx=5)

save_image_original = Image.open("images/save.png")
save_image_resized = save_image_original.resize((icon_width, icon_height), Image.ANTIALIAS)
save_image = ImageTk.PhotoImage(save_image_resized)

save_tasks_button = tk.Button(button_frame, image=save_image, command=save_tasks)
save_tasks_button.pack(side=tk.LEFT, padx=5)

checklist_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.NW)
task_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
add_task_button.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
button_frame.grid(row=3, column=0, columnspan=2, pady=5)

load_tasks()

root.mainloop()
