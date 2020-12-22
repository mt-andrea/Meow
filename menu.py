def main():
    filename=filename_please()
    while filename=="":
        print("\t1 - Fájlok kilistázása \n\t2 - Fájl kiválasztása/létrehozása \n\t3 - Kilépés")
        choise=input("Válasszon menüpontot(1-3): ")
        if choise=="1":
            listing_files()
        elif choise=="2":
            filename_please()
        elif choise=="3":
            print("Kilépés")
            exit()
        else:
            print("Nincs ilyen menüpontunk.")
    while filename!="":
        f=reading(filename)
        print("\t1 - Adatok kiírása \n\t2 - Adat hozzáfűzése \n\t3 - Keresés a fájlban \n\t4 - Fájl bezárása \n\t5 - Kilépés")
        choise=input("Válasszon menüpontot(1-5): ")
        if choise=="1":
            print_data(f)
        elif choise=="2":
            append_file(filename)
        elif choise=="3":
            search_in_file(filename)
        elif choise=="4":
            close_file(f)
        elif choise=="5":
            print("Kilépés")
            exit()
        else:
            print("Nincs ilyen menüpontunk.")
def listing_files():
    pass
def filename_please():
    filename=input("Kérem egy fájl nevét, amivel dolgozni fogunk (*.txt kérem a kiterjesztést is): ")
    return filename
def print_data(f):
    data=f.read()
    print(data)
def append_file(filename):
    f=reading(filename)
    name=input("Kérem egy hegység nevét: ")
    search_name()
    hight=input("Kérem a legmagasabb csúcs magasságát (m): ")
    f.write(name+"\t"+hight+"\n")
    print(filename+" bővült a következő sorral: "+name+"\t"+hight)
def search_in_file():
    print("Mit keressünk? \n\t1 - Legalacsonyabb hegység \n\t2 - Legmagasabb hegység \n\t3 - Hegység neve \n\t4 - Magasság")

def close_file(f):
    f.close()
    filename=""
    return filename
def reading(filename):
    f=open(filename,"r")
    return f
def appending(filename):
    f=open(filename,"a")
    return f
def search_min():
    pass
def search_max():
    pass
def search_name():
    pass
def search_hight():
    pass
