import random

kocke = [6, 10, 20]
kocke_strani = []
kocke_met = []
    

def strani():
    for x in kocke:
        kocke_strani.append(list(range(1,x+1)))

def met_kocke():
    rezultat_meta = 0
    for seznam_strani in kocke_strani:
        kocke_met.append(random.choice(seznam_strani))
            



def main():
    
    strani()
    met_kocke()
    print(kocke_met)


main()



'''









kocke_strani.append


print("--------------------")
print("NEW DICE THROW")
print("--------------------")
print(f"The D4 landed on {kocka_d4}")
print(f"The D6 landed on {kocka_d6}")
print(f"The D8 landed on {kocka_d8}")
print(f"The D10 landed on {kocka_d10}")
print(f"The D12 landed on {kocka_d12}")
print(f"The D20 landed on {kocka_d20}")
print("--------------------")


'''