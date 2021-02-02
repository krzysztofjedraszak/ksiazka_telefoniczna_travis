import main
import pytest

def test_klasa_osoba():
    imie="Jan"
    nazwisko="Nowak"
    nr_tel="123456789"

    obj=main.Osoba(imie,nazwisko,nr_tel)

    assert obj.imie==imie and obj.nazwisko==nazwisko and obj.nr_tel==nr_tel