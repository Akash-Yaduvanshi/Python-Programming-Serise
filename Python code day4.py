# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set visualization style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# Load dataset
file_path = r"C:\Users\dell\Desktop\Sem4\Ca folder\Akash Day1 Ptython\IMDB movies rating website.csv"  # Replace with the actual dataset file
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

# ---------------------------
# 2. Distribution of Runtime
# ---------------------------
if "runtimeMinutes" in df.columns:
    print("\n=== 2. Distribution of Runtime ===")
    print(df["runtimeMinutes"].describe())

    plt.figure()
    sns.histplot(df["runtimeMinutes"], bins=20, kde=True, color="orange")
    plt.title("Distribution of Movie Runtime")
    plt.xlabel("Runtime (Minutes)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

# ---------------------------
# 3. Top 5 Genres by Movie Count
# ---------------------------
if "genres" in df.columns:
    print("\n=== 3. Top 5 Genres by Movie Count ===")
    genre_counts = df["genres"].value_counts().head(5)
    print(genre_counts)

    plt.figure()
    sns.barplot(x=genre_counts.values, y=genre_counts.index, palette="Set2")
    plt.title("Top 5 Genres by Movie Count")
    plt.xlabel("Number of Movies")
    plt.ylabel("Genres")
    plt.tight_layout()
    plt.show()


# ---------------------------
# 4. Pollutant with the Most Significant Impact
# ---------------------------
if "Name" in df.columns and "Data Value" in df.columns:
    print("\n=== 4. Pollutant with the Most Significant Impact ===")
    pollutant_impact = df.groupby("Name")["Data Value"].mean().sort_values(ascending=False).head(10)
    print(pollutant_impact)

    plt.figure()
    sns.barplot(x=pollutant_impact.values, y=pollutant_impact.index, palette="viridis")
    plt.title("Top 10 Pollutants by Impact")
    plt.xlabel("Average Data Value")
    plt.ylabel("Pollutants")
    plt.tight_layout()
    plt.show()
