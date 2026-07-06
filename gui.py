from tkinter import *
from tkinter import messagebox

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from database import *
from security import hash_password
from datetime import datetime

CURRENT_USER = ""

# =========================
# WINDOW
# =========================

window = ttk.Window(themename="cyborg")

window.title("TODO APP v10.0")

window.geometry("1500x850")

window.minsize(1200, 700)

window.config(bg="#0f172a")

# =========================
# LOGIN FRAME
# =========================

login_frame = Frame(
    window,
    bg="#020617"
)

login_frame.pack(fill=BOTH, expand=True)

title = Label(
    login_frame,
    text="TODO APP v11.0",
    bg="#020617",
    fg="#00ffff",
    font=("Arial", 34, "bold")
)

title.pack(pady=30)

username_entry = Entry(
    login_frame,
    width=30,
    font=("Arial", 14)
)

username_entry.pack(pady=10)

password_entry = Entry(
    login_frame,
    width=30,
    show="*",
    font=("Arial", 14)
)

password_entry.pack(pady=10)

# =========================
# MAIN APP
# =========================

main_frame = Frame(
    window,
    bg="#0f172a"
)

sidebar = Frame(
    main_frame,
    bg="#020617",
    width=250
)

sidebar.pack(
    side=LEFT,
    fill=Y
)

sidebar.pack_propagate(False)

logo = Label(
    sidebar,
    text="TODO\nAPP",
    bg="#020617",
    fg="#00ffff",
    font=("Arial", 32, "bold")
)

logo.pack(pady=30)

user_label = Label(
    sidebar,
    text="USER",
    bg="#020617",
    fg="white",
    font=("Arial", 16, "bold")
)

user_label.pack(pady=20)

clock_label = Label(
    sidebar,
    bg="#020617",
    fg="#00ff99",
    font=("Consolas", 22, "bold")
)

clock_label.pack(pady=30)

stats_label = Label(
    sidebar,
    text="TASKS\n0",
    bg="#020617",
    fg="#00ffff",
    font=("Arial", 24, "bold")
)

stats_label.pack(pady=20)

# =========================
# TASK FORM
# =========================

form_frame = Frame(
    main_frame,
    bg="#0f172a"
)

form_frame.pack(
    pady=20,
    padx=20,
    anchor="nw"
)

Label(
    form_frame,
    text="Task",
    bg="#0f172a",
    fg="white",
    font=("Arial", 12)
).grid(row=0, column=0, padx=10)

task_entry = Entry(
    form_frame,
    width=30,
    font=("Arial", 12)
)

task_entry.grid(row=0, column=1)

Label(
    form_frame,
    text="Priority",
    bg="#0f172a",
    fg="white",
    font=("Arial", 12)
).grid(row=1, column=0, padx=10)

priority_combo = ttk.Combobox(
    form_frame,
    values=["Low", "Medium", "High"],
    width=27
)

priority_combo.grid(row=1, column=1)

Label(
    form_frame,
    text="Category",
    bg="#0f172a",
    fg="white",
    font=("Arial", 12)
).grid(row=2, column=0, padx=10)

category_entry = Entry(
    form_frame,
    width=30,
    font=("Arial", 12)
)

category_entry.grid(row=2, column=1)

Label(
    form_frame,
    text="Due Date",
    bg="#0f172a",
    fg="white",
    font=("Arial", 12)
).grid(row=3, column=0, padx=10)

due_entry = Entry(
    form_frame,
    width=30,
    font=("Arial", 12)
)

due_entry.grid(row=3, column=1)

style = ttk.Style()

style.configure(
    "Treeview",
    rowheight=35,
    font=("Consolas", 11)
)

style.configure(
    "Treeview.Heading",
    font=("Arial", 12, "bold")
)

# =========================
# TABLE
# =========================

columns = (
    "ID",
    "Task",
    "Status",
    "Priority",
    "Category",
    "Created",
    "Due"
)

table = ttk.Treeview(
    main_frame,
    columns=columns,
    show="headings",
    height=15
)

for col in columns:

    table.heading(col, text=col)

    table.column(col, width=150)

table.pack(pady=20)

# =========================
# FUNCTIONS
# =========================

def refresh_tasks():

    for item in table.get_children():

        table.delete(item)

    tasks = load_tasks(CURRENT_USER)
    
    stats_label.config(
    text=f"TASKS\n{len(tasks)}"
    )

    for task in tasks:

        table.insert(
            "",
            END,
            values=(
                task[0],
                task[2],
                task[3],
                task[4],
                task[5],
                task[6],
                task[7]
            )
        )

def add_new_task():

    task = task_entry.get()

    priority = priority_combo.get()

    category = category_entry.get()

    due = due_entry.get()

    created = "2026"

    add_task(
        CURRENT_USER,
        task,
        "Pending",
        priority,
        category,
        created,
        due
    )

    refresh_tasks()

    messagebox.showinfo(
        "Success",
        "Task Added"
    )

def delete_selected():

    selected = table.focus()

    if not selected:

        return

    values = table.item(selected, "values")

    task_id = values[0]

    delete_task(task_id)

    refresh_tasks()

def complete_selected():

    selected = table.focus()

    if not selected:

        return

    values = table.item(selected, "values")

    task_id = values[0]

    complete_task(task_id)

    refresh_tasks()

# =========================
# BUTTONS
# =========================

button_frame = Frame(
    main_frame,
    bg="#0f172a"
)

button_frame.pack(pady=10)

ttk.Button(
    button_frame,
    text="➕ Add Task",
    command=add_new_task,
    bootstyle="success-outline",
    width=20
).pack(side=LEFT, padx=10)

ttk.Button(
    button_frame,
    text="✅ Complete",
    command=complete_selected,
    bootstyle="info-outline",
    width=20
).pack(side=LEFT, padx=10)

ttk.Button(
    button_frame,
    text="❌ Delete",
    command=delete_selected,
    bootstyle="danger-outline",
    width=20
).pack(side=LEFT, padx=10)

ttk.Button(
    button_frame,
    text="🔄 Refresh",
    command=refresh_tasks,
    bootstyle="warning-outline",
    width=20
).pack(side=LEFT, padx=10)

# =========================
# LOGIN FUNCTIONS
# =========================

def login():

    global CURRENT_USER

    username = username_entry.get()

    password = password_entry.get()

    hashed = hash_password(password)

    data = login_user(
        username,
        hashed
    )

    if data:

        CURRENT_USER = username

        login_frame.pack_forget()

        main_frame.pack(fill=BOTH, expand=True)

        refresh_tasks()

    else:

        messagebox.showerror(
            "Error",
            "Invalid Login"
        )

def register():

    username = username_entry.get()

    password = password_entry.get()

    hashed = hash_password(password)

    success = register_user(
        username,
        hashed
    )

    if success:

        messagebox.showinfo(
            "Success",
            "Account Created"
        )

    else:

        messagebox.showerror(
            "Error",
            "Username Exists"
        )

# =========================
# LOGIN BUTTONS
# =========================

Button(
    login_frame,
    text="Login",
    command=login,
    bg="green",
    fg="white",
    width=20
).pack(pady=10)

Button(
    login_frame,
    text="Register",
    command=register,
    bg="blue",
    fg="white",
    width=20
).pack(pady=10)

# =========================
# START
# =========================

def update_clock():

    now = datetime.now().strftime("%H:%M:%S")

    clock_label.config(text=now)

    window.after(1000, update_clock)
    
update_clock()
    
window.mainloop()