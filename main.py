from webapp import create_app, db
from webapp.constants import *
from webapp.models import News
from webapp.helper.scrapers import *

app = create_app()

if __name__ == '__main__':
    # news_data = []
    # with app.app_context():
    #     for category in IN_CATEGORIES:
    #         data = indian_express(category)
    #         print(len(data))
    #         for item in data:
    #             temp = News(news=item['title'], link=item['link'], site=item['site'], category=item['category'])
    #             news_data.append(temp)
    #     # for category in HT_CATEGORIES:
    #     #     data = hindustan_times(category)
    #     #     print(len(data))
    #     #     for item in data:
    #     #         temp = News(news=item['title'], link=item['link'], site=item['site'], category=item['category'])
    #     #         news_data.append(temp)
    #     for category in ECO_CATEGORIES:
    #         data = economic_times(category)
    #         print(len(data))
    #         for item in data:
    #             temp = News(news=item['title'], link=item['link'], site=item['site'], category=item['category'])
    #             news_data.append(temp)
    #     for category in LOK_CATEGORIES:
    #         data = lokmat_times(category)
    #         print(len(data))
    #         for item in data:
    #             temp = News(news=item['title'], link=item['link'], site=item['site'], category=item['category'])
    #             news_data.append(temp)
    #     # for category in NDTV:
    #     #     data = ndtv(category)
    #     #     print(len(data))
    #     #     for item in data:
    #     #         temp = News(news=item['title'], link=item['link'], site=item['site'], category=item['category'])
    #     #         news_data.append(temp)
    #     for category in IT:
    #         data = india_today(category)
    #         print(len(data))
    #         for item in data:
    #             temp = News(news=item['title'], link=item['link'], site=item['site'], category=item['category'])
    #             news_data.append(temp)
    #     # for category in NEWS18:
    #     #     data = news18(category)
    #     #     print(len(data))
    #     #     for item in data:
    #     #         temp = News(news=item['title'], link=item['link'], site=item['site'], category=item['category'])
    #     #         news_data.append(temp)
    #     for category in ICOM:
    #         data = india_com(category)
    #         print(len(data))
    #         for item in data:
    #             temp = News(news=item['title'], link=item['link'], site=item['site'], category=item['category'])
    #             news_data.append(temp)
    #     hnd = hackernews()
    #     print(len(hnd))
    #     for item in hnd:
    #         temp = News(news=item['title'], link=item['link'], site=item['site'], category=item['category'])
    #         news_data.append(temp)

    #     db.session.add_all(news_data)
    #     db.session.commit()
    #     print('data fetched')
    app.run(host='0.0.0.0', port=8000, debug=True)