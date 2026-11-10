class Product:
    def __init__(self, MaSP, TenSP, Gia, SoLuong):
        self.MaSP = MaSP
        self.TenSP = TenSP
        self.Gia = Gia
        self.SoLuong = SoLuong

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["MaSP"],
            data["TenSP"],
            data["Gia"],
            data["SoLuong"]
        )

    def to_dict(self):
        return {
            "MaSP": self.MaSP,
            "TenSP": self.TenSP,
            "Gia": self.Gia,
            "SoLuong": self.SoLuong
        }

    def __str__(self):
        return f"{self.MaSP} - {self.TenSP} - {self.Gia} - {self.SoLuong}"