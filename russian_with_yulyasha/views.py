from django.shortcuts import render
import requests
from folium.plugins import MarkerCluster
from lxml import etree
import folium


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


def about_view(request):
    return render(request, 'about.html', {})


def map_view(request):
    map_ = folium.Map([55.3311, 37.2258], zoom_start=5, tiles='Stamen Terrain')

    with open('data.csv', 'r', encoding='UTF-8') as data:
        data_text = data.read()

    data_text_list = data_text.split('\n')

    def color_change(elev):
        if elev < 50:
            return 'green'
        elif 50 <= elev < 300:
            return 'orange'
        else:
            return 'red'

    marker_cluster = MarkerCluster().add_to(map_)

    for i in range(1, len(data_text_list) - 1):
        folium.Marker(location=[float(data_text_list[i].split(',')[10]), float(data_text_list[i].split(',')[11])],
                      popup=f"""
                            <a class='text-decoration-none text-center' target="_blank" href='{data_text_list[i].split(',')[0]}'>
                                <h1>{data_text_list[i].split(',')[4][1:-1]}
                                </h1>
                            </a>
                        """,
                      icon=folium.Icon(color=color_change(float(data_text_list[i].split(',')[7]))), color="gray",
                      fill_opacity=0.9).add_to(marker_cluster)

    marker_cluster = marker_cluster.get_root().render()
    return render(request, 'map.html', {'map': marker_cluster})
