import Registrovani_korisnik
from datetime import date, datetime, timedelta


def opcije(korisnicko_ime):
    print("1) Pretraga soba")
    print("2) Pretraga rezervacija")
    print("3) Izvestavanje")
    print("4) Odjava sa sistema")

    opcija = int(input("Izaberite opciju: "))
    while opcija not in range(1, 5):
        print("Unesite broj od 1 do 4!")
        opcija = int(input("Izaberite opciju: "))
    if opcija == 1:
        pretraga_soba(korisnicko_ime)
    elif opcija == 2:
        pretraga_rezervacija(korisnicko_ime)
    # elif opcija == 3:
    #     izvestaj(korisnicko_ime)
    elif opcija == 4:
        odjava()


def pretraga_soba(korisnicko_ime):
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
    print("1) Broj sobe")
    print("2) Broj kreveta")
    print("3) Tip")
    print("4) Klima (da/ne)")
    print("5) TV (da/ne)")
    print("6) Cena")
    print("7) Dostupnost sobe (rezervisana/nerezervisana)")

    opcija = int(
        input("Unesite na osnovu kog kriterijuma zelite pretrazivati: "))
    while opcija not in range(1, 8):
        print("Morate uneti broj od 1 do 7!")
        opcija = int(input(
            "Unesite na osnovu kog kriterijuma zelite pretrazivati: "))
    unos = input("Unesite zeljenu karakteristiku: ")
    soba = {}

    if opcija == 1:
        soba['broj_sobe'] = unos
    elif opcija == 2:
        soba['broj_kreveta'] = unos
    elif opcija == 3:
        soba['tip'] = unos
    elif opcija == 4:
        soba['klima'] = unos
    elif opcija == 5:
        soba['tv'] = unos
    elif opcija == 6:
        soba['cena'] = unos
    elif opcija == 7:
        soba['dostupnost'] = unos

    korisnici = open('korisnici.txt', 'r')
    for korisnik in korisnici.readlines():
        odlika = korisnik.rstrip("\n").split("|")
        if odlika[0] == korisnicko_ime:
            id_hotela = odlika[7]
        else:
            continue
    korisnici.close()

    sobe = open("sobe.txt", "r")
    soba_ucitano = {}
    pogodjene_sobe = []
    for jedna_soba in sobe.readlines():
        odlika = jedna_soba.rstrip("\n").split("|")
        soba_ucitano = {'id': odlika[0], 'id_hotela': odlika[1], 'broj_sobe': odlika[2], 'broj_kreveta': odlika[3],
                        'tip': odlika[4], 'klima': odlika[5], 'tv': odlika[6], 'cena': odlika[7], 'dostupnost': odlika[8]}

        if soba.items() <= soba_ucitano.items() and id_hotela in soba_ucitano.values():
            pogodjene_sobe.append(soba_ucitano)

    if len(pogodjene_sobe) != 0:
        print("--------------------------------------------------------------------------------------------")
        print("|   ID   |  broj sobe  | broj kreveta |    tip    |  klima  | tv |   cena   |  dostupnost  |")
        print("--------------------------------------------------------------------------------------------")
        for soba in pogodjene_sobe:
            print("|" + soba['id'].ljust(8) + "|" + soba['broj_sobe'].ljust(13) + "|" + soba['broj_kreveta'].ljust(14) + "|" + soba['tip'].ljust(
                11) + "|" + soba['klima'].ljust(9) + "|" + soba['tv'].ljust(4) + "|" + soba['cena'].ljust(10) + "|" + soba['dostupnost'].ljust(14) + "|")
        print("--------------------------------------------------------------------------------------------")
        opcije(korisnicko_ime)
    else:
        print("Nemamo takvih soba.")
    sobe.close()
    opcije(korisnicko_ime)


