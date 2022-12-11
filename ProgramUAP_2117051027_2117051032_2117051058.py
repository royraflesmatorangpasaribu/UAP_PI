import json, requests
import time #waktu
import datetime #tanggal
import os

katabijak = requests.get('https://katanime.vercel.app/api/getbyanime?anime=naruto&page=1')
katabijak2 = requests.get('https://katanime.vercel.app/api/getbyanime?anime=bleach&page=1')

katabijak
katabijak2

katabijak = katabijak.json()
katabijak2=katabijak2.json()

katabijak['result']
katabijak2['result']

def alldata():
  print('----------NARUTO----------')
  for data in katabijak['result']:
    print('Character\t :', data['character'].upper(),'\nQuotes\t\t :', data['indo'],'\n')

      print('----------BLEACH----------')
  for data in katabijak2['result']:
    
    print('Character\t :', data['character'].upper(),'\nQuotes\t\t :', data['indo'],'\n')
