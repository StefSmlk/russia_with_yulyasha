from django.shortcuts import render
import urllib.request as url_request
from bs4 import BeautifulSoup


def get_photo(info, info_id):
    new_news_info = ''
    yes = False
    for i in str(info[info_id].find('figure')):
        if i == '"':
            yes = not yes
        if yes:
            new_news_info += i
    return new_news_info[1:]


def get_main_photo(info):
    new_news = ''
    yes = False
    for i in str(news.find('figure')):
        if i == '"':
            yes = not yes
        if yes:
            new_news += i
    return new_news[1:]


with url_request.urlopen('https://www.themoscowtimes.com/news') as response:
    html_from_page = response.read()
parse_html = BeautifulSoup(html_from_page, 'html.parser')
news_info = parse_html.find_all(class_='article-excerpt-default__image-wrapper')
links = parse_html.find_all(class_='article-excerpt-default__link')
text_main_info = parse_html.find_all(class_='article-excerpt-default__headline')
text_info = parse_html.find_all(class_='article-excerpt-default__teaser')

news = parse_html.find(class_='article-excerpt-lead__image-wrapper')
link = parse_html.find(class_='article-excerpt-lead__link')
text_main = parse_html.find_all(class_='wrap wrap1')[0].text
text = parse_html.find_all(class_='wrap wrap1')[1].text


def news_view(request):

    temp_list = []
    news_list = []

    for i in range(len(news_info)):
        temp_list.append(i)
        temp_list.append(get_photo(news_info, i))
        temp_list.append(text_main_info[i].text)
        temp_list.append(text_info[i].text)
        news_list.append(temp_list)
        temp_list = []

    return render(request, 'news.html',
                  {'news': get_main_photo(news), 'text': text, 'text_main': text_main, 'list': news_list})


def news_detail_view(request, news_id):
    with url_request.urlopen(links[news_id].get('href')) as resp:
        html_page = resp.read()
    html = BeautifulSoup(html_page, 'html.parser')
    page = html.find_all('p')
    temp_lst = []
    for i in page:
        temp_lst.append(i.text)

    news_list = [get_photo(news_info, news_id), text_main_info[news_id].text, temp_lst]

    return render(request, 'news_detail.html', {'list': news_list})


def main_news_detail_view(request):
    with url_request.urlopen(link.get('href')) as resp:
        html_page = resp.read()
    html = BeautifulSoup(html_page, 'html.parser')
    page = html.find_all('p')
    temp_lst = []
    for i in page:
        temp_lst.append(i.text)

    news_list = [get_main_photo(news), text_main, temp_lst]

    return render(request, 'news_detail.html', {'list': news_list})
