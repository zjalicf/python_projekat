import Recepcioner
import Administrator
from datetime import date, datetime
from random import randint


def main():
    prijava()


def prijava():
    korisnici = open("korisnici.txt", "r")
    lines = korisnici.readlines()
    ime = input("Unesite korisnicko ime: ")
    lozinka = input("Unesite lozinku: ")
    korisnik = ""

    for value in lines:
        info = value.split("|")
        ime_korisnika = info[0]
        lozinka_korisnika = info[1]
        tip_korisnika = info[6].rstrip("\n")

        if ime == ime_korisnika and lozinka == lozinka_korisnika:
            print("-----------------------------------------")
            print("|      Uspesno ste se ulogovali!        |")
            print("-----------------------------------------")
            if tip_korisnika == "registrovani":
                korisnik = "registrovani"
                korisnicko_ime = ime_korisnika

            if tip_korisnika == "recepcioner":
                korisnik = "recepcioner"
                korisnicko_ime = ime_korisnika

            if tip_korisnika == "admin":
                korisnik = "admin"
                korisnicko_ime = ime_korisnika

            opcije(korisnik, korisnicko_ime)
            return korisnik

    print("Uneli ste pogresno ime ili lozinku. Pokusajte ponovo")
    prijava()

    korisnici.close()


def opcije(korisnik, korisnicko_ime):
    if korisnik == "registrovani":
        opcije_registrovani(korisnicko_ime)
    elif korisnik == "recepcioner":
        Recepcioner.opcije(korisnicko_ime)
    elif korisnik == "admin":
        Administrator.opcije(korisnicko_ime)


def opcije_registrovani(korisnicko_ime):
    print("Pozdrav {}!".format(korisnicko_ime))
    print("1. Pregled hotela")
    print("2. Pretraga hotela")
    print("3. Prikaz najbolje ocenjenih hotela")
    print("4. Kreiranje rezervacije")
    print("5. Pregled rezervacija")
    print("6. Ocenjivanje hotela")
    print("7. Odjava")

    opcija = int(input("Izaberite jednu od ponudjenih opcija: "))
    while opcija not in range(1, 8):
        print("Unesite broj od 1 do 8!")
        opcija = int(input("Izaberite jednu od ponudjenih opcija: "))
    if opcija == 1:
        pregled_hotela(korisnicko_ime)
    elif opcija == 2:
        pretraga_hotela(korisnicko_ime)
    elif opcija == 3:
        najbolje_ocenjeni(korisnicko_ime)
    elif opcija == 4:
        kreiranje_rez(korisnicko_ime)
    elif opcija == 5:
        pregled_rez(korisnicko_ime)
    elif opcija == 6:
        ocena(korisnicko_ime)
    elif opcija == 7:
        odjava(korisnicko_ime)


def pregled_hotela(korisnicko_ime):
    print("-----------------------------------------------------------------")
    print("|                         LISTA HOTELA                          |")
    print("-----------------------------------------------------------------")
    print("|   Naziv   |   Adresa   |   Ocena   |   Bazen   |   Restoran   |")
    print("-----------------------------------------------------------------")

    info_hotela = open("hoteli.txt", "r")
    hoteli = info_hotela.readlines()

    for hotel in hoteli:
        info = hotel.rstrip("\n").split("|")
        naziv = info[1]
        adresa = info[2]
        ocena = info[6]
        bazen = info[4]
        restoran = info[5]

        print("|" + naziv.ljust(11) + "|" + adresa.ljust(12) +
              "|" + ocena.ljust(11) + "|" + bazen.ljust(11) +
              "|" + restoran.ljust(14) + "|")
    print("-----------------------------------------------------------------")
    info_hotela.close()
    opcije_registrovani(korisnicko_ime)


