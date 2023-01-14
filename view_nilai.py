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