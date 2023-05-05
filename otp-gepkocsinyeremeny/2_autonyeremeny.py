with open("autonyeremeny.txt") as file:
    szamaink = []
    for sor in file:
        szam=sor.strip().split()
        szam = "".join(szam)
        if szam != "":
            szamaink.append(szam)
##print(szamaink)

with open("uj_szamok_old.txt") as uj:
    uj_szamok=[]
    for sor in uj:
        szam = sor.strip().split()
        szam = "".join(szam)
        uj_szamok.append(szam)
##print(uj_szamok)

szamok_2020 = []
with open("uj_szamok_new.txt") as new:
    for sor in new:
        szam = sor.strip().split()
        szam = "".join(szam)
        szamok_2020.append(szam)

##print(szamok_2020)


nyertunk = 0
for i in uj_szamok:
    if i in szamaink:
        nyertunk += 1

for i in szamok_2020:
    if i in szamaink:
        nyertunk += 1

if nyertunk == 0:
    print("Sajnos nem nyertünk... :(")
else:
    print(f"{nyertunk} gépkocsit nyertünk!!! :D")
