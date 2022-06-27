class Barang():
    harga_barang = 0
    def __init__(self,input_nama):
        self.nama = input_nama
    
    def hargaB(self,input_harga):
        self.harga_barang += input_harga
        
    def total(self):
        if self.harga_barang < 100000:
            print('dapat diskon')
        else :
            print('tidak dapat diskon')
            
barang_1 = Barang("Indomie")
barang_1.hargaB(3500)
barang_1.total()