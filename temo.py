import pandas as pd

input_file = "english_to_malayalam_500k.csv"
output_file = "english_to_malayalam_100k_small.csv"

# Read CSV
df = pd.read_csv(input_file)

# Drop empty rows
df = df.dropna(subset=["en", "ml"])

# Sentence length (number of words)
df["en_len"] = df["en"].apply(lambda x: len(str(x).split()))

# Sort by sentence length (ascending = smallest first)
df_sorted = df.sort_values(by="en_len", ascending=True)

# Take smallest 100k sentences
small_100k = df_sorted.head(100_000)

# Remove helper column
small_100k = small_100k.drop(columns=["en_len"])

# Save to CSV
small_100k.to_csv(output_file, index=False)

print("✅ Saved", len(small_100k), "smallest sentences")