def pretraga_hotela(korisnicko_ime):
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
    print("Pretraga na osnovu jednog kriterijuma: ")
    print("1) Naziv")
    print("2) Adresa")
    print("3) Ocena")

    opcija = int(
        input("Unesite na osnovu kog kriterijuma zelite pretrazivati: "))
    while opcija not in range(1, 4):
        print("Morate uneti broj 1, 2 ili 3!!")
        opcija = int(
            input("Unesite na osnovu kog kriterijuma zelite pretrazivati: "))
    unos = input("Unesite zeljenu karakteristiku: ")
    hotel = {}

    if opcija == 1:
        hotel['naziv'] = unos
    if opcija == 2:
        hotel['adresa'] = unos
    if opcija == 3:
        hotel['ocena'] = unos

    hoteli = open("hoteli.txt", "r")
    hotel_ucitano = {}
    pogodjeni_hoteli = []
    for jedan_hotel in hoteli.readlines():
        value = jedan_hotel.rstrip("\n").split("|")
        hotel_ucitano = {'id': value[0], 'naziv': value[1], 'adresa': value[2],
                         'lista_soba': value[3], 'bazen': value[4], 'restoran': value[5], 'ocena': value[6]}
        if hotel.items() <= hotel_ucitano.items():
            pogodjeni_hoteli.append(hotel_ucitano)

    if len(pogodjeni_hoteli) != 0:
        print("-------------------------------------------------------------------------------------------------")
        print("|   ID   |   naziv   |    adresa    |      lista soba      |   bazen   |   restoran   |  ocena  |")
        print("-------------------------------------------------------------------------------------------------")
        for hotel in pogodjeni_hoteli:
            print("|" + hotel['id'].ljust(8) + "|" + hotel['naziv'].ljust(11) + "|" + hotel['adresa'].ljust(14) + "|" + hotel['lista_soba'].ljust(
                22) + "|" + hotel['bazen'].ljust(11) + "|" + hotel['restoran'].ljust(14) + "|" + hotel['ocena'].ljust(9) + "|")
        print("-------------------------------------------------------------------------------------------------")
        opcije_registrovani(korisnicko_ime)
    else:
        print("Nemamo takvih hotela.")
    hoteli.close()
    opcije_registrovani(korisnicko_ime)


def vise_kriterijuma(korisnicko_ime):
    print("Pretraga na osnovu vise kriterijuma: ")
    print("1) Naziv")
    print("2) Adresa")
    print("3) Ocena")

    opcija = int(
        input("Unesite na osnovu kog kriterijuma zelite pretrazivati: "))
    while opcija not in range(1, 4):
        print("Morate uneti broj 1, 2 ili 3!!")
        opcija = int(input(
            "Unesite na osnovu kog kriterijuma zelite pretrazivati: "))
    unos = input("Unesite zeljenu karakteristiku: ")
    hotel = {}

    if opcija == 1:
        hotel['naziv'] = unos
    elif opcija == 2:
        hotel['adresa'] = unos
    elif opcija == 3:
        hotel['ocena'] = unos

    pitanje = input("Zelite li da unesete jos jedan kriterijum? (da/ne)")

    while pitanje != "da" and pitanje != "ne":
        print('Molim vas unesite da ili ne!')
        pitanje = input("Zelite li da unesete jos jedan kriterijum? (da/ne)")

    while pitanje == "da":
        opcija2 = int(input(
            "Unesite na osnovu kog kriterijuma zelite pretrazivati: "))
        while opcija2 not in range(1, 4):
            print("Morate uneti broj 1, 2 ili 3!!")
            opcija2 = int(input(
                "Unesite na osnovu kog kriterijuma zelite pretrazivati: "))
        unos2 = input("Unesite zeljenu karakteristiku: ")
        if opcija2 == 1:
            hotel['naziv'] = unos2
        elif opcija2 == 2:
            hotel['adresa'] = unos2
        elif opcija2 == 3:
            hotel['ocena'] = unos2

        pitanje = input("Zelite li da unesete jos jedan kriterijum? (da/ne)")
        while pitanje != "da" and pitanje != "ne":
            print('Molim vas unesite da ili ne!')
            pitanje = input(
                "Zelite li da unesete jos jedan kriterijum? (da/ne)")

    hoteli = open("hoteli.txt", "r")
    pogodjeni_hoteli = []
    for jedan_hotel in hoteli.readlines():
        odlika = jedan_hotel.rstrip("\n").split("|")
        hotel_ucitano = {'id': odlika[0], 'naziv': odlika[1], 'adresa': odlika[2],
                         'lista_soba': odlika[3], 'bazen': odlika[4], 'restoran': odlika[5], 'ocena': odlika[6]}
        if hotel.items() <= hotel_ucitano.items():
            pogodjeni_hoteli.append(hotel_ucitano)

    if len(pogodjeni_hoteli) != 0:
        print("-------------------------------------------------------------------------------------------------")
        print("|   ID   |   naziv   |    adresa    |      lista soba      |   bazen   |   restoran   |  ocena  |")
        print("-------------------------------------------------------------------------------------------------")
        for hotel in pogodjeni_hoteli:
            print("|" + hotel['id'].ljust(8) + "|" + hotel['naziv'].ljust(11) + "|" + hotel['adresa'].ljust(14) + "|" + hotel['lista_soba'].ljust(
                22) + "|" + hotel['bazen'].ljust(11) + "|" + hotel['restoran'].ljust(14) + "|" + hotel['ocena'].ljust(9) + "|")
        print("-------------------------------------------------------------------------------------------------")
        opcije_registrovani(korisnicko_ime)
    else:
        print("Nema takvih hotela.")
    hoteli.close()
    opcije_registrovani(korisnicko_ime)


