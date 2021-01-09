import Registrovani_korisnik
import re


def opcije(korisnicko_ime):
    print("1. Dodavanje novih hotela")
    print("2. Dodavanje novih recepcionera")
    print("3. Azuriranje hotela ")
    print("4. Brisanje hotela")
    print("5. Brisanje recepcionera")
    print("6. Pretraga recepcionera")
    print("7. Odjava")
    print("8. Izlazak iz aplikacije")
    opcija = int(input("Izaberite opciju: "))
    while opcija not in range(1, 9):
        print("Molim vas izaberite opciju od 1 do 9!")
        opcija = int(input("Izaberite opciju: "))

    if opcija == 1:
        dodavanje_novih_soba(korisnicko_ime)
    elif opcija == 2:
        dodavanje_novih_recepcionera(korisnicko_ime)
    elif opcija == 3:
        azuriranje(korisnicko_ime)
    elif opcija == 4:
        brisanje_hotela(korisnicko_ime)
    elif opcija == 5:
        brisanje_recepcionera(korisnicko_ime)
    elif opcija == 6:
        pretraga_recepcionera(korisnicko_ime)
    elif opcija == 7:
        odjava()
    elif opcija == 8:
        izlazak()


def dodavanje_novih_hotela(korisnicko_ime):
    print("\nUnesite karakteristike novog hotela: ")

    hoteli = open("hoteli.txt", "r")
    id_list = []
    naziv_list = []
    adresa_list = []

    for hotel in hoteli.readlines():
        odlika = hotel.rstrip("\n").split("|")
        id_hotela = odlika[0]
        naziv_hotela = odlika[1]
        adresa_hotela = odlika[2]
        id_list.append(id_hotela)
        naziv_list.append(naziv_hotela)
        adresa_list.append(adresa_hotela)
    hoteli.close()

    nov_id_hotela = input('Unesite ID novog hotela: ')
    while len(nov_id_hotela) != 6 or nov_id_hotela in id_list or nov_id_hotela.isnumeric() == False:
        if len(nov_id_hotela) != 6:
            print("ID mora imati 6 cifara!")
            nov_id_hotela = input('Unesite ID novog hotela: ')
        elif nov_id_hotela in id_list:
            print('Vec postoji hotel sa takvim ID')
            nov_id_hotela = input('Unesite ID novog hotela: ')
        else:
            print('Pokusajte ponovo!')
            nov_id_hotela = input('Unesite ID novog hotela: ')

    nov_naziv_hotela = input('Unesite naziv novog hotela: ')
    while nov_naziv_hotela in naziv_list:
        print('Vec postoji hotel sa takvim nazivom')
        nov_naziv_hotela = input('Unesite naziv novog hotela: ')

    nova_adresa_hotela = input('Unesite adresu novog hotela: ')
    while nova_adresa_hotela in adresa_list:
        print('Vec postoji hotel na toj adresi')
        nova_adresa_hotela = input('Unesite adresu novog hotela: ')

    nove_sobe = []
    nova_soba = input('Unesite broj sobe: ')
    while nova_soba.isnumeric() == False:
        print('Soba mora biti numerisana!')
        nova_soba = input('Unesite broj sobe: ')
    nove_sobe.append(nova_soba)
    pitanje = input('Da li zelite da uneste jos soba? (da/ne)')

    while pitanje != "da" and pitanje != "ne":
        print('Molim vas unesite da ili ne!')
        pitanje = input('Da li zelite da uneste jos soba? (da/ne)')

    while pitanje == "da":
        nova_soba2 = input('Unesite broj sobe: ')
        while nova_soba2.isnumeric() == False:
            print('Soba mora biti numerisana!')
            nova_soba2 = input('Unesite broj sobe: ')
        while nova_soba2 in nove_sobe:
            print('Vec ste dodali tu sobu!')
            nova_soba2 = input('Unesite broj sobe: ')
            while nova_soba2.isnumeric() == False:
                print('Soba mora biti numerisana!')
                nova_soba2 = input('Unesite broj sobe: ')
        nove_sobe.append(nova_soba2)
        pitanje = input('Da li zelite da uneste jos soba? (da/ne)')

        while pitanje != "da" and pitanje != "ne":
            print('Molim vas unesite da ili ne!')
            pitanje = input('Da li zelite da uneste jos soba? (da/ne)')

    nov_bazen = input('Unesite da li nov hotel ima bazen (da/ne): ')
    while nov_bazen != "da" and nov_bazen != "ne":
        print('Molim vas unesite da ili ne!')
        nov_bazen = input('Unesite da li nov hotel ima bazen (da/ne): ')
    if nov_bazen == "da":
        nov_bazen = 'da'
    else:
        nov_bazen = 'ne'

    nov_restoran = input('Unesite da li nov hotel ima restoran (da/ne): ')
    while nov_restoran != "da" and nov_restoran != "ne":
        print('Molim vas unesite da ili ne!')
        nov_restoran = input('Unesite da li nov hotel ima restoran (da/ne): ')
    if nov_restoran == "da":
        nov_restoran = 'da'
    else:
        nov_restoran = 'ne'
    ocena = '/'

    hoteli2 = open('hoteli.txt', 'a')
    hoteli2.write('\n' + nov_id_hotela + '|' + nov_naziv_hotela + '|' + nova_adresa_hotela +
                  '|' + str(nove_sobe) + '|' + nov_bazen + '|' + nov_restoran + '|' + ocena)
    hoteli2.close()

    print('Hotel uspesno dodat! Molim vas dodajte sada sobe.')

    return nove_sobe, nov_id_hotela


