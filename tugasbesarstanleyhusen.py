my_file = open("ListMenu.txt", "r") #r untuk membaca file txt
count = 0

listmakanan = []
listminuman = []
listsnack = []

while True:
    count += 1  
    data = my_file.readline()
    if not data:
        break
    if count == 1 :
        listmakanan = data.rstrip().split(",")
    elif count == 2 :
        listminuman = data.rstrip().split(",")
    elif count == 3 :
        listsnack = data.rstrip().split(",")

def lihatData():
    print("Daftar Menu :")
    data = zip(listmakanan, listminuman, listsnack)
    print ("{:<5} {:<18} {:<18} {:<17}".format('No','Makanan','Minuman','Snack'))
    for index, v in enumerate(data):
        makanan, minuman, snack = v
        print ("{:<5} {:<18} {:<18} {:<10}".format( index+1, makanan, minuman, snack))

def tambahData(makanan,minuman,snack):
    listmakanan.append(makanan)
    listminuman.append(minuman)
    listsnack.append(snack)

def hapusData(hapus):
    listmakanan.pop(hapus - 1)
    listminuman.pop(hapus - 1)
    listsnack.pop(hapus - 1)
    
def ubahData(ubah, makanan, minuman, snack):
    listmakanan[ubah - 1] = makanan
    listminuman[ubah - 1] = minuman
    listsnack[ubah - 1] = snack
    
listMenu = ["1.Menambah Menu", "2.Menampilkan Menu", "3.Mengubah Menu" ,"4.Menghapus Menu"]

while True :
    print("Daftar Menu :")
    for x in listMenu :
        print(x)
    print("Pilih Menu :")
    menu =int(input())
    if menu == 1 :
        print("Masukkan makanan :")
        makanan =str(input())
        print("Masukkan minuman :")
        minuman =str(input())
        print("Masukkan snack :")
        snack =str(input())
        tambahData(makanan, minuman, snack)
    elif menu == 2 :
        lihatData()
    elif menu == 3 :
        print("Data Yang Akan Diubah")
        ubah =int(input())
        print("Masukkan makanan :")
        makanan =str(input())
        print("Masukkan minuman :")
        minuman =str(input())
        print("Masukkan snack :")
        snack =str(input())
        ubahData(ubah, makanan, minuman, snack)
    elif menu == 4 :
        print("Data Yang Akan Dihapus")
        hapus =int(input())
        hapusData(hapus)
    else :
        break
  
   
