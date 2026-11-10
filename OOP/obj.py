class Student:
    def __init__(self, MaSV, HoTen, Lop, Diem):
        self.MaSV = MaSV
        self.HoTen = HoTen
        self.Lop = Lop
        self.Diem = Diem

    def an_com(self):
        print(self.HoTen, "Dang an com")

    def xep_loai(self):
        if self.Diem >= 9:
            return "Xuat sac"
        elif self.Diem >= 8:
            return "Gioi"
        elif self.Diem >= 7:
            return "Kha"
        else:
            return "Trung binh"

    @classmethod
    def thong_bao(cls):
        print("Warning")

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['Msv'],
            data['HoTen'],
            data['Lop'],
            data['Diem']
        )

    def to_dict(self):
        return {
            'Msv': self.MaSV,
            'HoTen': self.HoTen,
            'Lop': self.Lop,
            'Diem': self.Diem
        }


class StudentAptech(Student):
    def __init__(self, MaSV, HoTen, Lop, Diem):
        super().__init__(MaSV, HoTen, Lop, Diem)

    def lap_trinh(self):
        print(self.HoTen, "Dang lap trinh")