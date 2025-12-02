# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 14:42:09 2025

@author: mourade
"""
import streamlit as st
import matplotlib.pyplot as plt

nutrition_guidelines = {
    "Calories (kcal)": 2000,
    "Protein (g)": 50,
    "Fat (g)": 70,
    "Sugar (g)": 50,
    "Fiber (g)": 25,
    "Vitamin C (mg)": 90
}

st.title("🥗 Food Label Analyzer")
st.write("Enter the nutrition values from the food label:")

user_data = {}
for nutrient in nutrition_guidelines:
    user_data[nutrient] = st.number_input(nutrient, min_value=0.0, step=0.1)

if st.button("Analyze"):
    percentages = {}
    for nutrient, value in user_data.items():
        ref = nutrition_guidelines[nutrient]
        percentages[nutrient] = (value / ref) * 100

    sugar_pct = percentages["Sugar (g)"]
    fat_pct = percentages["Fat (g)"]
    cal_pct = percentages["Calories (kcal)"]

    if sugar_pct > 50 or fat_pct > 50 or cal_pct > 50:
        recommendation = "❌ Unhealthy"
    elif sugar_pct > 30 or fat_pct > 30 or cal_pct > 30:
        recommendation = "⚠️ Eat in Moderation"
    else:
        recommendation = "✅ Healthy Choice"

    st.subheader("📊 Nutrition Analysis")
    for nutrient, pct in percentages.items():
        st.write(f"**{nutrient}:** {pct:.1f}% of daily need")

    st.subheader("Recommendation:")
    st.success(recommendation)

    fig, ax = plt.subplots()
    ax.bar(percentages.keys(), percentages.values())
    ax.axhline(100, color='red', linestyle='--')
    plt.xticks(rotation=30)
    st.pyplot(fig)