def najbolje_ocenjeni(korisnicko_ime):
    print("----------------------------------")
    print("|    NAJBOLJE OCENJENI HOTELI    |")
    print("----------------------------------")
    print("|   Naziv   |   Adresa   | Ocena |")
    print("----------------------------------")
    hoteli = open("hoteli.txt", "r")
    hotel_citanje = hoteli.readlines()
    hoteli.close()
    lista = []
    for line in hotel_citanje:
        value = line.rstrip("\n").split("|")
        hotel = {'id': value[0], 'naziv': value[1], 'adresa': value[2],
                 'lista_soba': value[3], 'bazen': value[4], 'restoran': value[5], 'ocena': value[6]}
        lista.append(hotel)

    sortirana_lista = sorted(
        lista, key=lambda k: k['ocena'], reverse=True)
    sortirana_prvih_pet = sortirana_lista[:5]

    for hotel in sortirana_prvih_pet:
        print("|" + hotel['naziv'].ljust(11) + "|" +
              hotel['adresa'].ljust(12) + "|" + hotel['ocena'].ljust(7) + "|")
    print("--------------------------------")
    opcije_registrovani(korisnicko_ime)


def kreiranje_rez(korisnicko_ime):
    print("-----------------------------------------------------------------")
    print("|                         LISTA HOTELA                          |")
    print("-----------------------------------------------------------------")
    print("|   Naziv   |   Adresa   |   Ocena   |   Bazen   |   Restoran   |")
    print("-----------------------------------------------------------------")

    info_hotela = open("hoteli.txt", "r")
    hoteli = info_hotela.readlines()

    for hotel in hoteli:
        info = hotel.rstrip("\n").split("|")
        naziv = info[1]
        adresa = info[2]
        ocena = info[6]
        bazen = info[4]
        restoran = info[5]

        print("|" + naziv.ljust(11) + "|" + adresa.ljust(12) +
              "|" + ocena.ljust(11) + "|" + bazen.ljust(11) +
              "|" + restoran.ljust(14) + "|")
    print("-----------------------------------------------------------------")
    info_hotela.close()

    hoteli = open("hoteli.txt", "r")
    hotel_citanje = hoteli.readlines()
    lista_naziva = []
    lista_soba = []
    for hotel in hotel_citanje:
        odlika = hotel.rstrip('\n').split('|')
        lista_naziva.append(odlika[1])
        lista_soba.append(odlika[3])
    hoteli.close()

    izbor = input('Izaberite hotel (naziv): ')

    if izbor in lista_naziva:
        print('Izabrali ste hotel {}. '.format(izbor), end='')
    else:
        print('Nemamo hotel sa takvim nazivom!')
        kreiranje_rez(korisnicko_ime)

    hoteli2 = open("hoteli.txt", "r")
    hotel_citanje2 = hoteli2.readlines()
    trenutni_hotel = []
    for hotel2 in hotel_citanje2:
        odlika2 = hotel2.rstrip('\n').split('|')
        if izbor == odlika2[1]:
            trenutni_hotel = odlika2
    hoteli.close()

    prikaz_soba = ''
    for j in trenutni_hotel[3]:
        if j != '[' and j != ']':
            prikaz_soba += j
        else:
            continue

    str1 = trenutni_hotel[3].replace("[", "")
    str2 = str1.replace("]", "")
    lista_soba_fixed = list(str2.split(", "))

    print('U ovom hotelu postoje sledece sobe: ', prikaz_soba)

    dostupne_sobe = []
    rezervacije = open("rezervacije.txt", "r")
    rezervacije_citanje = rezervacije.readlines()
    for rezervacija in rezervacije_citanje:
        odlika_r = rezervacija.rstrip('\n').split('|')
        naziv_hotela = odlika_r[1]
        ime = odlika_r[6]
        str4 = odlika_r[2].replace("'", "")
        lista_rez_soba = str4.strip('][').split(', ')
        status = odlika_r[7]
        for k in lista_soba_fixed:
            if ime == korisnicko_ime and naziv_hotela == izbor and k.replace("'", "") in lista_rez_soba and status != 'zavrsena':
                continue
            elif ime == korisnicko_ime and naziv_hotela == izbor and k.replace("'", "") in lista_rez_soba and status == 'zavrsena' and k.replace("'", "") not in dostupne_sobe:
                dostupne_sobe.append(k.replace("'", ""))
            elif ime == korisnicko_ime and naziv_hotela == izbor and k.replace("'", "") not in lista_rez_soba and k.replace("'", "") not in dostupne_sobe:
                dostupne_sobe.append(k.replace("'", ""))

    prikaz_dostupnih_soba = ''
    lista_izabranih_soba = []
    rezervacije.close()
    for j in dostupne_sobe:
        if j != '[' and j != ']':
            prikaz_dostupnih_soba += j
            prikaz_dostupnih_soba += ' '
        else:
            continue

    izbor_sobe = input("Dostupne sobe su: {}\nMolim vas izaberite sobu koju zelite da rezervisete: ".format(
        prikaz_dostupnih_soba))
    while izbor_sobe not in dostupne_sobe:
        print('Molim vas odaberite neku od navedenih soba!')
        izbor_sobe = input("Dostupne sobe su: {}\nMolim vas izaberite sobu koju zelite da rezervisete: ".format(
            prikaz_dostupnih_soba))
    dostupne_sobe2 = []
    lista_izabranih_soba.append(izbor_sobe)
    for i in dostupne_sobe:
        if i == izbor_sobe:
            continue
        else:
            dostupne_sobe2.append(i)
    if dostupne_sobe2 != []:
        prikaz_dostupnih_soba2 = ''
        for j in dostupne_sobe2:
            if j != '[' and j != ']':
                prikaz_dostupnih_soba2 += j
                prikaz_dostupnih_soba2 += ' '
            else:
                continue

        pitanje = input('Da li zelite da rezervisete jos soba? (da/ne)')

        while pitanje != "da" and pitanje != "ne":
            print('Molim vas unesite da ili ne!')
            pitanje = input('Da li zelite da rezervisete jos soba? (da/ne)')

        while pitanje == "da":
            print('Trenutno dostupne sobe su: {}'.format(prikaz_dostupnih_soba2))
            izbor_sobe2 = input('Unesite broj sobe: ')
            while izbor_sobe2 not in dostupne_sobe2:
                print('Molim vas odaberite neku od navedenih soba!')
                izbor_sobe2 = input('Unesite broj sobe: ')
            lista_izabranih_soba.append(izbor_sobe2)
            for i in dostupne_sobe2:
                if i == izbor_sobe2:
                    dostupne_sobe2.remove(izbor_sobe2)
                else:
                    continue
            pitanje = input('Da li zelite da uneste jos soba? (da/ne)')

            while pitanje != "da" and pitanje != "ne":
                print('Molim vas unesite da ili ne!')
                pitanje = input('Da li zelite da uneste jos soba? (da/ne)')
    # -----------------------------------------------------------------------------------------------------------------------
    trenutni_datum = str(date.today())
    id_rezervacije = str(randint(100000, 999999))
    temp = str(datetime.now())
    datum_kreiranja = temp[:16]

    datum_prijave = input(
        'Kada zelite da se prijavite u hotel? (unesite u formatu yyyy-mm-dd): ')
    while datum_prijave < trenutni_datum:
        print("Datum prijave ne moze biti u proslosti!")
        datum_prijave = input(
            'Kada zelite da se prijavite u hotel? (unesite u formatu yyyy-mm-dd): ')
    datum_odjave = input(
        'Kada zelite da se odjavite iz hotela? (unesite u formatu yyyy-mm-dd): ')
    while datum_odjave < trenutni_datum or datum_odjave < datum_prijave:
        if datum_odjave < trenutni_datum:
            print("Datum odjave ne moze biti u proslosti!")
            datum_odjave = input(
                'Kada zelite da se odjavite iz hotela? (unesite u formatu yyyy-mm-dd): ')
        else:
            print("Datum odjave ne moze biti pre datuma prijave!")
            datum_odjave = input(
                'Kada zelite da se odjavite iz hotela? (unesite u formatu yyyy-mm-dd): ')
    ime_korisnika = korisnicko_ime
    status = 'nije zapoceta'
    ocena = '/'

    rezervacije = open('rezervacije.txt', 'a')
    rezervacije.write('\n' + id_rezervacije + '|' + izbor + '|' + str(lista_izabranih_soba) + '|' + datum_kreiranja +
                      '|' + datum_prijave + '|' + datum_odjave + '|' + ime_korisnika + '|' + status + "|" + ocena)
    rezervacije.close()
    print('Uspesna rezervacija!')
    opcije_registrovani(korisnicko_ime)