def dodavanje_novih_soba(korisnicko_ime):
    return_values = dodavanje_novih_hotela(korisnicko_ime)
    nove_sobe = return_values[0]
    nov_id_hotela = return_values[1]

    count = 1
    count2 = 0
    for _ in nove_sobe:  # _ zato sto mi ne treba element
        sobe_ucitano = open('sobe.txt', 'r')
        id_sobe_list = []
        # automatski se dodeljuje kasnije id hotela koji je upravo napravljen
        # automatski se dodeljuje kasnije broj sobe
        for soba in sobe_ucitano.readlines():
            odlika = soba.rstrip("\n").split("|")
            id_sobe = odlika[0]
            id_sobe_list.append(id_sobe)
        sobe_ucitano.close()

        print('Soba broj {} koju ste dodali je soba {}. Molim vas sada dodajte njenu specifikaciju.'.format(
            count, str(nove_sobe[count2])))

        nov_id_sobe = input('Unesite ID nove sobe: ')
        while len(nov_id_sobe) != 6 or nov_id_sobe in id_sobe_list or nov_id_sobe.isnumeric() == False:
            if len(nov_id_sobe) != 6:
                print("ID mora imati 6 cifara!")
                nov_id_sobe = input('Unesite ID nove sobe: ')
            elif nov_id_sobe in id_sobe_list:
                print('Vec postoji soba sa takvim ID')
                nov_id_sobe = input('Unesite ID nove sobe: ')
            else:
                print('Pokusajte ponovo!')
                nov_id_sobe = input('Unesite ID nove sobe: ')

        nov_broj_kreveta = input('Unesite broj kreveta (max 6): ')
        while nov_broj_kreveta.isnumeric() == False:
            print('Molim vas unesite broj kreveta ')
            nov_broj_kreveta = input('Unesite broj kreveta (max 6): ')
        while int(nov_broj_kreveta) not in range(1, 7):
            print('Molim vas unesite broj kreveta, minimalno jedan a maksimalno sest.')
            nov_broj_kreveta = input('Unesite broj kreveta (max 6): ')
            while nov_broj_kreveta.isnumeric() == False:
                print('Molim vas unesite broj kreveta ')
                nov_broj_kreveta = input('Unesite broj kreveta (max 6): ')
        nov_tip = input('Unesite tip sobe (jedna/apartman): ')
        while nov_tip != "jedna" and nov_tip != "apartman":
            print('Molim vas unesite da li je u pitanju jedna soba ili apartman!')
            nov_tip = input('Unesite tip sobe (jedna/apartman): ')
        if nov_tip == "jedna":
            nov_tip = 'jedna'
        else:
            nov_tip = 'apartman'

        nova_klima = input('Unesite da li nova soba ima klimu (da/ne): ')
        while nova_klima != "da" and nova_klima != "ne":
            print('Molim vas unesite da ili ne!')
            nova_klima = input('Unesite da li nova soba ima klimu (da/ne): ')
        if nova_klima == "da":
            nova_klima = 'da'
        else:
            nova_klima = 'ne'

        nov_tv = input('Unesite da li nova soba ima TV (da/ne): ')
        while nov_tv != "da" and nov_tv != "ne":
            print('Molim vas unesite da ili ne!')
            nov_tv = input('Unesite da li nova soba ima TV (da/ne): ')
        if nov_tv == "da":
            nov_tv = 'da'
        else:
            nov_tv = 'ne'

        nova_cena = input('Unesite novu cenu sobe: ')
        while nova_cena.isnumeric() == False:
            print('Greska - cena mora biti broj!')
            nova_cena = input('Unesite novu cenu sobe: ')
        nova_cena_din = nova_cena + 'din'

        sobe_ucitano2 = open('sobe.txt', 'a')
        sobe_ucitano2.write('\n' + nov_id_sobe + '|' + nov_id_hotela + '|' + str(
            nove_sobe[count2]) + '|' + nov_broj_kreveta + '|' + nov_tip + '|' + nova_klima + '|' + nov_tv + '|' + nova_cena_din + '|' + '/')
        sobe_ucitano2.close()

        print('Soba {} uspesno dodata!\n'.format(str(nove_sobe[count2])))

        count += 1
        count2 += 1
    opcije(korisnicko_ime)


