# UAS PEMROGRAMAN
## Membuat Package and Module

>✓ daftar_nilai.py berisi modul untuk: tambah_data, ubah_data, hapus_data, dan cari_data
✓ view_nilai.py berisi modul untuk: cetak_daftar_nilai, cetak_hasil_pencarian
✓ input_nilai.py berisi modul untuk: input_data yang meminta pengguna memasukkan data.
✓ main.py berisi program utama (menu pilihan yang memanggil semua menu yang ada)

### daftar_nilai.py
```python
def tambah_data(df, nim, nama, tugas, uts, uas):
    print("Menambahkan Data..")
    akhir = ((int(tugas) / 100*30) + (int(uts)/100*35) + (int(uas) / 100*35))
    df[nim] = {"nama": nama, "tugas": tugas,
               "uts": uts, "uas": uas, "akhir": akhir}
    print("Data Berhasil tersimpan")


def Ubah_data(df):
    found = 0
    nama = input("Cari Data Mahasiswa yang ingin di ubah : ")
    for i, j in df.items():
        if ((df.get(i)).get('nama') == nama):
            found = i
    if (found == 0):
        print("Data tidak ada")
    else:
        nama = input("Masukan Nama         : ")
        if nama == "":
            nama = df[found]['nama']
        tugas = input("Masukan Nilai Tugas  : ")
        if tugas == "":
            tugas = df[found]['tugas']
        uts = input("Masukan Nilai UTS    : ")
        if uts == "":
            uts = df[found]['uts']
        uas = input("Masukan Nilai UAS    : ")
        if uas == "":
            uas = df[found]['uas']
        akhir = ((int(tugas) / 100*30) +
                 (int(uts)/100*35) + (int(uas) / 100*35))
        df[found] = {"nama": nama, "tugas": tugas,
                          "uts": uts, "uas": uas, "akhir": akhir}
        print("Berhasil Mengubah Data")


def Hapus_data():
    print("Hapus Data..")


def Cari_data(df, nama):
    x, found = 0, 0
    for i, j in df.items():
        x += 1
        if ((df.get(i)).get('nama').startswith(nama)):
            found += 1
            print('| {0:^3}| {1:11} | {2:<17} | {3:7} | {4:4} | {5:3} | {6:6.2f} |'.format(
                1, i, df[i]["nama"], df[i]["tugas"], df[i]["uts"], df[i]["uas"], df[i]["akhir"]))
    if (found == 0):
        print("Data tidak ada")
```

### view_nilai.py
```python
def cetak_data(df, dn):
    print("mencetak hasil cari nilai...")
    nama = input("Cari Data nilai berdasarkan Nama : ")
    dn.Cari_data(df, nama)

def lihatdata(df):
    if df.items():
        print("Daftar Nilai")
        print("=" * 78)
        print("| NO | NIM            |       NAMA       |  TUGAS  |  UTS  |  UAS  |  Akhir  |")
        print("=" * 78)
        x = 1
        for i, j in df.items():
            print('| {0:^3}| {1:11} | {2:<17} | {3:7} | {4:4} | {5:3} | {6:7.2f} |'.format(
                x, i, df[i]["nama"], df[i]["tugas"], df[i]["uts"], df[i]["uas"], df[i]["akhir"]))
            x += 1
        i = 0

        print("=" * 78)
    else:
        print("Daftar Nilai")
        print("=" * 78)
        print("| NO | NIM            |       NAMA       |  TUGAS  |  UTS  |  UAS  |  Akhir  |")
        print("=" * 78)
        print("|                                TIDAK ADA DATA                              |")
        print("=" * 78)
```

### input_nilai
```python
def input_data(df, dz):
    nim = input("Masukan NIM : ")
    nama = input("Masukan Nama : ")
    tugas = input("Masukan Nilai Tugas : ")
    uts = input("Masukan Nilai UTS : ")
    uas = input("Masukan Nilai UAS : ")

    dz.tambah_data(df, nim, nama, tugas, uts, uas)
```

### main.py
```python
import view.view_nilai as view
import view.input_nilai as inp
import model.daftar_nilai as dn
DaftarNilai = {}
while True:
    menu = input(
        "Pilih Menu : L:Lihat T:Tambah U:Ubah H:Hapus C:Cari X:Keluar : ").capitalize()
    if (menu == "L"):
        view.lihatdata(DaftarNilai)
    if (menu == "T"):
        inp.input_data(DaftarNilai, dn)
    if (menu == "U"):
        dn.Ubah_data(DaftarNilai)
    if (menu == "H"):
        dn.Hapus_data()
    if (menu == "C"):
        view.cetak_data(DaftarNilai, dn)
    if (menu == "X"):
        break
```


## Output Package and Module

**Tambah dan Lihat Data**
![1](https://user-images.githubusercontent.com/116176746/212461846-48a5d619-98bd-4c13-ab6d-bf1c968e95df.png)

**Ubah Data**
![2](https://user-images.githubusercontent.com/116176746/212461894-955161e5-d0d8-4a08-8bfa-10307e437de0.png)

**Cari Data**
![3](https://user-images.githubusercontent.com/116176746/212461907-1012d65d-aef8-417b-ac54-0e17f2173a57.png)

**Keluar Program**
![4](https://user-images.githubusercontent.com/116176746/212461926-6c7308fc-c56e-4184-8bf1-ceb4d2d3fbaf.png)    
