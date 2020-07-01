"""
-[ ] Turn script into functional form
"""

import tkinter as tk
import webbrowser
from tkinter import ttk
from MacroEstimator import macroCaloriesEstimator as mce
from ToolTip import CreateToolTip

master = tk.Tk()
master.title("Macros Calculator")

tk.Label(master, text='Weight (lbs)', font='verdana 10').place(x=10, y=10)
tk.Label(master, text='Height (feet)', font='verdana 10').place(x=260, y=10)
tk.Label(master, text='Body fat %', font='verdana 10').place(x=10, y=40)
tk.Label(master, text='Age (years)', font='verdana 10').place(x=260, y=40)
tk.Label(master, text='Gender', font='verdana 10').place(x=10, y=70)
tk.Label(master, text='Exercise', font='verdana 10').place(x=260, y=70)
tk.Label(master, text='Goal', font='verdana 10').place(x=10, y=100)
tk.Label(master, text='Physical Job', font='verdana 10').place(x=260, y=100)

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
    exer, job = get_activites()
    user = create_user()
    diet = get_goal()
    return user.print_macros(diet, exer, job)

# Create return Labels
def final_output():
    lbm = round(calcualte_lbm(), 2)
    tdee = round(calculate_tdee(), 2)
    macros = calculate_macros()
    return tk.Label(master, text=str(lbm) + ' lbs', font='verdana 11 bold', fg='darkred',
            anchor="e", borderwidth=2, relief='ridge').place(x=150, y=230), \
        tk.Label(master, text=str(tdee) + ' kcal', font='verdana 11 bold', fg='darkred',
            anchor="e", borderwidth=2, relief='ridge').place(x=150, y=260), \
        tk.Label(master, text=macros, font='verdana 11 bold', fg='darkred',
            anchor="e", justify='left', borderwidth=2, relief='ridge').place(x=150, y=290)

def reset_button():
    weight.delete(0, 'end')
    height.delete(0, 'end')
    fat.delete(0, 'end')
    age.delete(0, 'end')
    GenderOptions.delete(0, 'end')
    ExerciseOptions.delete(0, 'end')
    DietOptions.delete(0, 'end')
    JobOptions.delete(0, 'end')


# Adding combobox drop down list 
GenderOptions['values'] = ('Male', 'Female')
DietOptions['values'] = ('Gain', 'Lose', 'Maintain')
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
        text='Calculate', fg='darkgreen', font='verdana 10',
        command=final_output).place(x=140, y=150)

tk.Button(master, 
        text='Reset', font='verdana 10',
        command=reset_button).place(x=230, y=150)

tk.Button(master, 
        text='Exit', font='verdana 10',
        command=master.quit).place(x=296, y=150)

tk.Label(master, text='========================= Results =========================', fg='blue', font=("Courier", 10)).place(relx=0.5, y=200, anchor='center')

master.grid_rowconfigure(4, minsize=70)

# Results
lbm = tk.Label(master, text='LMB:')
lbm.place(x=10, y=230)

tdee = tk.Label(master, text='TDEE:')
tdee.place(x=10, y=260)

macros = tk.Label(master, text='Daily Macros:')
macros.place(x=10, y=290)

# Hoover the pointer over the results
CreateToolTip(lbm, text='Lean Body Mass (LBM) is a part of body composition that is defined\nas the difference between total body weight and body fat weight.')
CreateToolTip(tdee, text='Total Daily Energy Expenditures (TDEE) is an estimation of how\ncalories burned per day when exercise is taken into account.')
CreateToolTip(macros, text='Portion of each macro element in the daily diet')

# Link to github

def callback(url):
    webbrowser.open_new('https://github.com/bexxmodd/CaloriesCalc')

github_logo = tk.PhotoImage(file="small-github.png")
bexxmodd = tk.Label(master, image=github_logo, cursor="hand2")
bexxmodd.place(relx=0.5, y=400, anchor='center')
bexxmodd.bind("<Button-1>", callback)


# Gets the requested values of the height and widht.
windowWidth = master.winfo_reqwidth()
windowHeight = master.winfo_reqheight()

# Gets both half the screen width/height and window width/height
positionRight = int(master.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(master.winfo_screenheight()/2 - windowHeight/2)

master.geometry(f'500x420+{positionRight}+{positionDown}')
master.iconphoto(False, tk.PhotoImage(file='nutrition.png'))

tk.mainloop()