def dodavanje_novih_recepcionera(korisnicko_ime):
    korisnicko_ime = input("Unesite korisnicko ime recepcionera: ")
    while len(korisnicko_ime) < 6:
        print("Korisnicko ime mora imati barem 6 karaktera!")
        korisnicko_ime = input("Unesite korisnicko ime recepcionera: ")
    lozinka = input("Unesite lozinku: ")
    while any(char.isdigit() for char in lozinka) == False or any(char.isalpha() for char in lozinka) == False:
        print(
            "Lozinka mora da sadrzi barem jedan broj, jedno slovo i ukupno osam karaktera!")
        lozinka = input("Unesite lozinku: ")
    ime = input("Unesite ime recepcionera: ")
    prezime = input("Unesite prezime recepcionera: ")
    telefon = input("Unesite kontakt telefon: ")
    email = input("Unesite email adresu: ")
    while not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Unesite ispravnu e-mail adresu")
        email = input("Email adresa: ")
    status = "recepcioner"

    id_hotela = input("Unesite ID hotela u kom ce recepcioner raditi: ")
    hoteli = open("hoteli.txt", "r")
    id_hotela_ucitano_list = []
    for hotel in hoteli.readlines():
        id_hotela_ucitano = hotel.rstrip("\n").split("|")[0]
        id_hotela_ucitano_list.append(id_hotela_ucitano)
    hoteli.close()
    while id_hotela not in id_hotela_ucitano_list:
        print("Ne postoji hotel sa takvim ID!")
        id_hotela = input("Unesite ID hotela u kom ce recepcioner raditi: ")

    korisnici = open("korisnici.txt", "a")
    korisnici.write("\n" + korisnicko_ime + "|" + lozinka + "|" +
                    ime + "|" + prezime + "|" + telefon + "|" + email + "|" + status + "|" + id_hotela)
    korisnici.close()

    print("Recepcioner uspesno dodat!")
    opcije(korisnicko_ime)


