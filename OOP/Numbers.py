class PhanSo():
    def __init__(self,TuSo,MauSo):
        self.TuSo= TuSo
        self.MauSo = MauSo
    def __float__(self):
        return self.TuSo/self.MauSo  
    def add(ps1,ps2):
        TuSoMoi= ps1.TuSo * ps2.MauSo + ps2.TuSo *ps1.MauSo
        MauSoMoi= ps1.MauSo* ps2.MauSo
        return TuSoMoi/MauSoMoi
    def nhan(ps1,ps2):
        TuSoMoi= ps1.TuSo * ps2.TuSo
        MauSoMoi= ps1.MauSo* ps2.MauSo
        return TuSoMoi/MauSoMoi
    def tru(ps1,ps2):
        TuSoMoi= ps1.TuSo * ps2.MauSo - ps2.TuSo *ps1.MauSo
        MauSoMoi= ps1.MauSo * ps2.MauSo
        return TuSoMoi/MauSoMoi
    