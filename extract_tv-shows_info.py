import requests
import re
import json
from tqdm import tqdm

# Metacritic API url
url = "https://mcgqlapi.com/api"

# Using readlines()
tvshows_file = open('tv_shows.txt', 'r')
tvshows_lines = tvshows_file.readlines()

tvshows = {}

# Obtain information using metacritic API
# https://mcgqlapi.com/docs/tvshowinfo.doc.html
# Assuming there is a similar endpoint for tv shows
for tvshow_line in tqdm(tvshows_lines, desc='Querying MetacriticAPI...', total=len(tvshows_lines)):
    match = re.findall('(.*) \((.*), (.*), (.*), (.*), (.*), ?(.*)?\)', tvshow_line)
    if match:
        title, year, network, genre, studio, rating, adaptation = match[0]
        if '-' in year:
            year_start, year_end = year.split('-')
            year = year_start + '-' + year_end
        else:
            year = year
        query = (
          'query {',
          'tvshow(input: {',
          f'  title: "{title}",',
          '}) {',
          '  title',
          '  season',
          '  criticScore',
          '  releaseDate',
          '  genres',
          '  summary',
          '  numOfCriticReviews',
          '  numOfPositiveCriticReviews',
          '  numOfMixedCriticReviews',
          '  numOfNegativeCriticReviews',
          '  productImage',
          ' }',
          '}'
        )
        query = '\n'.join(query)
        response = requests.post(url=url, json={"query": query})
        if response.status_code == 200:
            tvshows[title] = response.json()

with open('tvshows.json', 'w') as output_file:
     output_file.write(json.dumps(tvshows))
