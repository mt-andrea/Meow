import os

def main():
    filename=""
    run_while=True
    while run_while:
        if filename=="":
            print("\t1 - Fájlok kilistázása \n\t2 - Fájl kiválasztása/létrehozása \n\t3 - Kilépés")
            choise=input("Válasszon menüpontot(1-3): ")
            if choise=="1":
                listing_files()
            elif choise=="2":
                filename=filename_please()
            elif choise=="3":
                print("Kilépés")
                run_while=False
            else:
                print("Nincs ilyen menüpontunk.")
        else:
            print("\t1 - Adatok kiírása \n\t2 - Adat hozzáfűzése \n\t3 - Keresés a fájlban \n\t4 - Fájl bezárása \n\t5 - Kilépés")
            choise=input("Válasszon menüpontot(1-5): ")
            if choise=="1":
                print_data(filename)
            elif choise=="2":
                append_file(filename)
            elif choise=="3":
                search_in_file(filename)
            elif choise=="4":
                filename=""
            elif choise=="5":
                print("Kilépés")
                run_while=False
            else:
                print("Nincs ilyen menüpontunk.")

def listing_files():
    for f in os.listdir():
        if f.endswith(".txt"):
            print(f)

def filename_please():
    filename=input("Kérem egy fájl nevét, amivel dolgozni fogunk (*.txt kérem a kiterjesztést is): ")
    if not os.path.exists(filename):
        open(filename,'a').close()
    return filename

def print_data(filename):
    f=open(filename,"r")
    data=f.read()
    print(data)

def append_file(filename):
    f=open(filename,"a")
    name=input("Kérem egy hegység nevét: ")
    search_name()
    hight=input("Kérem a legmagasabb csúcs magasságát (m): ")
    f.write(name+"\t"+hight+"\n")
    print(filename+" bővült a következő sorral: "+name+"\t"+hight)

def search_in_file():
    print("Mit keressünk? \n\t1 - Legalacsonyabb hegység \n\t2 - Legmagasabb hegység \n\t3 - Hegység neve \n\t4 - Magasság")

def search_min():
    pass

def search_max():
    pass

def search_name():
    pass

def search_hight():
    pass

main()