def vise_kriterijuma(korisnicko_ime):
    print("Pretraga na osnovu vise kriterijuma: ")
    print("1) Broj sobe")
    print("2) Broj kreveta")
    print("3) Tip")
    print("4) Klima (da/ne)")
    print("5) TV (da/ne)")
    print("6) Cena")
    print("7) Dostupnost sobe (rezervisan/nerezervisan)")

    opcija = int(
        input("Unesite na osnovu kog kriterijuma zelite pretrazivati: "))
    while opcija not in range(1, 8):
        print("Morate uneti broj od 1 do 7!")
        opcija = int(input(
            "Unesite na osnovu kog kriterijuma zelite pretrazivati: "))
    unos = input("Unesite zeljenu karakteristiku: ")
    soba = {}

    if opcija == 1:
        soba['broj_sobe'] = unos
    elif opcija == 2:
        soba['broj_kreveta'] = unos
    elif opcija == 3:
        soba['tip'] = unos
    elif opcija == 4:
        soba['klima'] = unos
    elif opcija == 5:
        soba['tv'] = unos
    elif opcija == 6:
        soba['cena'] = unos
    elif opcija == 7:
        soba['dostupnost'] = unos

    korisnici = open('korisnici.txt', 'r')
    for korisnik in korisnici.readlines():
        odlika = korisnik.rstrip("\n").split("|")
        if odlika[0] == korisnicko_ime:
            id_hotela = odlika[7]
        else:
            continue
    korisnici.close()

    pitanje = input("Zelite li da unesete jos jedan kriterijum? (da/ne)")
    while pitanje != "da" and pitanje != "ne":
        print('Molim vas unesite da ili ne!')
        pitanje = input("Zelite li da unesete jos jedan kriterijum? (da/ne)")

    while pitanje == "da":
        opcija2 = int(input(
            "Unesite na osnovu kog kriterijuma zelite pretrazivati: "))
        while opcija not in range(1, 8):
            print("Morate uneti broj od 1 do 7!")
            opcija2 = int(input(
                "Unesite na osnovu kog kriterijuma zelite pretrazivati: "))
        unos2 = input("Unesite zeljenu karakteristiku: ")
        if opcija2 == 1:
            soba['broj_sobe'] = unos2
        elif opcija2 == 2:
            soba['broj_kreveta'] = unos2
        elif opcija2 == 3:
            soba['tip'] = unos2
        elif opcija2 == 4:
            soba['klima'] = unos2
        elif opcija2 == 5:
            soba['tv'] = unos2
        elif opcija2 == 6:
            soba['cena'] = unos2
        elif opcija2 == 7:
            soba['dostupnost'] = unos2

        pitanje = input("Zelite li da unesete jos jedan kriterijum? (da/ne)")
        while pitanje != "da" and pitanje != "ne":
            print('Molim vas unesite da ili ne!')
            pitanje = input(
                "Zelite li da unesete jos jedan kriterijum? (da/ne)")

    sobe = open("sobe.txt", "r")
    pogodjene_sobe = []
    for jedna_soba in sobe.readlines():
        odlika = jedna_soba.rstrip("\n").split("|")
        soba_ucitano = {'id': odlika[0], 'id_hotela': odlika[1], 'broj_sobe': odlika[2], 'broj_kreveta': odlika[3],
                        'tip': odlika[4], 'klima': odlika[5], 'tv': odlika[6], 'cena': odlika[7], 'dostupnost': odlika[8]}
        if soba.items() <= soba_ucitano.items() and id_hotela in soba_ucitano.values():
            pogodjene_sobe.append(soba_ucitano)
    if len(pogodjene_sobe) != 0:
        print("--------------------------------------------------------------------------------------------")
        print("|   ID   |  broj sobe  | broj kreveta |    tip    |  klima  | tv |   cena   |  dostupnost  |")
        print("--------------------------------------------------------------------------------------------")
        for soba in pogodjene_sobe:
            print("|" + soba['id'].ljust(8) + "|" + soba['broj_sobe'].ljust(13) + "|" + soba['broj_kreveta'].ljust(14) + "|" + soba['tip'].ljust(
                11) + "|" + soba['klima'].ljust(9) + "|" + soba['tv'].ljust(4) + "|" + soba['cena'].ljust(10) + "|" + soba['dostupnost'].ljust(14) + "|")
        print("--------------------------------------------------------------------------------------------")
        opcije(korisnicko_ime)
    else:
        print("Nemamo takvih soba.")
    opcije(korisnicko_ime)


def odjava():
    print("---------------------")
    print("|    Dovidjenja!    |")
    print("---------------------")
    print("Molimo vas unesite vase podatke kako bi ste se prijavili")
    Registrovani_korisnik.prijava()


