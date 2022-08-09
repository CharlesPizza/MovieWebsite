from flask import (Blueprint, flash, g, redirect, render_template, request,
    url_for)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db
# from PIL import Image
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import re
import lxml

bp = Blueprint('movies', __name__, url_prefix='/movies')

poster = re.compile('View .* Poster$')

@bp.route('/')
def index():
    image = get_movie_image()
    return render_template('movies/index.html', img=image)


def get_movie_image():
    lists = get_data()
    return (lists)

# Access movie dataset
data_path = r'C:\Users\Charles\PyProjects\MovieRatings\dataset\ml-25m'



def imdb_suffix(ttid):
    leading = 7 - len(str(ttid))
    url_suffix = 'tt' + '0'*leading + str(ttid) + '/'
    return url_suffix

def get_response(link_string):
    resp_dict = {}
    response = requests.get(link_string)
    soup = bs(response.text, 'lxml')
    resp_dict['image'] = get_image(soup)
    resp_dict['name'] = get_name(soup)
    return resp_dict

def get_image(soup):
    try:
        img_href = soup.find(attrs={'aria-label':poster})['href']
    except KeyError:
        return ('images/movenotfound.png')
    pic = requests.get('https://www.imdb.com/'+img_href)
    pic = bs(pic.text, 'lxml')
    return pic.find_all('img')[0]['src']

def get_name(soup):
    return soup.find('h1').text

# Access links dataset
def get_data():
    links_df = pd.read_csv(data_path+'/links.csv')
    sample_df = links_df.sample(5)
    list_data = []
    for row in sample_df.imdbId:
        link_string = 'https://www.imdb.com/title/' + imdb_suffix(row)
        list_data.append(get_response(link_string))
    return list_data