def azuriranje(korisnicko_ime):
    print("--------------------------------------")
    print("| ID hotela |   Naziv   |   Adresa   |")
    print("--------------------------------------")
    hoteli = open("hoteli.txt", "r")
    lista_id = []
    for i in hoteli.readlines():
        odlika = i.rstrip("\n").split("|")
        lista_id.append(odlika[0])
        print("|" + odlika[0].ljust(11) + "|" +
              odlika[1].ljust(11) + "|" + odlika[2].ljust(12) + "|")
    print("--------------------------------------")
    hoteli.close()

    opcija = input("Unesite ID hotela koji zelite da menjate: ")
    while opcija not in lista_id:
        print("Nema hotela s takvim ID!")
        opcija = input("Unesite ID hotela koji zelite da menjate: ")

    print("1) Dodavanje soba")
    print("2) Dodavanje bazena")
    print("3) Dodavanje restorana")
    izbor = int(input("Izaberite opciju:"))
    while izbor not in range(1, 4):
        print("Molim vas izaberite opciju od 1 do 4!")
        izbor = int(input("Izaberite opciju:"))

    hoteli = open("hoteli.txt", "r")
    string = ''
    string2 = ''
    string3 = ''
    string4 = ''
    string5 = ''
    for i in hoteli.readlines():
        odlika = i.rstrip("\n").split("|")
        lista_soba = odlika[3]
        string3 = lista_soba.replace("[", "")
        string4 = string3.replace("]", "")
        string5 = string4.replace("'", "")
        lista_soba_fixed = list(string5.split(", "))
        bazen = odlika[4]
        restoran = odlika[5]

        if odlika[0] == opcija:
            if izbor == 1:
                nove_sobe = []
                # nije uradjena provera da se vidi da li soba koju dodajemo vec postoji u hotelu!
                nova_soba = input('Unesite broj sobe: ')
                nove_sobe.append(nova_soba)
                pitanje = input('Da li zelite da uneste jos soba? (da/ne)')

                while pitanje != "da" and pitanje != "ne":
                    print('Molim vas unesite da ili ne!')
                    pitanje = input('Da li zelite da uneste jos soba? (da/ne)')

                while pitanje == "da":
                    nova_soba2 = input('Unesite broj sobe: ')
                    while nova_soba2 in nove_sobe:
                        print('Vec ste dodali tu sobu!')
                        nova_soba2 = input('Unesite broj sobe: ')
                    nove_sobe.append(nova_soba2)
                    pitanje = input('Da li zelite da uneste jos soba? (da/ne)')

                    while pitanje != "da" and pitanje != "ne":
                        print('Molim vas unesite da ili ne!')
                        pitanje = input(
                            'Da li zelite da uneste jos soba? (da/ne)')
                lista_soba_fixed.extend(nove_sobe)
                odlika[3] = str(lista_soba_fixed)
                string2 = odlika[0] + '|' + odlika[1] + '|' + odlika[2] + '|' + \
                    odlika[3] + '|' + odlika[4] + '|' + \
                    odlika[5] + '|' + odlika[6] + '\n'
                string += string2

                count = 1
                count2 = 0
                for i in nove_sobe:
                    sobe_ucitano = open('sobe.txt', 'r')
                    id_sobe_list = []
                    for soba in sobe_ucitano.readlines():
                        odlika = soba.rstrip("\n").split("|")
                        id_sobe = odlika[0]
                        id_sobe_list.append(id_sobe)
                    sobe_ucitano.close()

                    print('Soba broj {} koju ste dodali je soba {}. Molim vas sada dodajte njenu specifikaciju.'.format(
                        count, str(nove_sobe[count2])))

                    nov_id_sobe = input('Unesite ID nove sobe: ')
                    while len(nov_id_sobe) != 6 or nov_id_sobe in id_sobe_list or nov_id_sobe.isnumeric() == False:
                        if len(nov_id_sobe) != 6:
                            print("ID mora imati 6 cifara!")
                            nov_id_sobe = input('Unesite ID nove sobe: ')
                        elif nov_id_sobe in id_sobe_list:
                            print('Vec postoji soba sa takvim ID')
                            nov_id_sobe = input('Unesite ID nove sobe: ')
                        else:
                            print('Pokusajte ponovo!')
                            nov_id_sobe = input('Unesite ID nove sobe: ')

                    nov_broj_kreveta = input('Unesite broj kreveta (max 6): ')
                    while nov_broj_kreveta.isnumeric() == False:
                        print('Molim vas unesite broj kreveta ')
                        nov_broj_kreveta = input(
                            'Unesite broj kreveta (max 6): ')
                    while int(nov_broj_kreveta) not in range(1, 7):
                        print(
                            'Molim vas unesite broj kreveta, minimalno jedan a maksimalno sest.')
                        nov_broj_kreveta = input(
                            'Unesite broj kreveta (max 6): ')
                        while nov_broj_kreveta.isnumeric() == False:
                            print('Molim vas unesite broj kreveta ')
                            nov_broj_kreveta = input(
                                'Unesite broj kreveta (max 6): ')

                    nov_tip = input('Unesite tip sobe (jedna/apartman): ')
                    while nov_tip != "jedna" and nov_tip != "apartman":
                        print(
                            'Molim vas unesite da li je u pitanju jedna soba ili apartman!')
                        nov_tip = input('Unesite tip sobe (jedna/apartman): ')
                    if nov_tip == "jedna":
                        nov_tip = 'jedna'
                    else:
                        nov_tip = 'apartman'

                    nova_klima = input(
                        'Unesite da li nova soba ima klimu (da/ne): ')
                    while nova_klima != "da" and nova_klima != "ne":
                        print('Molim vas unesite da ili ne!')
                        nova_klima = input(
                            'Unesite da li nova soba ima klimu (da/ne): ')
                    if nova_klima == "da":
                        nova_klima = 'da'
                    else:
                        nova_klima = 'ne'

                    nov_tv = input('Unesite da li nova soba ima TV (da/ne): ')
                    while nov_tv != "da" and nov_tv != "ne":
                        print('Molim vas unesite da ili ne!')
                        nov_tv = input(
                            'Unesite da li nova soba ima TV (da/ne): ')
                    if nov_tv == "da":
                        nov_tv = 'da'
                    else:
                        nov_tv = 'ne'

                    nova_cena = input('Unesite novu cenu sobe: ')
                    while nova_cena.isnumeric() == False:
                        print('Greska - cena mora biti broj!')
                        nova_cena = input('Unesite novu cenu sobe: ')
                    nova_cena_din = nova_cena + 'din'

                    sobe_ucitano2 = open('sobe.txt', 'a')
                    sobe_ucitano2.write('\n' + nov_id_sobe + '|' + opcija + '|' + str(
                        nove_sobe[count2]) + '|' + nov_broj_kreveta + '|' + nov_tip + '|' + nova_klima + '|' + nov_tv + '|' + nova_cena_din + '|' + '/')
                    sobe_ucitano2.close()

                    print('Soba {} uspesno dodata!'.format(
                        str(nove_sobe[count2])))

                    count += 1
                    count2 += 1
                print("Sobe uspesno dodate!\n")

            elif izbor == 2 and bazen == "da":
                print("Hotel vec poseduje bazen!")
                azuriranje(korisnicko_ime)

            elif izbor == 2 and bazen == "ne":
                odlika[4] = 'da'
                string2 = odlika[0] + '|' + odlika[1] + '|' + odlika[2] + '|' + \
                    odlika[3] + '|' + odlika[4] + '|' + \
                    odlika[5] + '|' + odlika[6] + '\n'
                string += string2
                print("Bazen uspesno dodat!\n")

            elif izbor == 3 and restoran == "da":
                print("Hotel vec poseduje restoran!")
                azuriranje(korisnicko_ime)

            elif izbor == 3 and restoran == "ne":
                odlika[5] = 'da'
                string2 = odlika[0] + '|' + odlika[1] + '|' + odlika[2] + '|' + \
                    odlika[3] + '|' + odlika[4] + '|' + \
                    odlika[5] + '|' + odlika[6] + '\n'
                string += string2
                print("Restoran uspesno dodat!\n")
        else:
            string += i
    hoteli.close()
    hoteli_upis = open("hoteli.txt", "w")
    hoteli_upis.write(string)
    hoteli_upis.close()
    opcije(korisnicko_ime)


