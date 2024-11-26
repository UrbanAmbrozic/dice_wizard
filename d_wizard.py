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
    
    #'While-loop' za osnovno preverjanje ustreznosti vnosa
    while True:
        uporabnik_vnos = input("Opiši mi, koliko strani imajo tvoje kocke, in pričaral ti bom naključen met teh kock (Primer: Vnesi '4' za kocko D4. Vnesi več števil za več kock): ")
        try:
            kocke = [int(x) for x in uporabnik_vnos.split()] # Before-change: Kocke so bile vnešene ročno, kot seznam (npr. [4, 6, 20])
            # Zajem vnosa negativnih števil (in ničle) za vse elemente v 'kocke'
            if all(x > 0 for x in kocke):
                break
            else:
                print('Tvoj vnos je napačen. Prosim, drži se navodil: sprejemam samo pozitivna števila ločena s presledkom.')
        except ValueError:
            print("Vnašaj samo številke, ločene s presledki....prosim. Torej: ")

    kocke_strani = strani(kocke)

    # Dodajanje 'while-loop'-a, ki bo preko definiranih funkcij izrazil rezultat meta
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
            
            # Uporabnikov odgovor preverjamo po skupini 'negativno' in 'pozitivno'. Če ga ne najdemo, se loop ponovi
            response_neg = ['ne', 'no', 'n', 'nej', 'nje', 'nopanjeno']
            response_pos = ['da', 'yes', 'y', 'd', 'ye', 'dej', 'vrži']

            if uporabnik_odgovor in response_neg:
                print("Veliko sreče! Vedno sem ti na voljo, ko ti zmanjka naključnosti.")
                exit()  # Negativen odgovor = končanje programa
            
            elif uporabnik_odgovor in response_pos:
                print("Ponavljam met:")
                break  # Pozitiven odgovor = izhod iz notranjega 'while-loop'-a, ki vodi v zunanji 'while-loop' - ponoven met 

            else:
                print("Nisem te razumel. Prosim odgovori z da ali ne.")


# Zagon glavne funkcije
if __name__ == "__main__":
    main()