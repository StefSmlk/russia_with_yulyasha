from django.shortcuts import render
import requests
from lxml import etree


def home_view(request):
    resp = requests.get('https://www.themoscowtimes.com/rss/news')
    with open('my.xml', 'w', encoding='UTF-8') as my:
        my.write(resp.text)

    with open('my.xml', 'rb') as fobj:
        xml = fobj.read()

    list_of_news = []

    root = etree.fromstring(xml)
    news = root.getchildren()[0].getchildren()
    for j in range(7, 13):
        temp_list_of_news = []
        for i in range(len(news[j].getchildren())):
            if i < 4:
                temp_list_of_news.append(news[j].getchildren()[i].text)
        list_of_news.append(temp_list_of_news)

    return render(request, 'home.html', {'news': list_of_news})


def contacts_view(request):
    return render(request, 'contacts.html', {})


def about_view(request):
    return render(request, 'about.html', {})
