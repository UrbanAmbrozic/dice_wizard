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
    kocke = [6, 10, 20]
    kocke_strani = strani(kocke)
    kocke_meti = met_kocke(kocke_strani)
    
    for i in range(len(kocke)):
        print(f"Rezultat meta za D{kocke[i]} je {kocke_meti[i]}")


main()