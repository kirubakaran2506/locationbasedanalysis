import pandas as pd

# Load dataset
df = pd.read_csv("Dataset.csv")

# -----------------------------
# Step 1: Handle Missing Values
# -----------------------------
for col in df.select_dtypes(include=["int64", "float64"]).columns:
    df[col] = df[col].fillna(df[col].mean())

for col in df.select_dtypes(include=["object"]).columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# -----------------------------
# Step 2: Basic Latitude & Longitude Exploration
# -----------------------------
print("Latitude Summary:")
print(df["Latitude"].describe())

print("\nLongitude Summary:")
print(df["Longitude"].describe())

# -----------------------------
# Step 3: Restaurant Concentration by City (Top 10)
# -----------------------------
city_counts = df["City"].value_counts().head(10)
print("\nTop 10 Cities by Number of Restaurants:")
print(city_counts)

# -----------------------------
# Step 4: Average Rating by City (Top 10)
# -----------------------------
avg_rating_city = (
    df.groupby("City")["Aggregate rating"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\nAverage Rating by City (Top 10):")
print(avg_rating_city)

# -----------------------------
# Step 5: Average Price Range by City (Top 10)
# -----------------------------
avg_price_city = (
    df.groupby("City")["Price range"]
    .mean()
    .sort_values()
    .head(10)
)

print("\nAverage Price Range by City (Top 10):")
print(avg_price_city)

# -----------------------------
# Step 6: Cuisine Distribution in Most Popular City
# -----------------------------
top_city = df["City"].value_counts().idxmax()
top_city_cuisines = df[df["City"] == top_city]["Cuisines"].value_counts().head(5)

print(f"\nTop 5 Cuisines in {top_city}:")
print(top_city_cuisines)