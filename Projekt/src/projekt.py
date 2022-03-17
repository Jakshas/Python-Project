from xml.dom.minidom import TypeInfo
from sqlalchemy.sql.expression import null, table
from tkinter import Tk, Label, StringVar, IntVar, ttk
import tkinter as tk
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, ForeignKey, String, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker, decl_api


Base = declarative_base()

class Osoba(Base):
    '''Klasa dla tabeli Osoba'''
    __tablename__ = 'Osoba'
    id = Column(Integer, primary_key=True)
    imie = Column(String(20), nullable=False)
    email = Column(String)
    nazwisko = Column(String(20), nullable=False)
    ksiazki = relationship('Ksiazka')


class Ksiazka(Base):
    '''Klasa dla tabeli Ksiazka'''
    __tablename__ = "Ksiazka"
    id = Column(Integer, primary_key=True)
    tytul = Column(String(20), nullable=False)
    autor = Column(String(40), nullable=False)
    rok = Column(Integer)
    wyporzycza = Column(Integer, ForeignKey("Osoba.id"))


def AddKsPopUp()->None:
    '''Wyświetla okno do dodania nowych ksiazek'''
    top = tk.Toplevel(root)
    name_label = tk.Label(top, text='Tytul', font=('calibre', 10, 'bold'))
    name_entry = tk.Entry(top, textvariable=tytul_var,
                          font=('calibre', 10, 'normal'))
    name_label.grid(row=0, column=0)
    name_entry.grid(row=0, column=1)
    name_label = tk.Label(top, text='Autor', font=('calibre', 10, 'bold'))
    name_entry = tk.Entry(top, textvariable=autor_var,
                          font=('calibre', 10, 'normal'))
    name_label.grid(row=1, column=0)
    name_entry.grid(row=1, column=1)
    name_label = tk.Label(top, text='Rok', font=('calibre', 10, 'bold'))
    name_entry = tk.Entry(top, textvariable=rok_var,
                          font=('calibre', 10, 'normal'))
    name_label.grid(row=2, column=0)
    name_entry.grid(row=2, column=1)
    Bdodajos = tk.Button(top, text="Dodaj Książkę", command=AddKs)
    Bdodajos.grid(row=3, column=0, columnspan=2)


def AddOsPopUp()->None:
    '''Wyświetla okno do dodania nowych osób'''
    top = tk.Toplevel(root)
    name_label = tk.Label(top, text='Imie', font=('calibre', 10, 'bold'))
    name_entry = tk.Entry(top, textvariable=imie_var,
                          font=('calibre', 10, 'normal'))
    name_label.grid(row=0, column=0)
    name_entry.grid(row=0, column=1)
    name_label = tk.Label(top, text='Nazwisko', font=('calibre', 10, 'bold'))
    name_entry = tk.Entry(top, textvariable=nazwisko_var,
                          font=('calibre', 10, 'normal'))
    name_label.grid(row=1, column=0)
    name_entry.grid(row=1, column=1)
    name_label = tk.Label(top, text='Email', font=('calibre', 10, 'bold'))
    name_entry = tk.Entry(top, textvariable=email_var,
                          font=('calibre', 10, 'normal'))
    name_label.grid(row=2, column=0)
    name_entry.grid(row=2, column=1)
    Bdodajos = tk.Button(top, text="Dodaj Osobe", command=AddOs)
    Bdodajos.grid(row=3, column=0, columnspan=2)


def AddKs()->None:
    '''Dodaje ksiązke do bazy danych'''
    global tytul
    global autor
    global rok
    if __name__ == "__main__":
        tytul = tytul_var.get()
        autor = autor_var.get()
        rok = rok_var.get()
    k = Ksiazka(tytul=tytul, autor=autor, rok=rok)
    sesja.add(k)
    sesja.commit()
    if __name__ == "__main__":
        Wypisz()


def AddOs()->None:
    '''Dodaje osobe do bazy danych'''
    global imie
    global nazwisko
    global email
    if __name__ == "__main__":
        imie = imie_var.get()
        nazwisko = nazwisko_var.get()
        email = email_var.get()
    k = Osoba(imie=imie, nazwisko=nazwisko, email=email)
    sesja.add(k)
    sesja.commit()
    if __name__ == "__main__":
        Wypisz()


