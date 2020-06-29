"""
-[x] add .get() to the tk.Entry()
-[x] add activity days input from drowpdown menu
-[ ] implement macroestimator to convert input into the class args
-[ ] add LBM, TDEE, MACROS print at the end
"""

import tkinter as tk
from tkinter import ttk
from MacroEstimator import macroCaloriesEstimator as mce

def show_entry_fields():
    print("Weight: {}\tHeight: {}\nBody fat: {}\tAge: {}".format(e1.get(), e2.get(), e3.get(), e4.get()))

master = tk.Tk()
# entries = ['Weight', 'Height', 'Body fat %', 'Age', 'Gender', 'Goal']
tk.Label(master, text='Weight').grid(row=0, column=0)
tk.Label(master, text='Height').grid(row=0, column=2)
tk.Label(master, text='Body fat').grid(row=1, column=0)
tk.Label(master, text='Age').grid(row=1, column=2)
tk.Label(master, text='Gender').grid(row=2, column=0)
tk.Label(master, text='Exercise').grid(row=2, column=2)
tk.Label(master, text='Goal').grid(row=3, column=0)
tk.Label(master, text='Physical Job').grid(row=3, column=2)

e1 = tk.Entry(master, width=15)
e2 = tk.Entry(master, width=15)
e3 = tk.Entry(master, width=15)
e4 = tk.Entry(master, width=15)
GenderOptions = ttk.Combobox(master, width=13)
ExerciseOptions = ttk.Combobox(master, width=13)
DietOptions = ttk.Combobox(master, width=13)
JobOptions = ttk.Combobox(master, width=13)

def collect_input():
    return e1.get(), e2.get(), e3.get(), e4.get(), GenderOptions.get()

def collect_goal_activity():
    return DietOptions.get()

def something():
    sms = float(e1.get()) / 2.2
    return tk.Label(master, text=str(sms) + ' lbs').grid(row=4, column=1)
    

# Adding combobox drop down list 
GenderOptions['values'] = ('Male', 'Female')
DietOptions['values'] = ('Bulking', 'Cutting', 'Maintaning')
ExerciseOptions['values'] = ('Occasionally', '1 to 2 Day', '3 to 4 days', '4 to 5 days', '6 to 7 days')
JobOptions['values'] = ('Yes', 'No')

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=0, column=3)
e4.grid(row=1, column=3)
GenderOptions.grid(row=2, column=1)
ExerciseOptions.grid(row=2, column=3)
DietOptions.grid(row=3, column=1)
JobOptions.grid(row=3, column=3)

tk.Button(master, 
        text='Calculate', fg='darkgreen',
        command=something).place(relx=.41, rely=0.65, anchor="center")

tk.Button(master, 
        text='Reset', fg='darkred',
        command=master.quit).place(relx=.63, rely=0.65, anchor="center")

tk.Label(master, text='============= Results =============', fg='blue', font=("Courier", 10)).place(relx=.5, rely=0.85, anchor="center")

# Results
tk.Label(master, text='TDEE').grid(row=5, column=0)



master.grid_rowconfigure(4, minsize=70)
tk.mainloop()
