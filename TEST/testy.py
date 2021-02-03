import main
import pytest

def test_klasa_osoba():
    imie="Jan"
    nazwisko="Nowak"
    nr_tel="123456789"

    obj=main.Osoba(imie,nazwisko,nr_tel)

    assert obj.imie==imie and obj.nazwisko==nazwisko and obj.nr_tel==nr_tel

def test_klasa_ksiazka_telefoniczna():
    obj=main.Ksiazka_telefoniczna()

    assert hasattr(obj,"lista")

def test_dodaj():
    obj=main.Ksiazka_telefoniczna()
    ilosc_przed= len(obj.lista)
    obj.dodaj("Pawel","Piotr","987654321")
    ilosc_po= len(obj.lista)

    assert ilosc_przed+1==ilosc_po

def test_wyszukaj(capsys):
    obj=main.Ksiazka_telefoniczna()
    obj.dodaj("Pawel", "Piotr", "987654321")

    obj.wyszukaj("Pawel", "Piotr", "987654321")
    out,err=capsys.readouterr()

    assert out== "Dodano!\nTaka osoba znajduje sie w ksiazce\n"
