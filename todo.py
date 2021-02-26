#Melihat daftar
#Show lists
def read():
   i = 0
   print(" "*3 + "Daftar: ")
   file = open("list.txt", "r")
   ls = file.readlines()
   for line in ls:
      if line != "\n":
         print("  ", [i], line.strip())
         #menghapus linebreak pada list
         i +=1
   file.close()
   print("")

#Menambahkan daftar
#Add list
def create():
   file = open("list.txt", "a")
   new_list = file.write(input(" "*3 + "Masukan daftar: "))
   file.write("\n")
   #menambahkan linebreak agar input terindex
   #oleh list
   file.close()
   read()

#Mengedit daftar
#Edit lists
def update():
   n = int(input(" "*3 + "Masukan ID: "))
   file = open("list.txt", "r")
   ls = file.readlines()
   ls[n] = input(" "*3 + "Masukan daftar baru: ")
   ls[n] += "\n"
   file = open("list.txt", "w")
   file.writelines(ls)
   file.close()
   read()

#Menghapus daftar
#delete list
def delete():
   n = int(input(" "*3 + "Masukan ID:  "))
   file = open("list.txt", "r")
   ls = file.readlines()
   del ls[n]
   file = open("list.txt", "w+")
   for line in ls:
      file.write(line)
   file.close()
   read()


#Menghapus semua daftar
#delete all lists
def delete_all():
   file = open("list.txt", "r+")
   file.seek(0)
   file.truncate()
   file.close()
   print(" "*3 + "Semua daftar telah di hapus")
   print("")

#menampilkan menu
#Show menu
def menu():
   print("""
      __            __         ___      __
     / /_____  ____/ /___     / (_)____/ /_
    / __/ __ \/ __  / __ \   / / / ___/ __/
   / /_/ /_/ / /_/ / /_/ /  / / (__  ) /_
   \__/\____/\__,_/\____/  /_/_/____/\__/
   by: fioneri.

   [T] Tambahkan daftar 
   [L] Lihat daftar 
   [E] Edit daftar 
   [H] Hapus daftar 
   [S] Hapus semua daftar 
   [Q] Keluar
   """)

#Main menu
def main_menu(): 
   choice = input(" "*3 + "Masukan perintah → ")
   print("")
   if choice == "T" or choice == "t":
     create()
   elif choice == "L" or choice == "l":
     read()
   elif choice == "E" or choice == "e":
     update()
   elif choice == "H" or choice == "h":
     delete()
   elif choice == "S" or choice == "s":
     delete_all()
   elif choice == "Q" or choice == "q":
     exit()
   else:
     print(" "*3 + "Perintah tidak tersedia")

menu()
if __name__ == "__main__":
   while True:
      main_menu()