def pregled_rez(korisnicko_ime):
    rezervacije = open('rezervacije.txt', 'r')
    print("-------------------------------------------------------------------------------------------------------------")
    print('|                                             VASE REZERVACIJE                                              |')
    print("-------------------------------------------------------------------------------------------------------------")
    print('|  Ime hotela   |     Lista soba     |   Datum kreiranja  |  Datum prijave  |  Datum odjave  |    Status    |')
    for i in rezervacije.readlines():
        odlika = i.rstrip("\n").split("|")
        ime_hotela = odlika[1]
        lista_soba = odlika[2]
        datum_kreiranja = odlika[3]
        datum_prijave = odlika[4]
        datum_odjave = odlika[5]
        status = odlika[7]
        if korisnicko_ime == odlika[6]:
            print('|' + ime_hotela.ljust(15) + '|' + lista_soba.ljust(20) + '|' + datum_kreiranja.ljust(20) + '|' +
                  datum_prijave.ljust(17) + '|' + datum_odjave.ljust(16) + '|' + status.ljust(14) + '|')
    rezervacije.close()
    print("-------------------------------------------------------------------------------------------------------------")
    print('Mozete videti prethodne rezervacije, one koje jos nisu zapocete ili one koje su u toku.')
    izbor = int(input(
        'Za prethodne rezervacije unesite 1, za one koje nisu zapocete 2 a za one koje su u toku 3: '))
    while izbor not in range(1, 4):
        print("Molim vas izaberite nesto od ponudjenog!")
        izbor = int(input(
            'Za prethodne rezervacije unesite 1, za one koje nisu zapocete 2 a za one koje su u toku 3: '))
    rezervacije = open('rezervacije.txt', 'r')
    if izbor == 1:
        for i2 in rezervacije.readlines():
            odlika2 = i2.rstrip("\n").split("|")
            ime_hotela2 = odlika2[1]
            lista_soba2 = odlika2[2]
            datum_kreiranja2 = odlika2[3]
            datum_prijave2 = odlika2[4]
            datum_odjave2 = odlika2[5]
            status2 = odlika2[7]
            if korisnicko_ime == odlika2[6] and status2 == 'zavrsena':
                print(
                    "-----------------------------------------------------------------------------------------------------------")
                print(
                    '|  Ime hotela   |     Lista soba     |   Datum kreiranja  |  Datum prijave  |  Datum odjave  |   Status   |')
                print('|' + ime_hotela2.ljust(15) + '|' + lista_soba2.ljust(20) + '|' + datum_kreiranja2.ljust(20) + '|' +
                      datum_prijave2.ljust(17) + '|' + datum_odjave2.ljust(16) + '|' + status2.ljust(12) + '|')
                print(
                    "-----------------------------------------------------------------------------------------------------------")
        opcije_registrovani(korisnicko_ime)
    else:
        print('Nema takvih rezervacija!')
        rezervacije.close()
        opcije_registrovani(korisnicko_ime)
    if izbor == 2:
        for i3 in rezervacije.readlines():
            odlika3 = i3.rstrip("\n").split("|")
            ime_hotela3 = odlika3[1]
            lista_soba3 = odlika3[2]
            datum_kreiranja3 = odlika3[3]
            datum_prijave3 = odlika3[4]
            datum_odjave3 = odlika3[5]
            status3 = odlika3[7]
            if korisnicko_ime == odlika3[6] and status3 == 'nije zapoceta':
                print(
                    "-----------------------------------------------------------------------------------------------------------")
                print(
                    '|  Ime hotela   |     Lista soba     |   Datum kreiranja  |  Datum prijave  |  Datum odjave  |   Status   |')
                print('|' + ime_hotela3.ljust(15) + '|' + lista_soba3.ljust(20) + '|' + datum_kreiranja3.ljust(20) + '|' +
                      datum_prijave3.ljust(17) + '|' + datum_odjave3.ljust(16) + '|' + status3.ljust(12) + '|')
                print(
                    "-----------------------------------------------------------------------------------------------------------")
        opcije_registrovani(korisnicko_ime)
    else:
        print('Nema takvih rezervacija!')
        rezervacije.close()
        opcije_registrovani(korisnicko_ime)
    if izbor == 3:
        for i4 in rezervacije.readlines():
            odlika4 = i4.rstrip("\n").split("|")
            ime_hotela4 = odlika4[1]
            lista_soba4 = odlika4[2]
            datum_kreiranja4 = odlika4[3]
            datum_prijave4 = odlika4[4]
            datum_odjave4 = odlika4[5]
            status4 = odlika4[7]
            if korisnicko_ime == odlika4[6] and status4 == 'zapoceta':
                print(
                    "-----------------------------------------------------------------------------------------------------------")
                print(
                    '|  Ime hotela   |     Lista soba     |   Datum kreiranja  |  Datum prijave  |  Datum odjave  |   Status   |')
                print('|' + ime_hotela4.ljust(15) + '|' + lista_soba4.ljust(20) + '|' + datum_kreiranja4.ljust(20) + '|' +
                      datum_prijave4.ljust(17) + '|' + datum_odjave4.ljust(16) + '|' + status4.ljust(12) + '|')
                print(
                    "-----------------------------------------------------------------------------------------------------------")
        opcije_registrovani(korisnicko_ime)
    else:
        print('Nema takvih rezervacija!')
        rezervacije.close()
    print('\n')
    opcije_registrovani(korisnicko_ime)


