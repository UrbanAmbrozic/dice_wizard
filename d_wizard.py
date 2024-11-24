import random

kocka_d4 = random.randint(1, 4)
kocka_d6 = random.randint(1, 6)
kocka_d8 = random.randint(1, 8)
kocka_d10 = random.randint(1, 10)
kocka_d12 = random.randint(1, 8)
kocka_d20 = random.randint(1, 8)

print("------------------")
print("NEW DICE THROW")
print("------------------")
print(f"The D4 landed on {kocka_d4}")
print(f"The D6 landed on {kocka_d6}")
print(f"The D8 landed on {kocka_d8}")
print(f"The D10 landed on {kocka_d10}")
print(f"The D12 landed on {kocka_d12}")
print(f"The D20 landed on {kocka_d20}")
print("------------------")
