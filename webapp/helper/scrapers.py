from bs4 import BeautifulSoup
import requests

def get_response(url):
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Accept-Encoding": "*",
        "Connection": "keep-alive"
    }
    response = requests.get(url=url, headers=HEADERS)
    if response.status_code == 200:
        return response
    return response.raise_for_status()

def indian_express(category):
    # IN_CATEGORIES = ['political-pulse', 'india', 'entertainment', 'sports']
    _cat = {
        'political-pulse' : 'Politics',
        'india' : 'National'
    }
    BASE_URL = "https://indianexpress.com/section/"

    url = BASE_URL + category
    if category in _cat:
        category = _cat[category]
    else:
        category = category.title()
    response = get_response(url)
    data = []
    soup = BeautifulSoup(response.content, 'lxml')
    container = soup.find('div', class_='nation')
    articles = container.find_all('div', class_='articles')[:12]
    for i in range(len(articles)):
        title_link = articles[i].find(class_='title').find('a')
        title = title_link.text.strip()
        link = title_link['href']

        temp = {
            'title' : title,
            'link' : link,
            'site' : 'Indian Express',
            'category' : category
        }
        data.append(temp)
    return data

def hindustan_times(category):
    # HT_CATEGORIES = ['india', 'world', 'entertainment', 'sports', 'business', 'science']
    _cat = {
        'india' : 'National',
        'science' : 'Technology'
    }
    BASE_URL = 'https://www.hindustantimes.com/'

    data = []
    response = get_response(BASE_URL + category)
    if category in _cat:
        category = _cat[category]
    else:
        category = category.title()
    soup = BeautifulSoup(response.content, 'lxml')
    cards = soup.find_all('div', class_='cartHolder')[:12]
    for i in range(len(cards)):
        title_link = cards[i].find('h3', class_='hdg3')
        link = BASE_URL + title_link.find('a')['href'][1:]
        title = title_link.text.strip()

        temp = {
            'title' : title,
            'link' : link,
            'site' : 'Hindustan Times',
            'category' : category
        }
        data.append(temp)
    return data

def economic_times(category):
    # ECO_CATEGORIES = ["news/india", "news/sports", "news/politics", "news/international/world-news", "news/science"]
    _cat = {
        'india' : 'National',
        'international' : 'World',
        'science' : 'Technology'
    }
    BASE_URL = "https://economictimes.indiatimes.com/"

    data = []
    response = get_response(BASE_URL + category)
    category = category.split('/')
    if category[1] in _cat:
        category = _cat[category[1]]
    else:
        category = category[1].title()
    soup = BeautifulSoup(response.content, 'lxml')
    div = soup.find('div', class_='tabdata')
    cards = div.find_all('div', class_='eachStory')[:12]
    for card in cards:
        title_link = card.find('h3').find('a', href=True)
        link = BASE_URL + title_link['href']
        title = title_link.text.strip()

        temp = {
            'title' : title,
            'link' : link,
            'site' : 'Economic Times',
            'category' : category
        }
        data.append(temp)
    return data

def lokmat_times(category):
    # LOK_CATEGORIES = ['sports', 'technology', 'business', 'international', 'entertainment', 'national']
    BASE_URL = 'https://www.lokmattimes.com/'

    data = []
    response = get_response(BASE_URL + category)
    if category == 'international':
        category = 'World'
    else:
        category = category.title()
    soup = BeautifulSoup(response.content, 'lxml')
    cards = soup.find_all('figure')[:9]
    for card in cards:
        title_link = card.find('h2').find('a', class_=False)
        title = title_link.text.strip()
        link = title_link['href']

        temp = {
            'title' : title,
            'link' : link,
            'site' : 'Lokmat Times',
            'category' : category
        }
        data.append(temp)
    return data

