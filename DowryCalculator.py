import tkinter as tk
from tkinter import ttk, messagebox
import random

# Random Messages
messages = [
    "💡 Marriage is built on love, not price tags! 💡",
    "💡 True wealth is a happy marriage, not money! 💡",
    "💡 Dowry ruins relationships before they start! 💡",
    "💡 Respect and love are the real assets in marriage! 💡",
    "💡 Say NO to dowry, say YES to happiness! 💡"
]

def calculate_dowry():
    try:
        education = education_var.get()
        salary = int(salary_var.get())
        job_sector = job_var.get()
        car_ownership = car_var.get()
        family_status = family_var.get()
        looks = looks_var.get()

        base_dowry = 50000  # Basic dowry amount

        education_factor = {
            "10th Pass": 0.5, "12th Pass": 0.8, "Graduate": 1.2,
            "Postgraduate": 1.5, "Doctorate": 2.0
        }

        job_factor = {
            "Government": 2.5, "Private": 1.8, "Business": 2.0,
            "Freelancer": 1.2, "Unemployed": 0.5
        }

        car_bonus = {
            "No Car": 1.0, "Hatchback": 1.2, "Sedan": 1.5,
            "SUV": 2.0, "Luxury Car": 3.0
        }

        family_factor = {
            "Middle Class": 1.0, "Upper Middle Class": 1.5,
            "Rich": 2.0, "Ultra Rich": 3.0
        }

        looks_factor = {
            "Average": 1.0, "Good Looking": 1.5, "Very Handsome": 2.0,
            "Greek God": 3.0
        }

        # **Dowry Calculation Formula**
        dowry = base_dowry * education_factor.get(education, 1) * job_factor.get(job_sector, 1)
        dowry += salary * 2
        dowry *= car_bonus.get(car_ownership, 1)
        dowry *= family_factor.get(family_status, 1)
        dowry *= looks_factor.get(looks, 1)

        dowry_label.config(text=f"💰 Expected Dowry: ₹{int(dowry)} 💰")
        moral_label.config(text=random.choice(messages))  # Random Message

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid salary amount!")

# **GUI Setup**
root = tk.Tk()
root.title("Dowry Calculator 😂🔥")
root.geometry("450x600")
root.config(bg="lightblue")

# **Heading**
title_label = tk.Label(root, text="Dowry Calculator 😂🔥", font=("Arial", 16, "bold"), bg="lightblue")
title_label.pack(pady=10)

# **Dropdown Variables**
education_var = tk.StringVar(value="Graduate")
job_var = tk.StringVar(value="Private")
car_var = tk.StringVar(value="No Car")
family_var = tk.StringVar(value="Middle Class")
looks_var = tk.StringVar(value="Average")
salary_var = tk.StringVar()

# **Dropdown Menus**
ttk.Label(root, text="Education Level:", background="lightblue").pack(pady=5)
ttk.Combobox(root, textvariable=education_var, values=["10th Pass", "12th Pass", "Graduate", "Postgraduate", "Doctorate"]).pack()

ttk.Label(root, text="Salary (INR):", background="lightblue").pack(pady=5)
salary_entry = ttk.Entry(root, textvariable=salary_var)
salary_entry.pack()

ttk.Label(root, text="Job Sector:", background="lightblue").pack(pady=5)
ttk.Combobox(root, textvariable=job_var, values=["Government", "Private", "Business", "Freelancer", "Unemployed"]).pack()

ttk.Label(root, text="Car Ownership:", background="lightblue").pack(pady=5)
ttk.Combobox(root, textvariable=car_var, values=["No Car", "Hatchback", "Sedan", "SUV", "Luxury Car"]).pack()

ttk.Label(root, text="Family Status:", background="lightblue").pack(pady=5)
ttk.Combobox(root, textvariable=family_var, values=["Middle Class", "Upper Middle Class", "Rich", "Ultra Rich"]).pack()

ttk.Label(root, text="Looks:", background="lightblue").pack(pady=5)
ttk.Combobox(root, textvariable=looks_var, values=["Average", "Good Looking", "Very Handsome", "Greek God"]).pack()

# **Calculate Button**
calc_button = ttk.Button(root, text="Calculate Dowry 💰", command=calculate_dowry)
calc_button.pack(pady=10)

# **Result Labels**
dowry_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="lightblue")
dowry_label.pack(pady=10)

moral_label = tk.Label(root, text="", font=("Arial", 12, "italic"), fg="red", bg="lightblue")
moral_label.pack(pady=10)

root.mainloop()
