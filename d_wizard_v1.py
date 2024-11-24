import random

def strani(kocke):
    kocke_strani = []
    for x in kocke:
        kocke_strani.append(list(range(1, x + 1)))
    return kocke_strani

def met_kocke(kocke_strani):
    kocke_meti = []
    for seznam_strani in kocke_strani:
        kocke_meti.append(random.choice(seznam_strani))
    return kocke_meti

def main():
    while True:
        uporabnik_vnos = input("Opiši mi, koliko strani imajo tvoje kocke, in pričaral ti bom naključen met teh kock (Primer: Vnesi '4' za kocko D4. Vnesi več števil za več kock): ")
        try:
            kocke = [int(x) for x in uporabnik_vnos.split()]
            break
        except ValueError:
            print("Vnašaj samo številke, ločene s presledki....prosim. Torej: ")

    kocke_strani = strani(kocke)

    while True:
        kocke_meti = met_kocke(kocke_strani)
        
        print("---------------------------------------")
        print("---------------- MEČEM ----------------")

        for i in range(len(kocke)):
            print("---------------------------------------")
            print(f"Rezultat meta s kocko > D{kocke[i]} < je", "[", f"{kocke_meti[i]}", "]")
        
        print("---------------------------------------")     

        while True:
            response_neg = ['ne', 'no', 'n', 'nej', 'nje', 'nopanjeno']
            response_pos = ['da', 'yes', 'y', 'd', 'ye', 'dej', 'vrži']

            uporabnik_odgovor = input("Ali želiš, da ponovim met? (da/ne): ").strip().lower()

            if uporabnik_odgovor in response_neg:
                print("Veliko sreče! Vedno sem ti na voljo, ko ti zmanjka naključnosti.")
                exit() 
            elif uporabnik_odgovor in response_pos:
                print("Ponavljam met:")
                break
            else:
                print("Nisem te razumel. Prosim odgovori z da ali ne.")

if __name__ == "__main__":
    main()