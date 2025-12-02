# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 14:37:21 2025

@author: mourade
"""

#  FOOD LABEL ANALYZER 
#  done by Lytissia Ait Belkacem
#  Description:
#     A simple and clear graphical interface that analyzes
#     nutrition facts from a packaged food label and provides
#     helpful recommendations for the user.

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

# -------- Functions --------
def analyze():
    try:
        user_data = {}
        for nutrient, entry in entries.items():
            value = float(entry.get())
            user_data[nutrient] = value

        percentages = {
            nut: (val / nutrition_guidelines[nut]) * 100
            for nut, val in user_data.items()
        }

        # Recommendation Logic
        sugar = percentages["Sugar (g)"]
        fat = percentages["Fat (g)"]
        cal = percentages["Calories (kcal)"]

        if sugar > 60 or fat > 60 or cal > 60:
            recommendation = "⚠️ This product is likely UNHEALTHY.\nHigh levels detected."
            color = "red"
        elif sugar > 30 or fat > 30 or cal > 30:
            recommendation = "🟠 Eat in MODERATION.\nSome nutrients are a bit high."
            color = "orange"
        else:
            recommendation = "🟢 This product seems HEALTHY.\nWell-balanced values."
            color = "green"

        # Identify High / Low Nutrients
        details = "\n\nNutrient Highlights:\n"
        for n, pct in percentages.items():
            if pct > 50:
                details += f"• {n}: HIGH ❗ ({pct:.1f}%)\n"
            elif pct < 10:
                details += f"• {n}: LOW ⚠️ ({pct:.1f}%)\n"

        # Print Summary
        result_label.config(
            text=recommendation + details,
            fg=color
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter numbers only!")


def show_graph():
    try:
        nutrients = list(entries.keys())
        values = [float(entries[n].get()) / nutrition_guidelines[n] * 100 for n in nutrients]

        plt.bar(nutrients, values, edgecolor="black")
        plt.axhline(100, color='red', linestyle='--', label='Daily Limit (100%)')
        plt.title("Nutritional Contribution per Product")
        plt.ylabel("% of Daily Recommended Intake")
        plt.xticks(rotation=30)
        plt.legend()
        plt.tight_layout()
        plt.show()

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers first.")


def clear_fields():
    for entry in entries.values():
        entry.delete(0, tk.END)
    result_label.config(text="", fg="black")


# --------- INTERFACE ---------
root = tk.Tk()
root.title("Food Label Analyzer")
root.geometry("420x650")
root.config(bg="white")

# Title
tk.Label(
    root, text="🍏 FOOD LABEL ANALYZER", 
    font=("Arial", 18, "bold"), bg="white"
).pack(pady=15)

tk.Label(
    root, text="Enter values from the food label:",
    font=("Arial", 10), bg="white"
).pack()

entries = {}
for nutrient in nutrition_guidelines.keys():
    frame = tk.Frame(root, bg="white")
    frame.pack(pady=5)

    tk.Label(frame, text=nutrient + ":", width=18, anchor="w", bg="white").pack(side=tk.LEFT)
    entry = tk.Entry(frame, width=12, bg="#f5f5f5")
    entry.pack(side=tk.RIGHT)
    entries[nutrient] = entry

# Buttons Section
button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=20)

tk.Button(
    button_frame, text="Analyze", command=analyze,
    bg="#88c8ff", width=15
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame, text="Show Graph", command=show_graph,
    bg="#a4e6a1", width=15
).grid(row=0, column=1, padx=5)

tk.Button(
    root, text="Clear All", command=clear_fields,
    bg="#f7a8a8", width=20
).pack()

# Output Label
result_label = tk.Label(
    root, text="", justify="left",
    bg="white", fg="black", font=("Arial", 11)
)
result_label.pack(pady=20)

# Footer
tk.Label(
    root, text="© 2025 | Lytissia AIT BELKACEM",
    bg="white", fg="gray", font=("Arial", 8)
).pack(side="bottom", pady=10)

root.mainloop()

