import unittest
import src.projekt as projekt
from src.projekt import Osoba,Ksiazka
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker
from tkinter import  StringVar, IntVar
class testy(unittest.TestCase):

    def testDodanieKsiązki(self):
        """Wykonaj test dodawania ksiazki"""
        projekt.tytul = 'tytul'
        projekt.autor = 'autor'
        projekt.rok = 100
        projekt.sesja = sesja
        projekt.AddKs()
        wynik = sesja.query(Ksiazka).filter(Ksiazka.tytul == 'tytul', Ksiazka.autor == 'autor', Ksiazka.rok == 100).all()
        self.assertEqual(True, len(wynik) >= 1 , "Poprwnie dodał Książke")

    def testDodanieOsoby(self):
        """Wykonaj test dodawania osoby"""
        projekt.imie = 'imie'
        projekt.nazwisko = 'nazwisko'
        projekt.email = 'osoba@mail'
        projekt.sesja = sesja
        projekt.AddOs()
        wynik = sesja.query(Osoba).filter(Osoba.imie == 'imie', Osoba.nazwisko == 'nazwisko', Osoba.email == 'osoba@mail').all()
        self.assertEqual(True, len(wynik) >= 1 , "Poprwnie dodał osobe")
        
    def testDodawanieWyporzyczenia(self):
        """Wykonaj test wyporzyczania"""
        projekt.selected_imie = 'imie'
        projekt.selected_nazwisko = 'nazwisko'
        projekt.selected_email = 'osoba@mail'
        projekt.selected_tytul = 'tytul'
        projekt.selected_autor = 'autor'
        projekt.selected_rok = 100
        projekt.sesja = sesja
        projekt.AddWyp()
        wyniko = sesja.query(Osoba).filter(Osoba.imie == 'imie', Osoba.nazwisko == 'nazwisko', Osoba.email == 'osoba@mail').all()
        wynikk = sesja.query(Ksiazka).filter(Ksiazka.tytul == 'tytul', Ksiazka.autor == 'autor', Ksiazka.rok == 100).all()
        self.assertEqual(True, wynikk[0].wyporzycza == wyniko[0].id , "Poprwnie wyporzycza")

    def testDodawanieZwrotu(self):
        """Wykonaj test zwracania"""
        projekt.selected_imie = 'imie'
        projekt.selected_nazwisko = 'nazwisko'
        projekt.selected_email = 'osoba@mail'
        projekt.selected_tytul = 'tytul'
        projekt.selected_autor = 'autor'
        projekt.selected_rok = 100
        projekt.sesja = sesja
        projekt.AddZw()
        wyniko = sesja.query(Osoba).filter(Osoba.imie == 'imie', Osoba.nazwisko == 'nazwisko', Osoba.email == 'osoba@mail').all()
        wynikk = sesja.query(Ksiazka).filter(Ksiazka.tytul == 'tytul', Ksiazka.autor == 'autor', Ksiazka.rok == 100).all()
        self.assertEqual(True, wynikk[0].wyporzycza != wyniko[0].id , "Poprwnie zwraca")

    def testUsuniecieKsiązki(self):
        """Wykonaj test usuwanie ksiazki"""
        projekt.tytul = 'tytul'
        projekt.autor = 'autor'
        projekt.rok = 100
        projekt.sesja = sesja
        projekt.DelKs()
        wynik = sesja.query(Ksiazka).filter(Ksiazka.tytul == 'tytul', Ksiazka.autor == 'autor', Ksiazka.rok == 100).all()
        self.assertEqual(True, len(wynik) < 1 , "Poprwnie usunoł Książke")

    def testUsuniecieOsoby(self):
        """Wykonaj test usuwanie osoby"""
        projekt.imie = 'imie'
        projekt.nazwisko = 'nazwisko'
        projekt.email = 'osoba@mail'
        projekt.sesja = sesja
        projekt.DelOs()
        wynik = sesja.query(Osoba).filter(Osoba.imie == 'imie', Osoba.nazwisko == 'nazwisko', Osoba.email == 'osoba@mail').all()
        self.assertEqual(True, len(wynik) < 1 , "Poprwnie usunoł osobe")


if __name__ == "__main__":
    Base = declarative_base()
    engine = create_engine('sqlite:///wyklad.db', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sesja = Session()
    unittest.main()