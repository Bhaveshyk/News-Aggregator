PASS_REGEX = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
CATEGORIES = ['National', 'World', 'Sports', 'Entertainment', 'Business', 'Technology', 'Politics']
LOK_CATEGORIES = ['sports', 'technology', 'business', 'international', 'entertainment', 'national']
NDTV = ['india', 'world-news', 'science', 'business/latest', 'entertainment/latest']
ECO_CATEGORIES = ["news/india", "news/sports", "news/international/world-news", "news/science"]
IN_CATEGORIES = ['political-pulse', 'india', 'entertainment', 'sports']
HT_CATEGORIES = ['india', 'world', 'entertainment', 'sports', 'business', 'science']
IT = ['politics', 'business', 'world']
NEWS18 = ['politics', 'tech', 'movies']
ICOM = ['sports', 'business']

SITE_MAP = {
    'National' : ['Indian Express', 'NDTV', 'Hindustan Times', 'Economic Times', 'Lokmat Times'],
    'World' : ['NDTV', 'Hindustan Times', 'Economic Times','India Today', 'Lokmat Times'],
    'Sports' : ['Indian Express', 'Hindustan Times', 'Economic Times', 'India.Com', 'Lokmat Times'],
    'Entertainment' : ['Indian Express', 'NDTV', 'Hindustan Times', 'News18', 'Lokmat Times'],
    'Technology' : ['NDTV', 'Hindustan Times', 'Economic Times', 'News18', 'Hacker News'],
    'Politics' : ['Indian Express', 'India Today', 'News18'],
    'Business' : ['NDTV', 'Hindustan Times', 'India Today', 'India.Com', 'Lokmat Times']
}