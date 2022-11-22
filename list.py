# membuat 5 list dengan type data yang berbeda

listData = ["Teknik Informatika", "UPB", 650000, True, "Fakultas Teknik"]

 ###########################
 # mengakses element list #
 #########################

 # menampilkan element ke-3 pada sebuah list
print(listData[2])

 # menampilkan elemen ke-2 sampai ke-4
print(listData[1:4])

 # menampilkan elemen terakhir
print(listData[4])
 # atau bisa juga seperti ini
print(listData[-1])

 ##########################
 # Mengubah element list #
 ########################

 # Merubah elemen ke-4 dengan nilai lain
listData[3] = False
print(listData)

 # Merubah elemen ke-4 sampai dengan terakhir degan nilai lain
listData[3:5] = [True, "TI22A1"]
print(listData)

 ##########################
 # Menambah element list #
 ########################

 # membuat listA dan diisi oleh element yang ada di listData
listA = listData

 # membuat list B dengan element masih kosong
listB = []

 # mengambil 2 nilai dari listA lalu simpan ke listB
listB = listA[0:2]
print(listB)

 # Menambahkan list B dengan nilai string
listB.append("Fakultas Teknik")
print(listB)

 # Menambahkan list B dengan 3 nilai
listB.extend(["Teknik Sipil", "Teknik Lingkungan", "Teknik Industri"])
print(listB)

 # Menggabungkan list B dengan listA
listGabungan = listA + listB
print(listGabungan)