def DelKs()->None:
    '''Usuwa ksiązke z bazy danych'''
    global tytul
    global autor
    global rok
    tytul = selected_tytul
    autor = selected_autor
    rok = selected_rok
    sesja.query(Ksiazka).filter(Ksiazka.tytul == tytul,
                                Ksiazka.autor == autor, Ksiazka.rok == rok).delete()
    sesja.commit()
    if __name__ == "__main__":
        Wypisz()


def DelOs()->None:
    '''Usuwa osobe z bazy danych'''
    global imie
    global nazwisko
    global email
    imie = selected_imie
    nazwisko = selected_nazwisko
    email = selected_email
    sesja.query(Osoba).filter(Osoba.imie == imie, Osoba.nazwisko ==
                              nazwisko, Osoba.email == email).delete()
    sesja.commit()
    if __name__ == "__main__":
        Wypisz()


def AddWyp()->None:
    '''Dodaje relacje wyporzyczenia miedzy ksiązka a osoba'''
    imie = selected_imie
    nazwisko = selected_nazwisko
    email = selected_email
    tytul = selected_tytul
    autor = selected_autor
    rok = selected_rok
    listao = sesja.query(Osoba).filter(
        Osoba.imie == imie, Osoba.nazwisko == nazwisko, Osoba.email == email).all()
    listak = sesja.query(Ksiazka).filter(
        Ksiazka.tytul == tytul, Ksiazka.autor == autor, Ksiazka.rok == rok).all()
    listak[0].wyporzycza = listao[0].id
    sesja.commit()
    if __name__ == "__main__":
        Wypisz()


def AddZw()->None:
    '''Usówa relacje wyporzyczenia miedzy ksiązka a osoba'''
    imie = selected_imie
    nazwisko = selected_nazwisko
    email = selected_email
    tytul = selected_tytul
    autor = selected_autor
    rok = selected_rok
    listao = sesja.query(Osoba).filter(
        Osoba.imie == imie, Osoba.nazwisko == nazwisko, Osoba.email == email).all()
    listak = sesja.query(Ksiazka).filter(
        Ksiazka.tytul == tytul, Ksiazka.autor == autor, Ksiazka.rok == int(rok)).all()
    if listak[0].wyporzycza == listao[0].id:
        listak[0].wyporzycza = None
    sesja.commit()
    if __name__ == "__main__":
        Wypisz()


def Wypisz()->None:
    '''Wypisuje nowy zmieniony stan baz danych do widoków drzew'''
    Tree.delete(*Tree.get_children())
    l = sesja.query(Ksiazka)
    i = 1
    for l1 in l:
        if l1.wyporzycza is None:
            wyp = ""
        else:
            listao = sesja.query(Osoba).filter(Osoba.id == l1.wyporzycza).all()
            wyp = listao[0].imie
        Tree.insert('', tk.END, values=[l1.tytul, wyp])
        i = i + 1
    newtree.delete(*newtree.get_children())
    l = sesja.query(Osoba)
    i = 1
    for l1 in l:
        newtree.insert('', tk.END, values=[l1.imie, l1.nazwisko, l1.email])
        i = i + 1


def item_selected(event)->None:
    ''' Funkcja wypisujaca do listboxa inforamcje o zaznaczonej ksiązce'''
    global selected_tytul
    global selected_autor
    global selected_rok
    listbox.delete(0, 5)
    for selected_item in Tree.selection():
        item = Tree.item(selected_item)
        record = item['values']
        listak = sesja.query(Ksiazka).filter(Ksiazka.tytul == record[0]).all()
        if(len(listak) == 0):
            listbox.insert(0, "Tytuł:")
            listbox.insert(1, "Autor:")
            listbox.insert(2, "Rok:")
            listbox.insert(3, "Wyporzycza:")
        else:
            selected_tytul = listak[0].tytul
            selected_autor = listak[0].autor
            selected_rok = listak[0].rok
            listbox.insert(0, "Tytuł:"+listak[0].tytul)
            listbox.insert(1, "Autor:"+listak[0].autor)
            listbox.insert(2, "Rok:"+str(listak[0].rok))
            if(listak[0].wyporzycza is not None):
                listao = sesja.query(Osoba).filter(
                    Osoba.id == listak[0].wyporzycza).all()
                listbox.insert(3, "Wyporzycza:"+listao[0].imie)

