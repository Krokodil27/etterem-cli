def menu():
    print("\nÉttermi panel")
    print("1 - Új rendelés indítása")
    print("4 - Étlap megtekintése")
    print("5 - operátor jog")

def opmenu(): 
    print("\n operátori panel")

#  ASZTALOK BEOLVASÁSA 
asztalok = []

file = open("asztalok.csv", "r", encoding="utf-8")
elso = True

for sor in file:
    sor = sor.strip()

    if elso:
        elso = False
        continue

    adatok = sor.split(";")

    asztal = int(adatok[0])
    foglalt = int(adatok[1])
    szamla = int(adatok[2])
    rendelesek = adatok[3]

    asztalok.append([asztal, foglalt, szamla, rendelesek])

file.close()


# ASZTAL VÁLASZTÁS 
def asztal_valasztas():
    print("\nAsztalok:")

    for a in asztalok:
        if a[1] == 0:
            print(f"Asztal {a[0]} - szabad")
        else:
            print(f"Asztal {a[0]} - foglalt")

    val = int(input("Melyik asztal? "))

    for a in asztalok:
        if a[0] == val:
            if a[1] == 0:
                a[1] = 1
                return a
            else:
                print("Ez az asztal foglalt!")
                return None

    print("Nincs ilyen asztal!")
    return None


# -
rendelés = 0
aktualis_asztal = None

while True:
    menu()
    valasztas = input("Válassz: ")

   
    if valasztas == "1":
        if rendelés == 0:
            asztal = asztal_valasztas()
            if asztal is not None:
                aktualis_asztal = asztal
                rendelés = 1
                print(f"Rendelés elindítva - Asztal {asztal[0]}")
        else:
            print("Már van aktív rendelés!")

    rendelés = 0
    aktualis_asztal = None
    
    while True:
        menu()
        valasztas = input("Válassz egy menüpontot: ")
    
        if valasztas == "1":
            if rendelés == 0:
                asztal = asztal_valasztas()
                if asztal is not None:
                    aktualis_asztal = asztal
                    print(f"Új rendelés indítása - Asztal {asztal}")
                    rendelés = 1
            else:
                print("Már van folyamatban lévő rendelés")
    
        elif valasztas == "2":
            print("Étel hozzáadása")
    
        elif valasztas == "3":
            if rendelés == 1:
                print("Rendelés lezárása")
                rendelés = 0
    
                for a in asztalok:
                    if a[0] == aktualis_asztal:
                        a[1] = 0
    
            else:
                print("Nincs folyamatban lévő rendelés")
    
        elif valasztas == "4":
            print("Étlap megtekintése")
    
        elif valasztas == "5":
            print("Operátor mód")
    
        elif valasztas == "6":
            print("Étel törlése")
    
        else:
            print("Hibás választás!")
