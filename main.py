class Osoba():
    def __init__(self,imie,nazwisko,nr_tel):
        self.imie=imie
        self.nazwisko=nazwisko
        self.nr_tel=nr_tel

class Ksiazka_telefoniczna():
    def __init__(self):
        self.lista=[]

    def dodaj(self,imie,nazwisko,nr_tel):

        dodana_osoba=Osoba(imie,nazwisko,nr_tel)
        self.lista.append(dodana_osoba)
        print("Dodano!")

    def wyszukaj(self,imie,nazwisko,nr_tel):
        for i in self.lista:
            if imie==i.imie and nazwisko==i.nazwisko and nr_tel==i.nr_tel:
                print("Taka osoba znajduje sie w ksiazce")

    def usun(self,imie,nazwisko,nr_tel):
        for i in self.lista:
            if imie==i.imie and nazwisko==i.nazwisko and nr_tel==i.nr_tel:
                self.lista.remove(i)
                print("Usunieto!")


# print("Podaj imie osoby ktora chcesz dodac")
# imie=input()
# print("Podaj nazwisko osoby ktora chcesz dodac")
# nazwisko = input()
# print("Podaj numer telefonu osoby ktora chcesz dodac")
# nr_tel = input()

