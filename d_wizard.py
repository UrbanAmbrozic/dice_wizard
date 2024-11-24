# Import modula 'random' za možnost vključevanja faktorja "naključnosti"
import random

# Funkcija za generiranje vseh vrednosti, ki jih najdemo na n-kocki.
# Funkcija sprejme vrednost s seznama 'kocke' ( main() ) in za vsako kocko vrne seznam z njenimi vrednostmi 
def strani(kocke):
    kocke_strani = []
    for x in kocke:
        kocke_strani.append(list(range(1, x + 1)))
    return kocke_strani

# Funkcija prejme seznam z vsemi vrednostmi vseh kock (seznam seznamov).
# Funkcija lista po posameznem seznamu iz prejete zaloge in najključno izbere eno izmed vrednosti s seznam, ki ga lista.
def met_kocke(kocke_strani):
    kocke_meti = []
    for seznam_strani in kocke_strani:
        kocke_meti.append(random.choice(seznam_strani))
    return kocke_meti

# Definirana glavna funkcija, ki prejme seznam željenih kock preko vnosa uporabnika, in preko definiranih funkcij vrne generiran naključni met za vse vnešene kocke.
def main():
    uporabnik_vnos = input("Opiši mi, koliko strani imajo tvoje kocke, in pričaral ti bom naključen met teh kock (Primer: Vnesi '4' za kocko D4. Vnesi več števil za več kock): ")
    kocke = [int(x) for x in uporabnik_vnos.split()]

    kocke_strani = strani(kocke)

    # Dodajanje (indentiranega) 'while-loop'-a, ki bo spraševal po novem metu z obstoječimi kockami
    while True:
        kocke_meti = met_kocke(kocke_strani)
        
        print("---------------------------------------")
        print("---------------- MEČEM ----------------")

        for i in range(len(kocke)):
            print("---------------------------------------")
            print(f"Rezultat meta s kocko > D{kocke[i]} < je", "[", f"{kocke_meti[i]}", "]")
        
        print("---------------------------------------")     

        # Nov indentiran 'while-loop', ki preverja uporabnikovo željo po ponovnem metu
        while True:
            uporabnik_odgovor = input("Ali želiš, da ponovim met? (da/ne): ").strip().lower()
            
            response_neg = ['ne', 'no', 'n', 'nej', 'nje', 'nopanjeno']
            response_pos = ['da', 'yes', 'y', 'ye', 'dej', 'vrži']

            if uporabnik_odgovor in response_neg:
                print("Veliko sreče! Vedno sem ti na voljo, ko ti zmanjka naključnosti.")
                exit()  # Končanje programa
            
            elif uporabnik_odgovor in response_pos:
                print("Ponavljam met:")
                break  # Izhod iz notranjega 'while-loop'-a, ki vodi v tunanji 'while-loop' - ponoven met 

            else:
                print("Nisem te razumel. Prosim odgovori z da ali ne.")














        '''reroll_poziv = input("Ali želiš, da ponovim met? (da/ne): ").strip().lower()

        response_neg = ['ne', 'no', 'n', 'nej', 'nje', 'nopanjeno']
        response_pos = ['da', 'yes', 'y', 'ye', 'dej', 'vrži']

        if reroll_poziv in response_neg:
            print("Veliko sreče! Vedno sem ti na voljo, ko ti zmanjka naključnosti.")
            break
        elif reroll_poziv in response_pos:
            print("Ponavljam met:")
            continue
        else:
            print("Nisem razumel. Prosim odgovori z da/ne, če ponovim met z obstoječimi kockami.")
            continue'''
            


# Zagon glavne funkcije
if __name__ == "__main__":
    main()