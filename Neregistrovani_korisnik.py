import re
import Registrovani_korisnik


def opcije():
    print("1) Zapocnite registraciju")
    print("2) Izlaz iz aplikacije")
    opcija = int(input("Izaberite opciju: "))
    while opcija not in range(1, 3):
        print("Molim vas izaberite opciju 1 ili 2")
        opcija = int(input("Izaberite opciju: "))
    if opcija == 1:
        registracija()
    elif opcija == 2:
        print("---------------------")
        print("|    Dovidjenja!    |")
        print("---------------------")


def registracija():
    print("Popunite sledece informacije: \n")
    korisnik = {}

    korisnicko_ime = input("Unesite korisnicko ime: ")
    while len(korisnicko_ime) < 6:
        print("Korisnicko ime mora da sadrzi barem 6 karaktera!")
        korisnicko_ime = input("Unesite korisnicko ime: ")
    lozinka = input("Unesite lozinku: ")
    while any(char.isdigit() for char in lozinka) == False or any(char.isalpha() for char in lozinka) == False or len(lozinka) < 8:
        print(
            "Lozinka mora da sadrzi barem jedan broj, jedno slovo i ukupno osam karaktera!")
        lozinka = input("Unesite lozinku: ")
    ime = input("Ime: ")
    prezime = input("Prezime: ")
    kontakt_telefon = input("Kontakt telefon: ")
    email = input("Email adresa: ")
    while not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Unesite ispravnu e-mail adresu")
        email = input("Email adresa: ")

    status = "registrovani"
    korisnik = {'korisnicko_ime': korisnicko_ime, 'lozinka': lozinka, 'ime': ime,
                'prezime': prezime, 'kontakt_telefon': kontakt_telefon, 'email': email, 'status': status}
    korisnici_fajl = open("korisnici.txt", "a")
    korisnik_str = "|".join([korisnik['korisnicko_ime'], korisnik['lozinka'], korisnik['ime'],
                             korisnik['prezime'], korisnik['kontakt_telefon'], korisnik['email'], korisnik['status']])
    korisnici_fajl.write(("\n") + korisnik_str)
    korisnici_fajl.close()
    print("------------------------------------")
    print("|   Uspesno ste se registrovali!   |")
    print("------------------------------------")

    Registrovani_korisnik.opcije_registrovani(korisnicko_ime)
