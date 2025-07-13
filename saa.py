#! /usr/bin/python3
import requests as u
import json,pprint,os,time,datetime,random


if (time.localtime().tm_min%20)!=0:
    print('väärä aika')
    exit()

print('haku')
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

def tulos(j,tunnus):
  with open("index.html","w") as f:
          f.write(tunnus+" "+
                  str(time.localtime().tm_hour)+":"+
                  str(time.localtime().tm_min)+"\n"+
              str(j['temperature'])+"° "+
              ilmansuunta(j['windDirection'])+" "+
              str(j['windDirection'])+"° "+
              str(j['windSpeed'])+"m/s "+
              j['weatherSymbolText']+"\n")

if time.localtime().tm_min == 20:
    tulos(d[1]['fmi'],"I")
else:
    tulos(d[1]['foreca'],"F")