def pretraga_rezervacija(korisnicko_ime):
    print("1)Pretraga na osnovu jednog kriterijuma")
    print("2)Pretraga po vise kriterijuma")
    opcija = int(input("Kako zelite da pretrazujete? 1/2: "))
    while opcija not in range(1, 3):
        print("opcije su 1 i 2! ")
        opcija = int(input("Kako zelite da pretrazujete? 1/2: "))
    if opcija == 1:
        jedan_kriterijum_r(korisnicko_ime)
    elif opcija == 2:
        vise_kriterijuma_r(korisnicko_ime)


def jedan_kriterijum_r(korisnicko_ime):
    print("Pretraga na osnovu jednog kriterijuma:")
    print("1) Datum i vreme kreiranja rezervacije")
    print("2) Datum i vreme prijave iz hotela")
    print("3) Datum i vreme odjave iz hotela")
    print("4) Ime korisnika")
    print("5) Status")

    opcija = int(
        input("Unesite na osnovu kog kriterijuma zelite pretrazivati: "))
    while opcija not in range(1, 6):
        print("Morate uneti broj od 1 do 5!")
        opcija = int(input(
            "Unesite na osnovu kog kriterijuma zelite pretrazivati: "))
    unos = input("Unesite zeljenu karakteristiku: ")
    rezervacija = {}

    if opcija == 1:
        rezervacija['datum_kreiranja'] = unos
    elif opcija == 2:
        rezervacija['datum_prijave'] = unos
    elif opcija == 3:
        rezervacija['datum_odjave'] = unos
    elif opcija == 4:
        rezervacija['ime_korisnika'] = unos
    elif opcija == 5:
        rezervacija['status'] = unos

    rezervacije = open("rezervacije.txt", "r")
    rezervacije_ucitano = {}
    pogodjene_rezervacije = []
    for jedna_rezervacija in rezervacije.readlines():
        odlika = jedna_rezervacija.rstrip("\n").split("|")
        rezervacije_ucitano = {'id': odlika[0], 'lista_soba': odlika[2], 'datum_kreiranja': odlika[3],
                               'datum_prijave': odlika[4], 'datum_odjave': odlika[5], 'ime_korisnika': odlika[6], 'status': odlika[7], 'ocena': odlika[8]}
        if rezervacija.items() <= rezervacije_ucitano.items():
            pogodjene_rezervacije.append(rezervacije_ucitano)

    if len(pogodjene_rezervacije) != 0:
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
        print("|   ID   |  Lista rezervisanih soba  |   Datum kreiranja   |    Datum prijave    |    Datum odjave    |  Ime korisnika  |    Status    | Ocena |")
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
        for rezervacija in pogodjene_rezervacije:
            print("|" + rezervacija['id'].ljust(8) + "|" + rezervacija['lista_soba'].ljust(27) + "|" + rezervacija['datum_kreiranja'].ljust(21) + "|" + rezervacija['datum_prijave'].ljust(
                21) + "|" + rezervacija['datum_odjave'].ljust(20) + "|" + rezervacija['ime_korisnika'].ljust(17) + "|" + rezervacija['status'].ljust(14) + "|" + rezervacija['ocena'].ljust(7) + "|")
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
        opcije(korisnicko_ime)
    else:
        print("Nema takvih rezervacija.")
    rezervacije.close()
    opcije(korisnicko_ime)


