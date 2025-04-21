# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set visualization style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# Load dataset
file_path = r"C:\Users\dell\Desktop\Sem4\Ca folder\AkashPython\IMDB movies rating website.csv"  # Replace with the actual dataset file
df = pd.read_csv(file_path)

# Display basic info and check for missing values
print("Dataset Info:\n")
print(df.info())
print("\nMissing Values:\n")
print(df.isnull().sum())

# Fill numeric missing values with the mean (if any)
df = df.fillna(df.mean(numeric_only=True))

# ---------------------------
# 1. Top 10 Movies by Average Rating
# ---------------------------
if "primaryTitle" in df.columns and "averageRating" in df.columns:
    print("\n=== 1. Top 10 Movies by Average Rating ===")
    top_movies = df.sort_values(by="averageRating", ascending=False).head(10)
    print(top_movies[["primaryTitle", "averageRating"]])

    plt.figure()
    sns.barplot(x="averageRating", y="primaryTitle", data=top_movies, palette="coolwarm")
    plt.title("Top 10 Movies by Average Rating")
    plt.xlabel("Average Rating")
    plt.ylabel("Movie Title")
    plt.tight_layout()
    plt.show()
