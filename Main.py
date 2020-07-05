import tkinter as tk
import webbrowser

from tkinter import ttk
from MacroEstimator import macroCaloriesEstimator as mce
from ToolTip import CreateToolTip

# Create the master frame,
master = tk.Tk()
master.title("Macros Calculator")

labels = [
    'Weight (lbs)',
    'Height (feet)',
    'Body Fat %',
    'Age (years)',
    'Gender',
    'Exercise',
    'Goal',
    'Physical Job',
]

# Create the labels for the user input.
y_axis1 = 10
y_axis2 = 10

for label in labels[:4]:
    tk.Label(master, text=label, font='verdana 10').place(x=10, y=y_axis1)
    y_axis1 += 30

for label in labels[4:]:
    tk.Label(master, text=label, font='verdana 10').place(x=260, y=y_axis2)
    y_axis2 += 30

# Create input frames.
weight = tk.Entry(master, width=15)
height = tk.Entry(master, width=15)
fat = tk.Entry(master, width=15)
age = tk.Entry(master, width=15)
gender = ttk.Combobox(master, width=13)
exercise = ttk.Combobox(master, width=13)
diet = ttk.Combobox(master, width=13)
job = ttk.Combobox(master, width=13)

# Adding combobox drop down list 
gender['values'] = ('Male', 'Female')
diet['values'] = ('Gain', 'Lose', 'Maintain')
exercise['values'] = ('Occasionally', '1 to 2 Day', '3 to 4 days', '5 to 7 days')
job['values'] = ('Yes', 'No')

# Place input frames.
entry_points = [weight, height, fat, age, gender, exercise, diet, job]

y_axis1 = 10
y_axis2 = 10

for entry in entry_points[:4]:
    entry.place(x=100, y=y_axis1)
    y_axis1 += 30

for entry in entry_points[4:]:
    entry.place(x=350, y=y_axis2)
    y_axis2 += 30


"""Collect the user input"""
# Get bio
def get_bio():
    return {'weight': float(weight.get()), 'height': float(height.get()), 'fat': float(fat.get()), 'age': float(age.get())}

def get_gender():
    return gender.get()

def get_activites():
    return exercise.get(), job.get(), diet.get()


"""Make calculations from MacroEstimator"""
# Instantiate macroCaloriesEstimator class
def create_user():
    user_bio = get_bio()
    for i in user_bio.values():
        if i < 0:
            raise ValueError ('No negative values')
    return mce(user_bio["weight"], user_bio["height"], user_bio["fat"], user_bio["age"], get_gender())

def calcualte_lbm():
    return create_user().lean_body_mass()

def calculate_tdee():
    exer, job = get_activites()[:2]
    return create_user().total_daily_energy_expenditure(exer, job)

def calculate_macros():
    exer, job, diet = get_activites() 
    return create_user().print_macros(diet, exer, job)

# Return calculated results to the users
def final_output():
    lbm = round(calcualte_lbm(), 2)
    tdee = round(calculate_tdee(), 2)
    macros = calculate_macros()
    global results # Create a global variable of output labels to make it reusable
    results = [
        tk.Label(master, text=str(lbm) + ' lbs', font='verdana 11 bold', fg='darkred',
            anchor="e", borderwidth=2, relief='ridge'),
        tk.Label(master, text=str(tdee) + ' kcal', font='verdana 11 bold', fg='darkred',
            anchor="e", borderwidth=2, relief='ridge'),
        tk.Label(master, text=macros, font='verdana 11 bold', fg='darkred',
            anchor="e", justify='left', borderwidth=2, relief='ridge')
        ]
    y_axis = 230
    # Place output labels
    for i in results:
        i.place(x=150, y=y_axis)
        y_axis += 30

# Erase the user intput and output
def reset_button():
    for i in results:   # Erase output results
        i.place_forget()
    for entry in entry_points:  # Erase data entry points
        entry.delete(0, 'end')

# Error message
def error_msg():
    return tk.messagebox.showerror(title='ValueError', message='No negative values allowed')

"""Buttons for calculation, reset, and exit"""
tk.Button(master, 
        text='Calculate', fg='darkgreen', font='verdana 10',
        command=final_output).place(x=140, y=150)

tk.Button(master, 
        text='Reset', font='verdana 10',
        command=reset_button).place(x=230, y=150)

tk.Button(master, 
        text='Exit', font='verdana 10',
        command=master.quit).place(x=296, y=150)

tk.Label(master, text='Results',
        fg='blue', font=("Courier", 10)).place(relx=0.5, y=205, anchor='center')
tk.Frame(master, height=1, background='blue').pack(expand='yes', fill='x', padx=10) 

"""Display final results"""
# Results
results = [
    tk.Label(master, text='LMB:'),
    tk.Label(master, text='TDEE:'),
    tk.Label(master, text='Daily Macros:')
]

y_axis = 230
for result in results:
    result.place(x=10, y=y_axis)
    y_axis += 30

# Hoover the pointer over the results
CreateToolTip(results[0], text='Lean Body Mass (LBM) is a part of body composition that is defined\nas the difference between total body weight and body fat weight.')
CreateToolTip(results[1], text='Total Daily Energy Expenditures (TDEE) is an estimation of how\ncalories burned per day when exercise is taken into account.')
CreateToolTip(results[2], text='Portion of each macro element in the daily diet')

# Link to github repo with github icon
def callback(url):
    webbrowser.open_new('https://github.com/bexxmodd/CaloriesCalc')

# Link to the github repo with github logo
github_logo = tk.PhotoImage(file="./img/small-github.png")

bexxmodd = tk.Label(master, image=github_logo, cursor="hand2")
bexxmodd.place(relx=0.5, y=400, anchor='center')
bexxmodd.bind("<Button-1>", callback)

# Gets the requested values of the height and widht.
windowWidth = master.winfo_reqwidth()
windowHeight = master.winfo_reqheight()

# Gets both half the screen width/height and window width/height
positionRight = int(master.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(master.winfo_screenheight()/2 - windowHeight/2)

# Shape of the main frame and the icon
master.geometry(f'500x420+{positionRight}+{positionDown}')
master.iconphoto(False, tk.PhotoImage(file='./img/nutrition.png'))

tk.mainloop()
