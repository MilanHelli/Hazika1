

class Csapat:
    def __init__(self, nev, projekt, szerepkor):
        self._nev = nev
        self._projekt = projekt
        self._szerepkor = szerepkor
        print(self)

    def __str__(self):
            return f"-- Developer létrehozva--. --\n {self._nev} a {self._projekt}-en dolgozik {self._szerepkor} szerepkörben."

    def __eq__(self,masodikprojekt):
        return self._projekt == masodikprojekt._projekt

    def segito (self,  masodiknev):
        return self._nev < masodiknev._nev and self == masodiknev

dolgozok_list = []

dolgozok_list.append(Csapat("Ricsi", "SolArch", "Frontend"))
dolgozok_list.append(Csapat("Angéla", "ZerTeng", "Tesztelő"))
dolgozok_list.append(Csapat("Peti", "KefERP", "Backend"))
dolgozok_list.append(Csapat("Éva", "KefERP", "Frontend"))

for valtozo in dolgozok_list:
    for valtozo2 in dolgozok_list:
        if valtozo.segito(valtozo2):
            print(f"\n{valtozo._nev} és {valtozo2._nev} dolgoznak egy projekten.")

