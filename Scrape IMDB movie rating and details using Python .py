from bs4 import BeautifulSoup
import requests
import time

try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    source = requests.get('https://www.imdb.com/chart/top/', headers=headers)
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')

    movies=soup.find('ul',class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-3a353071-0 wTPeg compact-list-view ipc-metadata-list--base").find_all('li',class_='ipc-metadata-list-summary-item sc-bca49391-0 eypSaE cli-parent')

    for movie in movies:
        movie_info=movie.find('div',class_='sc-14dd939d-0 fBusXE cli-children').a.text
        rank, name = movie_info.split('. ',1)  
        year=movie.find('span',class_="sc-14dd939d-6 kHVqMR cli-title-metadata-item").text  
        rating=movie.find('span',class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating").text  
        print(rank,name,year,rating)
               
except Exception as e:
    print(e)
