def input_data(df, dz):
    nim = input("Masukan NIM : ")
    nama = input("Masukan Nama : ")
    tugas = input("Masukan Nilai Tugas : ")
    uts = input("Masukan Nilai UTS : ")
    uas = input("Masukan Nilai UAS : ")

    dz.tambah_data(df, nim, nama, tugas, uts, uas)
