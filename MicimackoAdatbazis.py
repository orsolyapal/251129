kik=["", "Micimackó", "Malacka", "Füles", "Nyuszi", "Tigris", "Róbert Gida", "Kanga", "Zsebibaba", "Bagoly"]
# fölvettünk elsőnek egy üres stringet, hogy az indexelés megegyezzen az exceles Micimackó nyilvántartással
print(kik[1])
mik=["", "méz", "alma", "dió", "mogyoró", "narancs", "körte", "banán", "meggy", "füge", "datolya", "chiamag"]

omazonosito=71613473575 # hetvenegymilliárd-hatszáztizenhárommillió-... ez egy hetvenegymilliárdos érték

# a programozási nyelvekben megjelenik egy INT típusú előjeles 32 bites számok tárolására alkalmas adattípus
# ez azonban csak -2milliárdtól +2milliárdig tárolja az adatokat. ebben nem lehet az om azonosítót tárolni
# ezért bevezették pl. a LONG adattípust, ami már 64 biten tárolja a számokat.
# pythonban ennél jóval nagyobb számokat tudunk kezelni (kb. a rendelkezésre álló memóriaterület határáig)

import random  # [(3,7),(1,1), (1,2), (1,6), (2,2)] 
ki_mit_szeret=[]

#print(kik.index(random.choice(kik)))
#print(random.choice(mik))


for i in range(7):
    nev=random.choice(kik)
    kulcs1=kik.index(nev)

    megnevezes=random.choice(mik)
    kulcs2=mik.index(megnevezes)
    ki_mit_szeret.append((kulcs1, kulcs2))

print(ki_mit_szeret)

