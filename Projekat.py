import Neregistrovani_korisnik
import Registrovani_korisnik


def opcije():
    print("-------------------")
    print("...: HOTEL APP :...")
    print("-------------------")
    print("1. Registruj se")
    print("2. Prijavi se")
    print("3. Izlaz")
    print("-------------------")


def main():
    opcije()
    opcija = int(input("Molim vas izaberite opciju: "))
    while opcija not in range(1, 4):
        print("--GRESKA!")
        print("\nMolim vas unesite opciju 1, 2 ili 3!\n")
        opcija = int(input("Molim vas izaberite opciju: "))
    if opcija == 1:
        Neregistrovani_korisnik.opcije()
    elif opcija == 2:
        Registrovani_korisnik.main()
    elif opcija == 3:
        print("---------------")
        print("| Dovidjenja! |")
        print("---------------")


main()