def brisanje_hotela(korisnicko_ime):
    print("--------------------------------------")
    print("| ID hotela |   Naziv   |   Adresa   |")
    print("--------------------------------------")
    hoteli = open("hoteli.txt", "r")
    lista_id = []
    for i in hoteli.readlines():
        odlika = i.rstrip("\n").split("|")
        lista_id.append(odlika[0])
        print("|" + odlika[0].ljust(11) + "|" +
              odlika[1].ljust(11) + "|" + odlika[2].ljust(12) + "|")
    print("--------------------------------------")
    hoteli.close()

    hotel_id = input("Unesite ID hotela kojeg zelite da obrisete: ")
    while hotel_id not in lista_id:
        print("Ne postoji hotel sa takvim ID!")
        hotel_id = input("Unesite ID hotela kojeg zelite da obrisete: ")
    hoteli_ucitano = open("hoteli.txt", "r")
    hotel = hoteli_ucitano.readlines()
    hoteli_ucitano.close()

    hotel_upis = open("hoteli.txt", "w")
    for i in hotel:
        odlika = i.split("|")
        if hotel_id != odlika[0]:
            hotel_upis.write(i)

    hotel_upis.close()
    print("Hotel uspesno obrisan!")
    opcije(korisnicko_ime)


def brisanje_recepcionera(korisnicko_ime):
    korisnici = open("korisnici.txt", "r")
    print("----------------------------------------------------------------------------------------")
    print("|                                LISTA RECEPCIONERA                                    |")
    print("----------------------------------------------------------------------------------------")
    print("|  korisnicko ime  |     Ime      |    Prezime    |    telefon    |   e-mail adresa    |")
    print("----------------------------------------------------------------------------------------")
    for i in korisnici.readlines():
        odlika = i.rstrip("\n").split("|")
        if odlika[6] == "recepcioner":
            print("|" + odlika[0].ljust(18) + "|" + odlika[2].ljust(14) + "|" + odlika[3].ljust(
                15) + "|" + odlika[4].ljust(15) + "|" + odlika[5].ljust(20) + "|")
    print("----------------------------------------------------------------------------------------")
    korisnici.close()

    username = input(
        "Unesite korisnicko ime recepcionera kojeg zelite da obrisete:")
    korisnici = open("korisnici.txt", "r")
    korisnici_ucitano = korisnici.readlines()
    korisnici.close()

    korisnici = open("korisnici.txt", "w")

    for korisnik in korisnici_ucitano:
        odlika = korisnik.rstrip("\n").split("|")

        if odlika[6] != "recepcioner":
            korisnici.write(korisnik)

        elif odlika[6] == "recepcioner":
            if username != odlika[0]:
                korisnici.write(korisnik)

    print("Recepcioner uspesno obrisan!")
    korisnici.close()
    opcije(korisnicko_ime)


