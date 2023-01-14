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