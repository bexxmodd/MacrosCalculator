"""
-[x] add .get() to the tk.Entry()
-[x] add activity days input from drowpdown menu
-[x] implement macroestimator to convert input into the class args
-[x] add LBM, TDEE, MACROS print at the end
-[ ] add when you hoover pointer over TDE/LBM gives info
-[ ] make reset button work
"""

import tkinter as tk
from tkinter import ttk
from MacroEstimator import macroCaloriesEstimator as mce

def show_entry_fields():
    print("Weight: {}\tHeight: {}\nBody fat: {}\tAge: {}".format(e1.get(), e2.get(), e3.get(), e4.get()))

master = tk.Tk()
# entries = ['Weight', 'Height', 'Body fat %', 'Age', 'Gender', 'Goal']
tk.Label(master, text='Weight (lbs)').place(x=10, y=10)
tk.Label(master, text='Height (feet)').place(x=260, y=10)
tk.Label(master, text='Body fat %').place(x=10, y=40)
tk.Label(master, text='Age (years)').place(x=260, y=40)
tk.Label(master, text='Gender').place(x=10, y=70)
tk.Label(master, text='Exercise').place(x=260, y=70)
tk.Label(master, text='Goal').place(x=10, y=100)
tk.Label(master, text='Physical Job').place(x=260, y=100)

weight = tk.Entry(master, width=15)
height = tk.Entry(master, width=15)
fat = tk.Entry(master, width=15)
age = tk.Entry(master, width=15)
GenderOptions = ttk.Combobox(master, width=13)
ExerciseOptions = ttk.Combobox(master, width=13)
DietOptions = ttk.Combobox(master, width=13)
JobOptions = ttk.Combobox(master, width=13)

# Collect user input
def get_bio():
    return weight.get(), height.get(), fat.get(), age.get(), GenderOptions.get()

def get_activites():
    return ExerciseOptions.get(), JobOptions.get()

def get_goal():
    return DietOptions.get()

# Calculate
def create_user():
    weight, height, body_fat, age, gender = get_bio()
    return mce(float(weight), float(height), float(body_fat), int(age), gender)

def calcualte_lbm():
    user = create_user()
    return user.lean_body_mass()

def calculate_tdee():
    user = create_user()
    exer, job = get_activites()
    return user.total_daily_energy_expenditure(exer, job)

def calculate_macros():
    user = create_user()
    diet = get_goal()
    return user.print_macros(diet)

# Create return Labels
def final_output():
    lbm = round(calcualte_lbm(), 2)
    tdee = round(calculate_tdee(), 2)
    macros = calculate_macros()
    return tk.Label(master, text=str(lbm) + ' lbs', font='bold', fg='darkred',
            anchor="e", borderwidth=2, relief='ridge').place(x=150, y=230), \
        tk.Label(master, text=str(tdee) + ' kcal', font='bold', fg='darkred',
            anchor="e", borderwidth=2, relief='ridge').place(x=150, y=260), \
        tk.Label(master, text=macros, font='bold', fg='darkred',
            anchor="e", justify='left', borderwidth=2, relief='ridge').place(x=150, y=290)
    


# Adding combobox drop down list 
GenderOptions['values'] = ('Male', 'Female')
DietOptions['values'] = ('Bulking', 'Cutting', 'Maintaining')
ExerciseOptions['values'] = ('Occasionally', '1 to 2 Day', '3 to 4 days', '5 to 7 days')
JobOptions['values'] = ('Yes', 'No')

weight.place(x=100, y=10)
height.place(x=350, y=10)
fat.place(x=100, y=40)
age.place(x=350, y=40)
GenderOptions.place(x=100, y=70)
ExerciseOptions.place(x=350, y=70)
DietOptions.place(x=100, y=100)
JobOptions.place(x=350, y=100)

tk.Button(master, 
        text='Calculate', fg='darkgreen',
        command=final_output).place(x=140, y=150)

tk.Button(master, 
        text='Reset',
        command=master.quit).place(x=230, y=150)

tk.Button(master, 
        text='Exit',
        command=master.quit).place(x=296, y=150)

tk.Label(master, text='=============== Results ===============', fg='blue', font=("Courier", 10)).place(x=80, y=200)

master.grid_rowconfigure(4, minsize=70)

# Results
tk.Label(master, text='LMB:').place(x=10, y=230)
tk.Label(master, text='TDEE:').place(x=10, y=260)
tk.Label(master, text='Daily Macros:').place(x=10, y=290)

master.geometry('500x390+20+20')




tk.mainloop()