def pretraga_recepcionera(korisnicko_ime):
    print("1)Pretraga na osnovu jednog kriterijuma")
    print("2)Pretraga po vise kriterijuma")
    opcija = int(input("Kako zelite da pretrazujete? 1/2: "))
    while opcija not in range(1, 3):
        print("opcije su 1 i 2! ")
        opcija = int(input("Kako zelite da pretrazujete? 1/2: "))
    if opcija == 1:
        jedan_kriterijum(korisnicko_ime)
    elif opcija == 2:
        vise_kriterijuma(korisnicko_ime)


def jedan_kriterijum(korisnicko_ime):
    print("Pretraga na osnovu jednog kriterijuma:")
    print("1) Ime recepcionera")
    print("2) Prezime recepcionera")
    print("3) Korisnicko ime recepcionera")
    print("4) Email recepcioneras")
    print("5) Uloga")
    print("6) Hotel(ID)")

    opcija = int(
        input("Unesite na osnovu kog kriterijuma zelite pretrazivati: "))
    while opcija not in range(1, 7):
        print("Morate uneti broj od 1 do 6!")
        opcija = int(input(
            "Unesite na osnovu kog kriterijuma zelite pretrazivati: "))
    unos = input("Unesite zeljenu karakteristiku: ")
    korisnik = {}

    if opcija == 1:
        korisnik['ime_recepcionera'] = unos
    elif opcija == 2:
        korisnik['prezime_recepcionera'] = unos
    elif opcija == 3:
        korisnik['korisnicko_ime_recepcionera'] = unos
    elif opcija == 4:
        korisnik['email_recepcionera'] = unos
    elif opcija == 5:
        korisnik['uloga'] = unos
    elif opcija == 6:
        korisnik['hotel'] = unos

    korisnici = open("korisnici.txt", "r")
    korisnici_ucitano = {}
    pogodjeni_korisnici = []
    for jedan_korisnik in korisnici.readlines():
        odlika = jedan_korisnik.rstrip("\n").split("|")
        korisnici_ucitano = {'korisnicko_ime_recepcionera': odlika[0], 'ime_recepcionera': odlika[2],
                             'prezime_recepcionera': odlika[3], 'telefon': odlika[4], 'email': odlika[5], 'uloga': odlika[6], 'hotel': odlika[7]}
        if korisnik.items() <= korisnici_ucitano.items() and odlika[6] == 'recepcioner':
            pogodjeni_korisnici.append(korisnici_ucitano)

    if len(pogodjeni_korisnici) != 0:
        print("------------------------------------------------------------------------------------------------------")
        print("|   Korisnicko ime   |    Ime    |   Prezime   |  Telefon  |      Email      |   Uloga   |   Hotel   |")
        print("------------------------------------------------------------------------------------------------------")
        for korisnik in pogodjeni_korisnici:
            print("|" + korisnik['korisnicko_ime_recepcionera'].ljust(20) + "|" + korisnik['ime_recepcionera'].ljust(11) + "|" + korisnik['prezime_recepcionera'].ljust(13) + "|" + korisnik['telefon'].ljust(
                11) + "|" + korisnik['email'].ljust(17) + "|" + korisnik['uloga'].ljust(11) + "|" + korisnik['hotel'].ljust(11) + "|")
        print("------------------------------------------------------------------------------------------------------")
        opcije(korisnicko_ime)
    else:
        print("Nema takvih recepcionera.")
    korisnici.close()
    opcije(korisnicko_ime)


