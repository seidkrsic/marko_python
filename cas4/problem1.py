


class Proizvod: 
    def __init__(self, ime, kolicina, cijena): 
        self.ime = ime 
        self.kolicina = kolicina 
        self.cijena = cijena 

    # odredi cijenu 
    def odredi_cijenu(self, ukupno_proizvoda):
        # ako ima <=10 proizvoda ---- nema popust 
        if ukupno_proizvoda <=10: 
            print(f"Cijena je: {ukupno_proizvoda * self.cijena}") 
        # ako ima od 10 do 99 --- onda ima popust od 10% 
        elif ukupno_proizvoda >10 and ukupno_proizvoda < 100:
            print(f"Cijena je: {ukupno_proizvoda * self.cijena * 0.9}")
        else:
            (f"Cijena je: {ukupno_proizvoda * self.cijena * 0.8}")
        # a ako ima preko 100 ---- onda ima popust 20% 

    # obavi kupovinu 
    def obavi_kupovinu(self, ukupno_proizvoda): 
        if ukupno_proizvoda <= self.kolicina: 
            self.kolicina = self.kolicina - ukupno_proizvoda
            print("Kupovina uspjesna!") 
            print(f"Na zalihama ostalo jos {self.kolicina}")
        else: 
            print(f"Nemamo toliko proizvoda") 



sir = Proizvod("Sir", 20, 2)  
sir.obavi_kupovinu(10) 
sir.odredi_cijenu(20)