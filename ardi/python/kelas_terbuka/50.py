'''*args'''


#memasukkan data/argumen

def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
    
fungsi("ucup",120,150)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")


fungsi(["ucup", 120, 150])


# *args

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")


fungsi("ucup", 120, 150)


#studi kasus

def tambah(*data):
    output = 0
    for angka in data:
        output +=angka
        
    return output
    
    
hasil = tambah(1,2,3,4,5,6,7,8,9)
print (f"hasil = {hasil}")
hasil = tambah(10,20,20)
print (f"hasil = {hasil}")