def vise_kriterijuma(korisnicko_ime):
    print("Pretraga na osnovu vise kriterijuma:")
    print("1) Ime recepcionera")
    print("2) Prezime recepcionera")
    print("3) Korisnicko ime recepcionera")
    print("4) Email recepcioneras")
    print("5) Uloga")
    print("6) Hotel")

    opcija = int(
        input("Unesite na osnovu kog kriterijuma zelite pretrazivati: "))
    while opcija not in range(1, 7):
        print("Morate uneti broj od 1 do 6!")
        opcija = int(input(
            "Unesite na osnovu kog kriterijuma zelite pretrazivati: "))
    unos = input("Unesite zeljenu karakteristiku: ")
    korisnik = {}

    if opcija == 1:
        korisnik['ime_recepcionera'] = unos
    elif opcija == 2:
        korisnik['prezime_recepcionera'] = unos
    elif opcija == 3:
        korisnik['korisnicko_ime_repecionera'] = unos
    elif opcija == 4:
        korisnik['email_recepcionera'] = unos
    elif opcija == 5:
        korisnik['uloga'] = unos
    elif opcija == 6:
        korisnik['hotel'] = unos

    pitanje = input("Zelite li da unesete jos jedan kriterijum? (da/ne)")

    while pitanje != "da" and pitanje != "ne":
        print('Molim vas unesite da ili ne!')
        pitanje = input("Zelite li da unesete jos jedan kriterijum? (da/ne)")

    while pitanje == "da":
        opcija2 = int(input(
            "Unesite na osnovu kog kriterijuma zelite pretrazivati: "))
        while opcija2 not in range(1, 7):
            print("Morate uneti broj od 1 do 6!")
            opcija2 = int(input(
                "Unesite na osnovu kog kriterijuma zelite pretrazivati: "))
        unos2 = input("Unesite zeljenu karakteristiku: ")
        if opcija2 == 1:
            korisnik['ime_recepcionera'] = unos2
        elif opcija2 == 2:
            korisnik['prezime_recepcionera'] = unos2
        elif opcija2 == 3:
            korisnik['korisnicko_ime_recepcionera'] = unos2
        elif opcija2 == 4:
            korisnik['email_recepcionera'] = unos2
        elif opcija2 == 5:
            korisnik['uloga'] = unos2
        elif opcija2 == 6:
            korisnik['hotel'] = unos2

        pitanje = input("Zelite li da unesete jos jedan kriterijum? (da/ne)")
        while pitanje != "da" and pitanje != "ne":
            print('Molim vas unesite da ili ne!')
            pitanje = input(
                "Zelite li da unesete jos jedan kriterijum? (da/ne)")

    korisnici = open("korisnici.txt", "r")
    pogodjeni_korisnici = []
    for jedan_korisnik in korisnici.readlines():
        odlika = jedan_korisnik.rstrip("\n").split("|")
        korisnici_ucitano = {'korisnicko_ime_recepcionera': odlika[0], 'ime_recepcionera': odlika[2],
                             'prezime_recepcionera': odlika[3], 'telefon': odlika[4], 'email': odlika[5], 'uloga': odlika[6], 'hotel': odlika[7]}
        if korisnik.items() <= korisnici_ucitano.items() and odlika[6] == 'recepcioner':
            pogodjeni_korisnici.append(korisnici_ucitano)

    if len(pogodjeni_korisnici) != 0:
        print("------------------------------------------------------------------------------------------------------")
        print("|   Korisnicko ime   |    Ime    |   Prezime   |  Telefon  |      Email      |   Uloga   |   Hotel   |")
        print("------------------------------------------------------------------------------------------------------")
        for korisnik in pogodjeni_korisnici:
            print("|" + korisnik['korisnicko_ime_recepcionera'].ljust(20) + "|" + korisnik['ime_recepcionera'].ljust(11) + "|" + korisnik['prezime_recepcionera'].ljust(13) + "|" + korisnik['telefon'].ljust(
                11) + "|" + korisnik['email'].ljust(17) + "|" + korisnik['uloga'].ljust(11) + "|" + korisnik['hotel'].ljust(11) + "|")
        print("------------------------------------------------------------------------------------------------------")
        opcije(korisnicko_ime)
    else:
        print("Nema takvih recepcionera.")
    korisnici.close()
    opcije(korisnicko_ime)


def odjava():
    print("---------------------")
    print("|    Dovidjenja!    |")
    print("---------------------")
    print("Molimo vas unesite vase podatke kako bi ste se prijavili")
    Registrovani_korisnik.prijava()


def izlazak():
    print("---------------------")
    print("|    Dovidjenja!    |")
    print("---------------------")
