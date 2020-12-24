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
    f.close()

def append_file(filename):
    lista=[]
    inputFile(filename,lista)
    f=open(filename,"a")
    name=input("Kérem egy hegység nevét: ")
    exist=search_name(lista,name,filename)
    if exist:
        name=input("Kérem egy másik hegység nevét: ")
    hight=input("Kérem a legmagasabb csúcs magasságát (m): ")
    f.write(name+"\t"+hight+"\n")
    print(filename+" bővült a következő sorral: "+name+"\t"+hight)
    f.close()

def search_in_file(filename):
    print("\t1 - Legalacsonyabb hegység \n\t2 - Legmagasabb hegység \n\t3 - Hegység neve \n\t4 - Magasság")
    choise=input("Mit keressünk? ")
    lista=[]
    inputFile(filename,lista)
    if choise=="1":
        search_min(lista)
    elif choise=="2":
        search_max(lista)
    elif choise=="3":
        txt="Adja meg a kivánt hegység nevét ékezet nélkül (Pl.: Mount Everest): "
        name=input("\t"+txt)
        search_name(lista,name)
    elif choise=="4":
        search_hight(lista)

def search_min(lista):
    minindex=0
    for i in range(len(lista)):
        if(lista[i][1]<=lista[minindex][1]):
            minindex=i
    print(lista[minindex])

def search_max(lista):
    maxindex=0
    for i in range(len(lista)):
        if(lista[i][1]>=lista[maxindex][1]):
            maxindex=i
    print(lista[maxindex])

def search_name(lista,name,filename):
    for i in range(0,len(lista),1):
        if(name==lista[i][0]):
            exist=True
            print(lista[i])
        else:
            print("Még nincs ilyen nevű hegy rögzítve.")
            exist=False
            append=input("Szeretné hozzáadni? (igen/nem)")
            if append=="igen":
                append_file(filename)
    return exist

def search_hight(lista):
    txt="Adja meg a kívánt magasságot méterben: "
    value=int(input("\t"+txt))
    for i in range(0,len(lista),1):
        if(value==lista[i][1]):
            print(lista[i])
        elif value+[x for x in range(50)]<=lista[i][1]:
            print(lista[i])
        elif value+[x for x in range(50)]>=lista[i][1]:
            print(lista[i])

def inputFile(filename,lista):
    f = open(filename,"r")
    for sor in f:
        sor=sor[:-1].split(";")
        lista.append([str(sor[0]),int(sor[1])])
    f.close()

main()