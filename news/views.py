from django.shortcuts import render
import urllib.request as url_request
from bs4 import BeautifulSoup


def news_view(request):
    with url_request.urlopen('https://www.themoscowtimes.com/news') as response:
        html_from_page = response.read()
    parse_html = BeautifulSoup(html_from_page, 'html.parser')

    link = parse_html.find(class_='article-excerpt-lead__link').get('href')
    news = parse_html.find(class_='article-excerpt-lead__image-wrapper')
    text_main = parse_html.find_all(class_='wrap wrap1')[0].text
    text = parse_html.find_all(class_='wrap wrap1')[1].text

    temp_list = []
    news_list = []
    link_info = parse_html.find_all(class_='article-excerpt-default__link')
    news_info = parse_html.find_all(class_='article-excerpt-default__image-wrapper')
    text_main_info = parse_html.find_all(class_='article-excerpt-default__headline')
    text_info = parse_html.find_all(class_='article-excerpt-default__teaser')
    for i in range(len(news_info)):
        temp_list.append(link_info[i].get('href'))
        temp_list.append(news_info[i])
        temp_list.append(text_main_info[i].text)
        temp_list.append(text_info[i].text)
        news_list.append(temp_list)
        temp_list = []

    return render(request, 'news.html',
                  {'news': news, 'text': text, 'text_main': text_main, 'link': link, 'list': news_list})
