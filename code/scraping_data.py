from bs4 import BeautifulSoup
import os
import requests

## set up directories
DATA_DIR = '../data/'

## for Henri-matisse
HENRI_ARTIST_URL = 'http://www.henri-matisse.net/paintingssection{section_num}.html'
HENRI_PAINTING_URL = 'http://www.henri-matisse.net/{painting_source}'

## for Pablo Picasso
PABLO_URL = 'https://www.pablo-ruiz-picasso.net/{where_to_scrape}.php'
PABLO_PAINTING_URL = 'https://www.pablo-ruiz-picasso.net/{painting_source}'

## checking if our data directory is there or not
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)





# getting all of the image urls
def scrape_arts_henri(sec_num):
    url_query = HENRI_ARTIST_URL.format(section_num=sec_num)
    artist_page = requests.get(url_query)

    # check for request error
    try:
        artist_page.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("Error trying to retrieve {}".format(artist_page.url))
        raise e

    soup = BeautifulSoup(artist_page.text, 'lxml')

    painting_paths = []
    ## filtering part, getting year between 1900-1942
    for li in soup.find_all('div', {'class': 'thmbnlspaintingselectbis'}):
        try:
            year = li.find('p').getText().split('\n')[-1].strip()
        except:
            year = li.getText().split('\n')[-1].strip()
        year_lst = year.split('-')
        year = year_lst[-1]
        if len(year) == 4:
            try:
                year = int(year)
            except:
                year = ''
        else:
            continue
        if (1900 <= year <= 1942):
            painting_paths.append(li.find('img').get('src'))
    return painting_paths


HENRI_ARTS = [scrape_arts_henri(sec_num) for sec_num in ['one', 'two', 'three']]
HENRI_ARTS = sum(HENRI_ARTS, [])
HENRI_ARTS






# getting all of the image urls
def scrape_arts_pablo(here_to_scrape):
    PABLO_WEB = PABLO_URL.format(where_to_scrape=here_to_scrape)
    print(PABLO_WEB)
    artist_page = requests.get(PABLO_WEB)
    try:
        artist_page.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("Error trying to retrieve {}".format(artist_page.url))
        raise e

    soup = BeautifulSoup(artist_page.text, 'lxml')

    painting_paths = []
    pics = soup.find('div', {'id': 'main'}).find_all('div', style=lambda value: 'width' in value)

    ## filtering part, getting year between 1900-1942
    for pic in pics:
        year = pic.text.split(',')[-1].strip()
        year_lst = year.split('-')
        year = int(year_lst[-1])
        if (1900 <= year <= 1942):
            painting_paths.append(pic.find('img').get('src'))
    return painting_paths


PABLO_ARTS = scrape_arts_pablo('topviews')+scrape_arts_pablo('topshared')+scrape_arts_pablo('topexpensive')
PABLO_ARTS







def download_and_save(artist_name):
    if artist_name == 'henri-matisse':
        painting_urls = HENRI_ARTS
        PAINTING_URL = HENRI_PAINTING_URL
    else:
        painting_urls = PABLO_ARTS
        PAINTING_URL = PABLO_PAINTING_URL

    IMAGE_DIR = os.path.join(DATA_DIR, artist_name)
    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)
    for url in painting_urls:
        download_url = PAINTING_URL.format(painting_source=url)
        outfile = os.path.join(IMAGE_DIR, url.replace('/', '-'))
        if not os.path.exists(outfile):
            print("downloading: {}".format(url))
            r_painting_page = requests.get(download_url)
            with open(outfile, 'wb') as f:
                f.write(r_painting_page.content)
        else:
            pass

print('start downloading....')
download_and_save('henri-matisse')
download_and_save('picasso')