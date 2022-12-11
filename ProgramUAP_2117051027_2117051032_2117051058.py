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
      
     "Gaara"         : "Data diri : \n"+
                       "Gaara (我愛羅, Gaara) adalah shinobi dari Sunagakure. Shukaku disegel ke dalam tubuhnya pada hari ia dilahirkan, \n"+
                       "prosedur yang menyebabkan kematian ibunya. Dianggap sebagai monster oleh desa dan dengan tidak ada yang mencintainya, \n"+
                       "Gaara menjadi benci pada dunia dan mulai hanya mengandalkan kekuatannya sendiri, dengan mendapatkan gelar \n"+
                       "Gaara Sang Pasir Terjun (砂瀑の我愛羅).\n"+
                       "\nLink Fandom : https://naruto.fandom.com/id/wiki/Gaara\n",
    "Naruto Uzumaki" : "Data diri : \n"+
                       "Naruto Uzumaki (渦巻 鳴門, Uzumaki Naruto) adalah shinobi dari Konohagakure. Dia menjadi jinchūriki dari Ekor Sembilan \n"+
                       "pada hari kelahirannya — sebuah nasib yang menyebabkan dia dijauhi oleh sebagian besar penduduk Konoha sepanjang masa kecilnya. \n"+
                       "Setelah bergabung dengan Tim Kakashi, Naruto bekerja keras untuk mendapatkan pengakuan desa sambil mengejar mimpinya \n"+
                       "untuk menjadi Hokage.\n"+
                       "\nLink Fandom : https://naruto.fandom.com/id/wiki/Naruto_Uzumaki\n",
    "Haku"           : "Data diri : \n"+
                       "Haku (白, Haku) dalah seorang yatim piatu dari Negara Air, dan keturunan klan Yuki. \n"+
                       "Ia kemudian menjadi shinobi setelah bertemu Zabuza Momochi yang menjadi mitranya, dan akhirnya menjadi Ninja Bayaran.\n"+
                       "\nLink Fandom : https://naruto.fandom.com/id/wiki/Haku\n",
    "Obito Uchiha"   : "Data diri : \n"+
                       "Obito Uchiha (うちはオビト, Uchiha Obito) adalah anggota klan Uchiha dari Konohagakure. Dia diyakini telah meninggal selama Perang \n"+
                       "Dunia Shinobi Ketiga, satu-satunya warisan yang masih ada adalah Sharingan yang dia berikan kepada rekan setimnya, Kakashi Hatake.\n"+
                       "\nLink Fandom : https://naruto.fandom.com/id/wiki/Obito_Uchiha\n",
    "Itachi Uchiha"  : "Data diri : \n"+
                       "Itachi Uchiha (団扇 鼬, Uchiha Itachi) adalah seorang anak ajaib klan Uchiha dari Konohagakure. \n"+
                       "Ia menjadi seorang penjahat internasional setelah membunuh seluruh klan, dan hanya menyelamatkan adiknya, Sasuke.\n"+
                       "\nLink Fandom : https://naruto.fandom.com/id/wiki/Itachi_Uchiha\n",
    "Nara Shikamaru" : "Data Diri : \n"+
                       "Shikamaru Nara (奈良シカマル, Nara Shikamaru) adalah anggota Klan Nara dari Konohagakure. Meskipun malas adalah sifat alaminya, \n"+
                       "Shikamaru memiliki kecerdasan langka dan konsisten yang memungkinkan dia untuk menang dalam pertempuran.\n"+
                       "\nLink Fandom : https://naruto.fandom.com/id/wiki/Shikamaru_Nara\n"
    
}
