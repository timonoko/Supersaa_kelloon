#! /usr/bin/python3
import requests as u
import json,pprint,os,time,datetime,random

a=u.get('https://www.supersaa.fi',timeout=20)
b=a.text.split('>')
for b2 in b:
        for c in b2.split('<'):
            if c != "" and "{" == c[0]:
                d=json.loads(c)
                break
            break
d=d['props']['pageProps']['weatherOverview']['forecasts']

suunnat=["Pohjois", "Koillis", "Itä", "Kaakko", "Etelä", "Louna",
          "Länsi", "Luode", "Pohjois"]

def ilmansuunta(x):
    return suunnat[round(x/45)]

def tulos(j):
    aa=str(j['temperature'])+"° "+\
              ilmansuunta(j['windDirection'])+" "+\
              str(j['windDirection'])+"° "+\
              str(j['windSpeed'])+"m/s "+\
              j['weatherSymbolText']+"\n"
    return(aa.encode("utf-8"))

eka=1
def indeksi():
    global eka
    eka=(eka+1)%2
    if eka==1:
       return tulos(d[1]['fmi'])
    else:
       return tulos(d[1]['foreca'])