def vise_kriterijuma_r(korisnicko_ime):
    print("Pretraga na osnovu jednog kriterijuma:")
    print("1) Datum i vreme kreiranja rezervacije")
    print("2) Datum i vreme prijave iz hotela")
    print("3) Datum i vreme odjave iz hotela")
    print("4) Ime korisnika")
    print("5) Status")

    opcija = int(
        input("Unesite na osnovu kog kriterijuma zelite pretrazivati: "))
    while opcija not in range(1, 6):
        print("Morate uneti broj od 1 do 5!")
        opcija = int(input(
            "Unesite na osnovu kog kriterijuma zelite pretrazivati: "))
    unos = input("Unesite zeljenu karakteristiku: ")
    rezervacija = {}

    if opcija == 1:
        rezervacija['datum_kreiranja'] = unos
    elif opcija == 2:
        rezervacija['datum_prijave'] = unos
    elif opcija == 3:
        rezervacija['datum_odjave'] = unos
    elif opcija == 4:
        rezervacija['ime_korisnika'] = unos
    elif opcija == 5:
        rezervacija['status'] = unos

    pitanje = input("Zelite li da unesete jos jedan kriterijum? (da/ne)")
    while pitanje != "da" and pitanje != "ne":
        print('Molim vas unesite da ili ne!')
        pitanje = input("Zelite li da unesete jos jedan kriterijum? (da/ne)")

    while pitanje == "da":
        opcija2 = int(input(
            "Unesite na osnovu kog kriterijuma zelite pretrazivati: "))
        while opcija not in range(1, 6):
            print("Morate uneti broj od 1 do 5!")
            opcija2 = int(input(
                "Unesite na osnovu kog kriterijuma zelite pretrazivati: "))
        unos2 = input("Unesite zeljenu karakteristiku: ")
        if opcija2 == 1:
            rezervacija['datum_kreiranja'] = unos2
        elif opcija2 == 2:
            rezervacija['datum_prijave'] = unos2
        elif opcija2 == 3:
            rezervacija['datum_odjave'] = unos2
        elif opcija2 == 4:
            rezervacija['ime_korisnika'] = unos2
        elif opcija2 == 5:
            rezervacija['status'] = unos2

        pitanje = input("Zelite li da unesete jos jedan kriterijum? (da/ne)")
        while pitanje != "da" and pitanje != "ne":
            print('Molim vas unesite da ili ne!')
            pitanje = input(
                "Zelite li da unesete jos jedan kriterijum? (da/ne)")

    rezervacije = open("rezervacije.txt", "r")
    pogodjene_rezervacije = []
    for jedna_rezervacija in rezervacije.readlines():
        odlika = jedna_rezervacija.rstrip("\n").split("|")
        rezervacije_ucitano = {'id': odlika[0], 'lista_soba': odlika[2], 'datum_kreiranja': odlika[3],
                               'datum_prijave': odlika[4], 'datum_odjave': odlika[5], 'ime_korisnika': odlika[6], 'status': odlika[7], 'ocena': odlika[8]}
        if rezervacija.items() <= rezervacije_ucitano.items():
            pogodjene_rezervacije.append(rezervacije_ucitano)

    if len(pogodjene_rezervacije) != 0:
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
        print("|   ID   |  Lista rezervisanih soba  |   Datum kreiranja   |    Datum prijave    |    Datum odjave    |  Ime korisnika  |    Status    | Ocena |")
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
        for rezervacija in pogodjene_rezervacije:
            print("|" + rezervacija['id'].ljust(8) + "|" + rezervacija['lista_soba'].ljust(27) + "|" + rezervacija['datum_kreiranja'].ljust(21) + "|" + rezervacija['datum_prijave'].ljust(
                21) + "|" + rezervacija['datum_odjave'].ljust(20) + "|" + rezervacija['ime_korisnika'].ljust(17) + "|" + rezervacija['status'].ljust(14) + "|" + rezervacija['ocena'].ljust(7) + "|")
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
        opcije(korisnicko_ime)
    else:
        print("Nema takvih rezervacija.")
    opcije(korisnicko_ime)


# def izvestaj(korisnicko_ime):
#     print("----------------------------")
#     print("1) Dnevni izvestaj")
#     print("2) Nedeljni izvestaj")
#     print("3) Mesecni izvestaj")
#     print("----------------------------")
#     opcija = int(input("Izaberite opciju: "))
#     while opcija not in range(1, 4):
#         print("Opcije su od 1 do 3!")
#         opcija = input("Izaberite opciju: ")
#     if opcija == 1:
#         dnevni_izvestaj()
#         opcije(korisnicko_ime)
#     elif opcija == 2:
#         nedeljni_izvestaj()
#         opcije(korisnicko_ime)
#     elif opcija == 3:
#         meseci_izvestaj()
#         opcije(korisnicko_ime)


# def dnevni_izvestaj():


# def nedeljni_izvestaj():


# def meseci_izvestaj():
