import json
import requests
from bs4 import BeautifulSoup
from celery import shared_task
from .models import *
from time import sleep


@shared_task
def create_lao_vip():
    print('Creating lao VIP data...')
    req = requests.get('https://www.laosviplot.com/result')
    bs = BeautifulSoup(req.content, 'html.parser')
    json_data = json.loads(str(bs.text))
    numOne = json_data['lotto_0']
    numTwo = json_data['lotto_1']
    numThree = json_data['lotto_2']
    numFour = json_data['lotto_3']
    numFive = json_data['lotto_4']
    title = ('หวยลาวVIP')
    Five = numOne + numTwo + numThree + numFour + numFive
    Four = numOne + numTwo + numThree + numFour
    Three = numOne + numTwo + numThree
    Two = numOne + numTwo
    date = json_data['date']
    
    print({'title':title, 'Five':Five, 'Four':Four, 'Three':Three, 'Two':Two, 'date':date})

    lao_vip.objects.create(
        title=title,
        Five=Five,
        Four=Four,
        Three=Three,
        Two=Two,
        date=date
    )
    
    sleep(15)
    
@shared_task
def update_lao_vip():
    print('Updating lao VIP data...')
    req = requests.get('https://www.laosviplot.com/result')
    bs = BeautifulSoup(req.content, 'html.parser')
    json_data = json.loads(str(bs.text))
    numOne = json_data['lotto_0']
    numTwo = json_data['lotto_1']
    numThree = json_data['lotto_2']
    numFour = json_data['lotto_3']
    numFive = json_data['lotto_4']
    title = ('หวยลาวVIP')
    Five = numOne + numTwo + numThree + numFour + numFive
    Four = numOne + numTwo + numThree + numFour
    Three = numOne + numTwo + numThree
    Two = numOne + numTwo
    date = json_data['date']
    
    data= {'title':title, 'Five':Five, 'Four':Four, 'Three':Three, 'Two':Two, 'date':date}
    lao_vip.objects.filter(date=date).update(**data)


create_lao_vip()
if True:
    sleep(3)
    update_lao_vip()


@shared_task
def create_lao_lotto():
    print('Creating lao lotto data...')
    req = requests.get('https://www.ruay.info/%E0%B8%95%E0%B8%A3%E0%B8%A7%E0%B8%88%E0%B8%AB%E0%B8%A7%E0%B8%A2%E0%B8%A5%E0%B8%B2%E0%B8%A7/')
    bs = BeautifulSoup(req.content, 'html.parser')
    title = bs.find_all('strong')[1].get_text()
    date = bs.find_all('span')[15].get_text()
    Four = bs.find_all('strong')[3].get_text()
    Three = bs.find_all('strong')[6].get_text()
    Two = bs.find_all('strong')[7].get_text()
    
    print({'title':title, 'Four':Four, 'Three':Three, 'Two':Two, 'date':date})
    
    lao_lotto.objects.create(
        title=title,
        Four=Four,
        Three=Three,
        Two=Two,
        date=date
    )
    
    sleep(3)


@shared_task
def update_lao_lotto():
    print('Updating lao lotto data...')
    req = requests.get('https://www.ruay.info/%E0%B8%95%E0%B8%A3%E0%B8%A7%E0%B8%88%E0%B8%AB%E0%B8%A7%E0%B8%A2%E0%B8%A5%E0%B8%B2%E0%B8%A7/')
    bs = BeautifulSoup(req.content, 'html.parser')
    title = bs.find_all('strong')[1].get_text()
    date = bs.find_all('span')[15].get_text()
    Four = bs.find_all('strong')[3].get_text()
    Three = bs.find_all('strong')[6].get_text()
    Two = bs.find_all('strong')[7].get_text()
    
    data = ({'title':title, 'Four':Four, 'Three':Three, 'Two':Two, 'date':date})
    lao_lotto.objects.filter(date=date).update(**data)

create_lao_lotto()
if True:
    sleep(3)
    update_lao_lotto()
