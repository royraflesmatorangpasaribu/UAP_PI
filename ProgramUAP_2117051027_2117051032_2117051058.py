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
    
def characterlist(nama):
  if nama == 1:
    print('\nHatake Kakashi')
    for data in katabijak['result']:
      if data['character']=='Hatake Kakashi':
        print('Quotes\t :',data['indo'])
    print()
    print(narutoDict["Hatake Kakashi"])
    
  elif nama== 2:
    print('\nRock Lee')
    for data in katabijak['result']:
      if data['character']=='Rock Lee':
        print('Quotes\t :',data['indo'])
    print()
    print(narutoDict['Rock Lee'])
    
  elif nama== 3:
    print('\nGaara')
    for data in katabijak['result']:
      if data['character']=='Gaara':
        print('Quotes\t :',data['indo'])
    print()
    print(narutoDict['Gaara'])
    
  elif nama== 4:
    print('\nNaruto Uzumaki')
    for data in katabijak['result']:
      if data['character']=='Naruto Uzumaki':
        print('Quotes\t :',data['indo'])
    print()
    print(narutoDict['Naruto Uzumaki'])
    
  elif nama== 5:
    print('\nHaku')
    for data in katabijak['result']:
      if data['character']=='Haku':
        print('Quotes\t :',data['indo'])
    print()
    print(narutoDict['Haku'])
