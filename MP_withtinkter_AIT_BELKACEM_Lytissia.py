# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 17:59:09 2025

@author: mourade
"""


#  FOOD LABEL ANALYZER (WITH Tkinter )
#  Author: Lytissia Ait Belkacem
#  Description:
#     A simple program with a graphical interface that analyzes
#     nutrition facts from a packaged food label and compares them
#     to daily recommended values for an average adult.


import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Reference Nutrition Guidelines 
nutrition_guidelines = {
    "Calories (kcal)": 2000,
    "Protein (g)": 50,
    "Fat (g)": 70,
    "Sugar (g)": 50,
    "Fiber (g)": 25,
    "Vitamin C (mg)": 90
}

# Function to Analyze Nutrition
def analyze():
    try:
        # Get data from entries
        user_data = {}
        for nutrient, entry in entries.items():
            value = float(entry.get())
            user_data[nutrient] = value

        # Calculate percentages
        percentages = {}
        for nutrient, value in user_data.items():
            ref = nutrition_guidelines[nutrient]
            pct = (value / ref) * 100
            percentages[nutrient] = pct

        # Make a recommendation
        sugar_pct = percentages["Sugar (g)"]
        fat_pct = percentages["Fat (g)"]
        cal_pct = percentages["Calories (kcal)"]

        if sugar_pct > 50 or fat_pct > 50 or cal_pct > 50:
            recommendation = "Unhealthy"
        elif sugar_pct > 30 or fat_pct > 30 or cal_pct > 30:
            recommendation = "Eat in Moderation"
        else:
            recommendation = "Healthy"

        # Show results
        result_text = "Nutrition Analysis:\n\n"
        for nutrient, pct in percentages.items():
            result_text += f"{nutrient}: {pct:.1f}% of daily need\n"
        result_text += f"\nRecommendation: {recommendation}"

        result_label.config(text=result_text)

    except ValueError:
        messagebox.showerror("Error", "Please enter numbers only.")

# Function to Show Graph 
def show_graph():
    try:
        nutrients = list(entries.keys())
        values = [float(entries[n].get()) / nutrition_guidelines[n] * 100 for n in nutrients]

        plt.bar(nutrients, values, color="skyblue", edgecolor="black")
        plt.axhline(100, color='red', linestyle='--', label='Daily Limit (100%)')
        plt.title("Nutritional Contribution per Product")
        plt.ylabel("% of Daily Recommended Intake")
        plt.xticks(rotation=30)
        plt.legend()
        plt.tight_layout()
        plt.show()

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers before showing the graph.")

#  Create the Window with Tinkter
root = tk.Tk()
root.title("Food Label Analyzer")
root.geometry("400x600")
root.config(bg="white")
# Title 
tk.Label(root, text="Food Label Analyzer", font=("Arial", 16, "bold"), bg="white").pack(pady=10)
tk.Label(root, text="Enter values from the food label below:", bg="white").pack()

# Inputs 
entries = {}
for nutrient in nutrition_guidelines.keys():
    frame = tk.Frame(root, bg="white")
    frame.pack(pady=5)
    tk.Label(frame, text=nutrient + ":", width=15, anchor="w", bg="white").pack(side=tk.LEFT)
    entry = tk.Entry(frame, width=10)
    entry.pack(side=tk.RIGHT)
    entries[nutrient] = entry

# Buttons 
tk.Button(root, text="Analyze", command=analyze, bg="#a3c9f1").pack(pady=10)
tk.Button(root, text="Show Graph", command=show_graph, bg="#c1e1c1").pack(pady=5)

#  Result Label 
result_label = tk.Label(root, text="", justify="left", bg="white", fg="black", font=("Arial", 10))
result_label.pack(pady=15)

#  Footer
tk.Label(root, text=" 2025 | Lytissia AIT BELKACEM", bg="white", fg="gray", font=("Arial", 8)).pack(side="bottom", pady=10)

root.mainloop()
