import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','proj1.settings')

import django
django.setup()

import random
from app1.models import Topic,Webpage,AccessRecord
from faker import Faker

fake = Faker()
topics = ['Search','Social','Marketplace','News','Games']
#Adding random topic from lists
def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):
        #getting topic for the entry
        top = add_topic()

        #Create fake url,name and company for entry
        fake_url = fake.url()
        fake_date = fake.date()
        fake_name = fake.company()
        #Create webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        
         #Creating fake access record entry
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print('Populate Script')
    populate(20)
    print('Populating Complete')