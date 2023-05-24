import requests
import re
import json
from tqdm import tqdm

# Metacritic API url
url = "https://mcgqlapi.com/api"

# Using readlines()
albums_file = open('albums.txt', 'r')
albums_lines = albums_file.readlines()

albums = {}

# Obtain information using Metacritic API
# https://mcgqlapi.com/docs/albuminfo.doc.html
for album_line in tqdm(albums_lines, desc='Querying MetacriticAPI...', total=len(albums_lines)):
    pattern = r'(.*) - (.*) \((.*?)\) - (\d{4}) - (.*?) - (\d+ million)?$'
    match = re.match(pattern, album_line.strip())
    if match:
        album, artist, genres, release_date, publisher, sales = match.groups()
        album_identifier = f"{album} - {artist}"
        query = (
            'query {',
            '  album(input: {',
            f'    album: "{album}",',
            f'    artist: "{artist}"',
            '  }) {',
            '    url',
            '    album',
            '    artist',
            '    releaseDate',
            '    criticScore',
            '    publisher',
            '    genres',
            '    numOfCriticReviews',
            '    numOfPositiveCriticReviews',
            '    numOfMixedCriticReviews',
            '    numOfNegativeCriticReviews',
            '  }',
            '}'
        )
        query = '\n'.join(query)
        response = requests.post(url=url, json={"query": query})
        if response.status_code == 200:
            album_data = response.json().get('data', {}).get('album')
            if album_data:
                albums[album_identifier] = {"data": {"album": album_data}}


with open('albums.json', 'w') as output_file:
    output_file.write(json.dumps(albums, indent=2))
