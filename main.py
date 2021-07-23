import requests
from bs4 import BeautifulSoup
import time
import plyer

def get_weather0():
    url ='https://yandex.ru/pogoda/lipetsk?utm_campaign=informer&utm_content=main_informer&utm_medium=web&utm_source=home&utm_term=main_number'
    page = requests.get(url)
    # print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser")
    p1 = []
    p1 = str(soup.findAll('abbr', class_='icon-abbr'))
    p1 = p1[26:30]
    # print(p1)
    return(p1)

def ischange(p1):
    url = 'https://yandex.ru/pogoda/lipetsk?utm_campaign=informer&utm_content=main_informer&utm_medium=web&utm_source=home&utm_term=main_number'
    page = requests.get(url)
    #print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser")
    p2 = []
    p2 = str(soup.findAll('abbr', class_='icon-abbr'))
    p2 = p2[26:30]
    if p2 == p1:
        print("изменений нет")
        time.sleep(5)
        ischange(p1)
    else:
        give_advice(get_weather0())

def give_advice(p1):
    if p1 == str("севе") or p1 == str("вост"):
        plyer.notification.notify(message='закрывай окна',
        app_name='Название твоего приложения',
        #app_icon='sample.jpg',
        title='обновления ветра на лтз',)
        time.sleep(5)
        ischange(get_weather0())
    else:
        #print("open wind")
        plyer.notification.notify(message='можно проветрить', app_name='Название твоего приложения',
        # app_icon='sample.jpg',
        title='обновления ветра на лтз', )
        time.sleep(5)
        ischange(get_weather0())

give_advice(get_weather0())
time.sleep(2)
ischange(get_weather0())