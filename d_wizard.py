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
    vnos_uporabnika = input("Opiši mi, koliko strani imajo tvoje kocke, in pričaral ti bom naključen met teh kock (Primer: Vnesi '4' za kocko D4. Vnesi več števil za več kock): ")
    kocke = [int(x) for x in vnos_uporabnika.split()]
    kocke_strani = strani(kocke)
    kocke_meti = met_kocke(kocke_strani)
    
    for i in range(len(kocke)):
        print(f"Rezultat meta s kocko D{kocke[i]} je {kocke_meti[i]}")

# Zagon glavne funkcije
main()