def ndtv(category):
    # NDTV = ['india', 'world-news', 'science', 'business/latest', 'entertainment/latest']
    _cat = {
        'india' : 'National',
        'world-news' : 'World',
        'science' : 'Technology'
    }
    BASE_URL = 'https://www.ndtv.com/'

    data = []
    response = get_response(BASE_URL + category)
    category = category.split('/')
    if category[0] in _cat:
        category = _cat[category[0]]
    else:
        category = category[0].title()
    soup = BeautifulSoup(response.content, 'lxml')
    div = soup.find('div', class_='lisingNews')
    cards = div.find_all('div', class_='news_Itm')
    for card in cards:
        temp = {}
        title_link = card.find('h2', class_='newsHdng')
        try:
            title = title_link.text.strip()
            link = title_link.find('a', href=True)['href']
            temp['title'] = title
            temp['link'] = link
            temp['site'] = 'NDTV'
            temp['category'] = category
            data.append(temp)
        except:
            pass
    return data[:12]

def hackernews():
    BASE_URL = 'https://news.ycombinator.com/'
    data = []

    response = get_response('https://news.ycombinator.com/newest')
    soup = BeautifulSoup(response.content, 'lxml')
    table = soup.find('table')
    articles = table.find_all('span', class_='titleline')[:12]
    for item in articles:
        title = item.text.strip()
        site = item.find('a', href=True)['href']

        temp = {
            'title' : title,
            'site' : 'Hacker News',
            'link' : site,
            'category' : 'Technology'
        }
        data.append(temp)
    return data

def india_today(category):
    # IT = ['politics', 'technology', 'world']

    BASE_URL = 'https://www.indiatoday.in/'
    data = []
    response = get_response(BASE_URL + category)
    if category == 'showbuzz':
        category = 'entertainment'
    soup = BeautifulSoup(response.content, 'lxml')
    body = soup.find('div', class_='story__grid')
    articles = body.find_all('article', class_='B1S3_story__card__A_fhi')[:12]
    for item in articles:
        anchor = item.find('h2').find('a')
        title = anchor['title']
        link = BASE_URL + anchor['href']

        temp = {
            'title' : title,
            'site' : 'India Today',
            'link' : link,
            'category' : category.title()
        }
        data.append(temp)
    return data

def news18(category):
    #NEWS18 = ['politics', 'tech']
    _cat = {
        'tech' : 'Technology',
        'movies' : 'Entertainment'
    }
    data = []

    BASE_URL = 'https://www.news18.com/'
    response = get_response(BASE_URL + category)
    if category in _cat:
        category = _cat[category]
    soup = BeautifulSoup(response.content, 'lxml')
    blogs = soup.find_all('div', class_='jsx-4088862090 blog_list')[-1]
    cards = blogs.find_all('div', class_='jsx-4088862090 blog_list_row')[:12]
    for item in cards:
        link = item.find('a')['href']
        title = item.find('div', class_='jsx-4088862090 blog_title').find('h4').text.strip()

        temp = {
            'title' : title,
            'link' : link,
            'site' : 'News18',
            'category' : category.title()
        }
        data.append(temp)
    return data

def india_com(category):
    #ICOM = ['sports', 'business']
    BASE_URL = 'https://www.india.com/'
    data = []

    response = get_response(BASE_URL + category)
    soup = BeautifulSoup(response.content, 'lxml')
    news = soup.find('div', class_='listing-boxes')
    cards = news.find_all('article', class_='repeat-box')[:12]
    for item in cards:
        anchor = item.find('figcaption', class_='text').find('h2').find('a')
        link = anchor['href']
        title = anchor.text.strip()

        temp = {
            'title' : title,
            'link' : link,
            'site' : 'India.Com',
            'category' : category.title()
        }
        data.append(temp)
    return data

# for c in NDTV:
#     print(len(ndtv(c)))
# for c in LOK_CATEGORIES:
#     print(len(lokmat_times(c)))
# for c in HT_CATEGORIES:
#     print(len(hindustan_times(c)))
# for c in IN_CATEGORIES:
#     print(len(indian_express(c)))
# for c in ECO_CATEGORIES:
#     print(len(economic_times(c)))