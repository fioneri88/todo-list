#Melihat daftar
def read():
   i = 0
   print("")
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
def create():
   file = open(".txt", "a")
   file.write(input(" "*3 + "Masukan daftar: "))
   file.write("\n")
   #menambahkan linebreak agar input terindex
   #oleh list
   file.close()
   read()

#Mengedit daftar
def update():
   n = int(input(" "*3 + "Masukan ID: "))
   file = open("list.txt", "r")
   ls = file.readlines()
   ls[n] = input(" "*3 + "Masukan daftar baru: ")
   ls[n] += "\n"
   file.close()
   
   file = open("list.txt", "w")
   file.writelines(ls)
   file.close()
   read()

#Menghapus daftar
def delete():
   n = input("   Masukan nama daftar: ")
   file = open("list.txt", "r")
   ls = file.readlines()
   file.close()
   
   file = open("list.txt", "w")
   for line in ls:
      if line.strip("\n") != n:
         file.write(line)
   file.close()
   read()

#Menghapus semua daftar
def delete_all():
   file = open("list.txt", "r+")
   file.seek(0)
   file.truncate()
   file.close()

#menampilkan menu
def menu():
   print("""
                   __     
      ____  ____  / /____ ___ _ 
     / __ \/ __ \/ __/ _ \ ___ _ 
    / / / / /_/ / /_/ ___/ ___ _ 
   /_/ /_/\____/\__/\___/ ___ _ 
   by: fioneri.

   [0] Tambahkan daftar 
   [1] Lihat daftar 
   [2] Edit daftar 
   [3] Hapus daftar 
   [4] Hapus semua daftar 
   [5] Keluar
   """)

def main_menu(): 
   choice = int(input(" "*3 + "→ "))
   if choice == 0:
     create()
   elif choice == 1:
     read()
   elif choice == 2:
     update()
   elif choice == 3:
     delete()
   elif choice == 4:
     delete_all()
   elif choice == 5:
     exit()
   else:
     print("Input tidak tersedia")

menu()
if __name__ == "__main__":
   while True:
      main_menu()