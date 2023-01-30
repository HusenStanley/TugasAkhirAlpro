my_file = open("ListMenu.txt", "r") #r untuk membaca file txt #my_file berfungsi untuk variabel membuka file
count = 0

listmakanan = []
listminuman = []
listsnack = []

while True:
    count += 1  
    data = my_file.readline() #readline untuk membaca isi file perbaris dan akan mengembalikan nilai berupa list
    if not data:
        break
    if count == 1 :
        listmakanan = data.rstrip().split(",") #rstrip untuk menghilangkan enter
    elif count == 2 :
        listminuman = data.rstrip().split(",") #split untuk memberi jarak
    elif count == 3 :
        listsnack = data.rstrip().split(",")

def lihatData():
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    print("|< ================= * Daftar Menu * ================ >|")
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    data = zip(listmakanan, listminuman, listsnack) #zip untuk menggabungkan menjadi 1 list
    print ("|{:<5}|{:<15}|{:<15}|{:<16}|".format('  No','    Makanan','    Minuman','     Snack'))
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    for index, v in enumerate(data): #enumerate untuk mendapatkan index dari list data
        makanan, minuman, snack = v
        print ("|{:<5}|{:<15}|{:<15}|{:<16}|".format( index+1, makanan, minuman, snack))

def tambahData(makanan,minuman,snack):
    listmakanan.append(makanan) #append untuk menambah data
    listminuman.append(minuman)
    listsnack.append(snack)
    stringmakanan = ",".join(listmakanan)
    stringminuman = ",".join(listminuman)
    stringsnack = ",".join(listsnack) 
    my_file = open("ListMenu.txt", "w") #w untuk membuka txt dengan fungsi write pada file
    my_file.write(stringmakanan + "\n") #\n untuk enter
    my_file.write(stringminuman + "\n")
    my_file.write(stringsnack)
    my_file.close()

def hapusData(hapus):
    listmakanan.pop(hapus - 1) #Pop Berfungsi untuk menghapus
    listminuman.pop(hapus - 1)
    listsnack.pop(hapus - 1)
    stringmakanan = ",".join(listmakanan)
    stringminuman = ",".join(listminuman)
    stringsnack = ",".join(listsnack) 
    my_file = open("ListMenu.txt", "w") #my_file berfungsi untuk membuka file  #w untuk membuka txt dengan fungsi write pada file
    my_file.write(stringmakanan + "\n")
    my_file.write(stringminuman + "\n")
    my_file.write(stringsnack)
    my_file.close()
    
def ubahData(ubah, makanan, minuman, snack):
    listmakanan[ubah - 1] = makanan
    listminuman[ubah - 1] = minuman
    listsnack[ubah - 1] = snack
    stringmakanan = ",".join(listmakanan)
    stringminuman = ",".join(listminuman)
    stringsnack = ",".join(listsnack) 
    my_file = open("ListMenu.txt", "w") #my_file berfungsi untuk membuka file #w untuk membuka txt dengan fungsi write pada file
    my_file.write(stringmakanan + "\n")
    my_file.write(stringminuman + "\n")
    my_file.write(stringsnack)
    my_file.close()
    
    
listMenu =["  |1. Menambah Menu     |", "  |2. Menampilkan Menu  |", "  |3. Mengubah Menu     |" ,"  |4. Menghapus Menu    |"]

while True :
    print("  |=====================|")
    print("  |<   * List Menu *   >|")
    print("  |=====================|")
    for x in listMenu :
        print(x)
    print("  |=====================|")
    print("  |    * Pilih Menu *   |")
    print("  |=====================|")
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
        print("Menu Yang Akan Diubah")
        ubah =int(input())
        print("Masukkan makanan :")
        makanan =str(input())
        print("Masukkan minuman :")
        minuman =str(input())
        print("Masukkan snack :")
        snack =str(input())
        ubahData(ubah, makanan, minuman, snack)
    elif menu == 4 :
        print("Menu Yang Akan Dihapus")
        hapus =int(input())
        hapusData(hapus)
    else :
        break
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")

  
   
