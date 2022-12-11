# modules
class Admin:
  admCount = 0
  
  def __init__(this, name, npm):
      this.name = name
      this.npm = npm
      Admin.admCount += 1

  def displayCount(this):
      print (Admin.admCount)

  def displayAdmin(this):
      print ("\t",this.name,"-",this.npm,"\t")
      
      
def pengembang():
  print("")
  print("===================================================")
  print("|--\t\tProgram UAP PI \t\t\t--|")
  print("===================================================")
  print("")
  print("----        Selamat Datang Program Kami       ----")
  adm1.displayAdmin()
  adm2.displayAdmin()
  adm3.displayAdmin()
  print("\tTotal Developers : ",Admin.admCount)
  print("==================================================")
