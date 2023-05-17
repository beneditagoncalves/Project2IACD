import pandas as pd
import json

# Load the json files
with open('movies.json', 'r') as movies_file:
    movies_data = json.load(movies_file)
with open('albums.json', 'r') as albums_file:
    albums_data = json.load(albums_file)
with open('tvshows.json', 'r') as tvshows_file:
    tvshows_data = json.load(tvshows_file)
# Convert dictionaries to pandas DataFrames
movies_df = pd.json_normalize(movies_data.values())
albums_df = pd.json_normalize(albums_data.values())
tvshows_df = pd.json_normalize(tvshows_data.values())

# Ensure columns are named correctly
movies_df.rename(columns={'title': 'Title', 'criticScore': 'Critic Score', 'releaseDate': 'Release Date', 'genres': 'Genres', 'numOfCriticReviews': 'Number of Critic Reviews'}, inplace=True)
albums_df.rename(columns={'album': 'Title', 'criticScore': 'Critic Score', 'releaseDate': 'Release Date', 'genres': 'Genres', 'numOfCriticReviews': 'Number of Critic Reviews'}, inplace=True)
tvshows_df.rename(columns={'title': 'Title', 'criticScore': 'Critic Score', 'releaseDate': 'Release Date', 'genres': 'Genres', 'numOfCriticReviews': 'Number of Critic Reviews'}, inplace=True)

# Concatenate the datasets
merged_df = pd.concat([movies_df, albums_df, tvshows_df], axis=0, ignore_index=True)

# Handle missing values (NaNs)
merged_df.fillna('NA', inplace=True)


# Print the first few rows of the merged DataFrame
print(merged_df.head())

# Print information about the merged DataFrame
print(merged_df.info())

# Print summary statistics of the merged DataFrame
print(merged_df.describe())

