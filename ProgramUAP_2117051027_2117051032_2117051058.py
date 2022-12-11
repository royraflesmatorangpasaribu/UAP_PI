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
    
  elif nama== 6:
    print('\nObito Uchiha')
    for data in katabijak['result']:
      if data['character']=='Obito Uchiha':
        print('Quotes\t :',data['indo'])
    print()
    print(narutoDict['Obito Uchiha'])

  elif nama== 7:
    print('\nItachi Uchiha')
    for data in katabijak['result']:
      if data['character']=='Itachi Uchiha':
        print('Quotes\t :',data['indo'])
    print()
    print(narutoDict['Itachi Uchiha'])

  elif nama== 8:
    print('\nNara Shikamaru')
    for data in katabijak['result']:
      if data['character']=='Nara Shikamaru':
        print('Quotes\t :',data['indo'])
    print()
    print(narutoDict['Nara Shikamaru'])

  else:
    print('\nPilihan Tidak Tersedia!')
    
    
def characterlist2(nama2):
  
  if nama2 == 1:
    print('\nKurosaki Ichigo')
    for data in katabijak2['result']:
      if data['character']=='Kurosaki Ichigo':
        print('Quotes\t :',data['indo'])
    print()
    print(bleachDict['Kurosaki Ichigo'])

  elif nama2== 2:
    print('\nAbarai Renji')
    for data in katabijak2['result']:
      if data['character']=='Abarai Renji':
        print('Quotes\t :',data['indo'])
    print()
    print(bleachDict['Abarai Renji'])

  elif nama2== 3:
    print('\nKuchiki Byakuya')
    for data in katabijak2['result']:
      if data['character']=='Kuchiki Byakuya':
        print('Quotes\t :',data['indo'])
    print()
    print(bleachDict['Kuchiki Byakuya'])

  elif nama2== 4:
    print('\nAizen Sousuke')
    for data in katabijak2['result']:
      if data['character']=='Aizen Sousuke':
        print('Quotes\t :',data['indo'])
    print()
    print(bleachDict['Aizen Sousuke'])
    
    elif nama2== 5:
    print('\nZaraki Kenpachi')
    for data in katabijak2['result']:
      if data['character']=='Zaraki Kenpachi':
        print('Quotes\t :',data['indo'])
    print()
    print(bleachDict['Zaraki Kenpachi'])
    
    elif nama2== 6:
    print('\nUrahara Kisuke')
    for data in katabijak2['result']:
      if data['character']=='Urahara Kisuke':
        print('Quotes\t :',data['indo'])
    print()
    print(bleachDict['Urahara Kisuke'])
    
    elif nama2== 7:
    print('\nUlquiorra Schiffer')
    for data in katabijak2['result']:
      if data['character']=='Ulquiorra Schiffer':
        print('Quotes\t :',data['indo'])
    print()
    print(bleachDict['Ulquiorra Schiffer'])

    else:
    print('\nPilihan Tidak Tersedia!')
    
    narutoDict = {
    "Hatake Kakashi" : "Data diri : \n"+
                       "Kakashi Hatake (派竹 歌々子, Hatake Kakashi) adalah shinobi Konohagakure dari klan Hatake.\n"+
                       "Terkenal sebagai Kakashi si Sharingan (写輪眼のカカシ, Sharingan no Kakashi), \n"+
                       "dia adalah salah satu ninja Konoha yang paling berbakat; secara teratur tampak suka memberi nasihat \n"+
                       "dan berkepemimpinan meskipun dia tidak menyukai tanggung jawab pribadi. Untuk murid-muridnya di Tim 7, \n"+
                       "Kakashi mengajarkan pentingnya kerja sama tim, sebuah pelajaran yang dia terima, bersama dengan Sharingan, \n"+
                       "dari teman masa kecilnya, Obito Uchiha. Setelah Perang Dunia Shinobi Keempat, Kakashi menjadi Hokage Keenam \n"+
                       "(六代目火影, Rokudaime Hokage; Secara harfiah berarti Bayangan Api Keenam).\n"+
                       "\nLink Fandom : https://naruto.fandom.com/id/wiki/Kakashi_Hatake\n",
    "Rock Lee"       : "Data diri : \n"+
                       "Rock Lee (ロック・リー, Rokku Rī) adalah shinobi dari Konohagakure. Sementara ia tidak memiliki keterampilan tertentu \n"+
                       "biasanya terkait dengan kehidupan sebagai seorang ninja, Lee berusaha untuk menebus kekurangannya dengan cara apa pun \n"+
                       "yang dia bisa. Sebagai anggota Tim Guy, ia menerima pelatihan khusus dalam hal ini dari gurunya, Might Guy, \n"+
                       "untuk menjadi seorang ahli taijutsu.\n"+
                       "\nLink Fandom : https://naruto.fandom.com/id/wiki/Rock_Lee\n",
 
