import pandas as pd

# 1. Tell the computer where the files are
input_file = 'data/raw/acled-africa-aggregated.csv'
output_file = 'data/cleaned/ACLED_Central_Sahel_filtered.csv'

print(f"Reading the big data file: {input_file}...")

# 2. Load the CSV file into a "DataFrame" (think of it as a digital spreadsheet)
df = pd.read_csv(input_file)

# 3. Create a list of the countries we want to keep
target_countries = ['Burkina Faso', 'Niger', 'Mali']

# 4. Filter the data: Keep only rows where the 'COUNTRY' column matches our list
# .isin() is a handy tool that checks if the country name is in our list
filtered_df = df[df['COUNTRY'].isin(target_countries)]

# 5. Save the smaller, filtered version to a new file
# index=False means we don't want to add extra row numbers to our CSV
filtered_df.to_csv(output_file, index=False)

print(f"Success! I found {len(filtered_df)} rows for {target_countries}.")
print(f"The new file is saved at: {output_file}")
