# -*- coding: utf-8 -*-
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm_cbv.settings')

import django
django.setup()

##FAKE POP SCRIPT

import random
from proj.models import website, website_subject
from faker import Faker

fakegen = Faker()

topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def populate(N=5):

    allsubjectlst = []
    ## ForeignKey 在原來主表，需要儲存成 instance
    lst = website_subject.objects.all()    
    for obj in lst:
        #allsubjectlst.append("%s" % obj.id)        
        allsubjectlst.append(obj)

    for entry in range(N):
        ## get the topic for the entry
        
        fake_title = fakegen.name()        
        fake_uri = fakegen.url()
        fake_date = fakegen.date_time()
        ps('fake_title', fake_title)
        ## random 取得 website_subject instance
        Random_subject = allsubjectlst[random.randint(0, len(allsubjectlst)-1)]
        ## 直接抓取其中一個 instance
        #Random_subject = website_subject.objects.get(pk=4)
        ps('Random_subject', Random_subject)

        ## Create the new Reguser entry
        add_website = website.objects.get_or_create(title=fake_title,
                                                uri=fake_uri, date=fake_date,
                                                subject=Random_subject)[0]

def ps(fn,fv=''):
    print(fn, fv)

if __name__ == '__main__':
    addNum = 30
    print("populating script!")    
    populate(addNum)
    print("add:%s doned" % addNum)
    print("populating complete!")
