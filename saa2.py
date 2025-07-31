#! /usr/bin/python3
import requests as u
import json,pprint,os,time,datetime,random

suunnat=["Pohjois", "Koillis", "Itä", "Kaakko", "Etelä", "Louna",
          "Länsi", "Luode", "Pohjois"]

def ilmansuunta(x):
    return suunnat[round(x/45)]

def lataus():
   global d
   a=u.get('https://www.supersaa.fi',timeout=60)
   b=a.text.split('>')
   for b2 in b:
        for c in b2.split('<'):
            if c != "" and "{" == c[0]:
                d=json.loads(c)
                break
            break
   d=d['props']['pageProps']['weatherOverview']['forecasts']


def tulos(laitos):
  try:
    j=d[1][laitos]
    aa=str(j['temperature'])+"° "+\
              ilmansuunta(j['windDirection'])+" "+\
              str(j['windDirection'])+"° "+\
              str(j['windSpeed'])+"m/s "+\
              j['weatherSymbolText']+"\n"
  except:
    aa=laitos+' ei toimi'
  return(aa.encode("utf-8"))

eka=1
def indeksi():
    global eka
    lataus()
    eka=(eka+1)%2
    if eka==1:
       return tulos('fmi')
    else:
       return tulos('foreca')