def item_selectedOsoba(event)->None:
    '''Funkcja wypisujaca do listboxa liste książek wyporzyczonych przez zaznaczona osobe'''
    global selected_imie
    global selected_nazwisko
    global selected_email
    listbooks.delete(0, 100)
    for selected_item in newtree.selection():
        item = newtree.item(selected_item)
        record = item['values']
        selected_imie = record[0]
        selected_nazwisko = record[1]
        selected_email = record[2]
        listao = sesja.query(Osoba).filter(
            Osoba.imie == record[0], Osoba.nazwisko == record[1], Osoba.email == record[2]).all()
        listak = sesja.query(Ksiazka).filter(
            Ksiazka.wyporzycza == listao[0].id).all()
        i = 0
        for k in listak:
            listbooks.insert(i, "Tytuł: "+k.tytul+" Autor: "+k.autor)

if __name__ == "__main__":
    '''Stwórz okno i zmienne globalne dla pól tekstowych i ustaw cały interfejs'''
    root = Tk()
    root.title('Aplikacja dla biblioteki')
    root.geometry("1600x400")
    selected_imie = ''
    selected_nazwisko = ''
    selected_email = ''
    selected_tytul = ''
    selected_autor = ''
    selected_rok = '0'
    imie_var = StringVar()
    nazwisko_var = StringVar()
    email_var = StringVar()
    tytul_var = StringVar()
    autor_var = StringVar()
    rok_var = IntVar()
    engine = create_engine('sqlite:///wyklad.db', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sesja = Session()
    name_label = tk.Label(root, text='Lista Książek', font=('calibre', 10, 'bold'))
    name_label.grid(row=0, column=2)
    Bdodajos = tk.Button(root, text="Dodaj Osobe", command=AddOsPopUp)
    Bdodajos.grid(row=1, column=0)
    Bdodajos = tk.Button(root, text="Dodaj Książkę", command=AddKsPopUp)
    Bdodajos.grid(row=1, column=1)
    Bdodajos = tk.Button(root, text="Usuń Osobe", command=DelOs)
    Bdodajos.grid(row=2, column=0)
    Bdodajos = tk.Button(root, text="Usuń Książkę", command=DelKs)
    Bdodajos.grid(row=2, column=1)
    Bdodajos = tk.Button(root, text="Wyporzycz Książkę", command=AddWyp)
    Bdodajos.grid(row=3, column=0)
    Bdodajos = tk.Button(root, text="Zwróć Książkę", command=AddZw)
    Bdodajos.grid(row=3, column=1)
    columns = ('tytul', 'wyporzycza')
    Tree = ttk.Treeview(root, columns=columns, show='headings')
    Tree.heading('tytul', text='Tytuł')
    Tree.heading('wyporzycza', text='Wyporzycza')
    Tree.bind('<<TreeviewSelect>>', item_selected)
    Tree.grid(row=1, column=2, rowspan=5, padx=5, pady=5)
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=Tree.yview)
    Tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=3, rowspan=5, sticky='ns')
    listbox = tk.Listbox(root, height=4)
    listbox.grid(row=1, column=4, rowspan=2)
    name_label = tk.Label(root, text='Info o Książce',
                        font=('calibre', 10, 'bold'))
    name_label.grid(row=0, column=4)
    label = tk.Label(root, text="Lista Wyporzyczajacych",
                    font=('calibre', 10, 'bold'))
    label.grid(row=0, column=5)
    columns = ('Imie', 'Nazwisko', 'Email')
    newtree = ttk.Treeview(root, columns=columns, show='headings')
    newtree.grid(row=1, column=5, rowspan=5)
    newtree.heading('Imie', text='Imie')
    newtree.heading('Nazwisko', text='Nazwisko')
    newtree.heading('Email', text='Email')
    newtree.bind('<<TreeviewSelect>>', item_selectedOsoba)
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=listbox.yview)
    newtree.configure(yscroll=scrollbar.set)
    label = tk.Label(root, text="Lista wyporzyczonych ksiązek",
                    font=('calibre', 10, 'bold'))
    label.grid(row=0, column=7)
    scrollbar.grid(row=1, column=6, rowspan=5, sticky='ns')
    listbooks = tk.Listbox(root, height=20, width=30)
    listbooks.grid(row=1, column=7, rowspan=6)
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=listbooks.yview)
    listbooks.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=8, rowspan=3, sticky='ns')
    Wypisz()
    print(type(Base))
    root.mainloop()
