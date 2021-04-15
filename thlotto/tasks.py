from __future__ import absolute_import, unicode_literals
from time import sleep
from .models import gov_thai
from celery import shared_task
from bs4 import BeautifulSoup
from .views import gov_thaiDetail
import requests
import json


@shared_task
def create_gov_thai():
    print('Creating data..')
    req = requests.get('https://lotto.postjung.com', headers={'User-Agent': 'Mozilla/5.0'})
    bs = BeautifulSoup(req.content, 'html.parser')
    title = bs.find_all('div', attrs={'class':'sptitle'})[0].get_text()[0:19]
    date = bs.find_all('div', attrs={'class':'sptitle'})[0].get_text()[22:42]
    FirstPrize = bs.find_all('div', attrs={'class':'xres'})[0].get_text()
    ThreeFront = bs.find_all('div', attrs={'class':'xres'})[2].get_text()[0:3]
    ThreeFrontTwo = bs.find_all('div', attrs={'class':'xres'})[2].get_text()[3:6]
    ThreeUnder = bs.find_all('div', attrs={'class':'xres'})[3].get_text()[0:3]
    ThreeUnderTwo = bs.find_all('div', attrs={'class':'xres'})[3].get_text()[3:6]
    TwoUnder = bs.find_all('div', attrs={'class':'xres'})[1].get_text()
        
    print({'title':title, 'date':date, 'FirstPrize':FirstPrize, 'ThreeFront':ThreeFront, 'ThreeFrontTwo':ThreeFrontTwo, 'ThreeUnder':ThreeUnder, 'ThreeUnderTwo':ThreeUnderTwo, 'TwoUnder':TwoUnder})

    gov_thai.objects.create(
        title=title,
        date=date,
        FirstPrize=FirstPrize,
        ThreeFront=ThreeFront,
        ThreeFrontTwo=ThreeFrontTwo,
        ThreeUnder=ThreeUnder,
        ThreeUnderTwo=ThreeUnderTwo,
        TwoUnder=TwoUnder,
    )
    
    print('Data have been Created')

    sleep(5)
    
    
@shared_task
def update_gov_thai():
    print('Updating data..')
    req = requests.get('https://lotto.postjung.com', headers={'User-Agent': 'Mozilla/5.0'})
    bs = BeautifulSoup(req.content, 'html.parser')
    title = bs.find_all('div', attrs={'class':'sptitle'})[0].get_text()[0:19]
    date = bs.find_all('div', attrs={'class':'sptitle'})[0].get_text()[22:42]
    FirstPrize = bs.find_all('div', attrs={'class':'xres'})[0].get_text()
    ThreeFront = bs.find_all('div', attrs={'class':'xres'})[2].get_text()[0:3]
    ThreeFrontTwo = bs.find_all('div', attrs={'class':'xres'})[2].get_text()[3:6]
    ThreeUnder = bs.find_all('div', attrs={'class':'xres'})[3].get_text()[0:3]
    ThreeUnderTwo = bs.find_all('div', attrs={'class':'xres'})[3].get_text()[3:6]
    TwoUnder = bs.find_all('div', attrs={'class':'xres'})[1].get_text()
    
    data = {'title':title, 'date':date, 'FirstPrize':FirstPrize, 'ThreeFront':ThreeFront, 'ThreeFrontTwo':ThreeFrontTwo, 'ThreeUnder':ThreeUnder, 'ThreeUnderTwo':ThreeUnderTwo, 'TwoUnder':TwoUnder}
    gov_thai.objects.filter(date=date).update(**data)

    sleep(5)

create_gov_thai()
if True:
    sleep(5)
    update_gov_thai()
    print('Data have been Updated')