def ocena(korisnicko_ime):
    rezervacije = open('rezervacije.txt', 'r')
    print('Mozete oceniti samo prethodne rezervacije koje nisu ocenjene!')

    lista_id = []
    pogodjene_rezervacije = []
    for i in rezervacije.readlines():
        odlika = i.rstrip("\n").split("|")
        id_rezervacije = odlika[0]
        status = odlika[7]
        ocena = odlika[8]
        lista_id.append(id_rezervacije)
        rezervacije_ucitano = {'id_rezervacije': odlika[0], 'ime_hotela': odlika[1], 'lista_soba': odlika[2],
                               'datum_kreiranja': odlika[3], 'datum_prijave': odlika[4], 'datum_odjave': odlika[5], 'status': odlika[6]}

        if korisnicko_ime == odlika[6] and status == 'zavrsena' and ocena == '/':
            pogodjene_rezervacije.append(rezervacije_ucitano)

    if len(pogodjene_rezervacije) == 0:
        print("Nastala je greska. Postoje dve mogucnosti: ")
        print("1. Nemate nijednu zavrsenu rezervaciju")
        print("2. Vec ste ocenili sve zavrsene rezervacije")
        print("Molim vas pokusajte ponovo")
        rezervacije.close()
        opcije_registrovani(korisnicko_ime)
    else:
        print('| ID rezervacije |   Ime hotela   |      Lista soba      |    Datum kreiranja   |   Datum prijave   |   Datum odjave   |    Status    |')
        for rezervacija in pogodjene_rezervacije:
            print("|" + rezervacija['id_rezervacije'].ljust(16) + "|" + rezervacija['ime_hotela'].ljust(16) + "|" + rezervacija['lista_soba'].ljust(22) + "|" +
                  rezervacija['datum_kreiranja'].ljust(22) + "|" + rezervacija['datum_prijave'].ljust(19) + "|" + rezervacija['datum_odjave'].ljust(18) + "|" + rezervacija['status'].ljust(14) + "|")

    rezervacije.close()
    izbor = input('Izaberite ID rezervacije koju zelite da ocenite: ')
    while izbor not in lista_id:
        print("Molim vas izaberite jednu od ponudjenih rezervacija")
        izbor = input('Izaberite ID rezervacije koju zelite da ocenite: ')
    ocena = input('Unesite ocenu od 1 do 5: ')
    while int(ocena) not in range(1, 6):
        print('Molim vas unesite ocenu od 1 do 5: ')
        ocena = input('Unesite ocenu od 1 do 5: ')

    rezervacije2 = open('rezervacije.txt', 'r')
    str1 = ''
    str2 = ''
    for j in rezervacije2.readlines():
        odlika2 = j.rstrip("\n").split("|")
        if izbor == odlika2[0]:
            odlika2[8] = ocena
            str2 = odlika2[0] + '|' + odlika2[1] + '|' + odlika2[2] + '|' + \
                odlika2[3] + '|' + odlika2[4] + '|' + \
                odlika2[5] + '|' + odlika2[6] + '|' + \
                odlika2[7] + '|' + odlika2[8] + '\n'
            str1 += str2
            print("Uspesno ste ocenili hotel {} sa ocenom {}.".format(
                odlika2[1], ocena))
        else:
            str1 += j
    rezervacije2.close()
    rez_upis = open('rezervacije.txt', 'w')
    rez_upis.write(str1)
    rez_upis.close()
    opcije_registrovani(korisnicko_ime)


def odjava(korisnicko_ime):
    print("Dovidjenja, {}.".format(korisnicko_ime))
    print("Molimo vas unesite vase podatke kako bi ste se prijavili")
    prijava()
