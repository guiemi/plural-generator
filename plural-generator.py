from desacentuador import desacento
palavra = str(input("Digite: \n"))

# Letras que formam substantivos plurais em PB:
a = ["s"]
e = ["s"]
i = ["s"]
m = ["ns"]
n = ["s"]
o = ["s"]
r = ["es"]
s = ["es"]
u = ["s"]
z = ["es"]

''' Casos especiais:
Segundo HUBACK (2017), plurais terminados em "ão" ("avião" / "aviões"), 
em "-l" ("anel" /"anéis") e em ditongo em "u" ("chapéu"/ "chapéus")
constituem um grupo de plurais irregulares em PB.
'''

l = ["es", "is"]
ão = ["ões"]

def plural(palavra):
    # Letra a:
    if palavra[-1] == "a": # Talvez dicionários melhores que listas
        print(f"{palavra}{a[0]}")

    # Letra s:
    if palavra[-1] == "s":
        if palavra[-2] == "í":
            print(f"{palavra}{s[0]}")
        elif palavra[-2] == "ê":
            palavra = desacento(palavra)
            print(f"{palavra}{s[0]}")
        else:
            print(f"{palavra}")

plural(palavra)
desacento(palavra)
acentuadas = ["á", "â", "é", "ê", "í", "ó", "ô", "ú"]
vogais = ["a", "a", "e", "e", "i", "o", "o", "u"]
