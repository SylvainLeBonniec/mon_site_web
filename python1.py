#sorted
capitales=["Paris","Londres","Pragues","Vienne"]

print("voici quelques capitales : ", capitales)

position=input("entrez un chiffre entre 1 et 4 : ")
classement=int(position) -1
print(capitales[classement])

Autre_capitale=input("entrez une capitale : ")
capitales.append(Autre_capitale)
Autre_capitale=input("entrez une capitale : ")
capitales.append(Autre_capitale)
Autre_capitale=input("entrez une capitale : ")
capitales.append(Autre_capitale)
print("liste capitales Mis à jour : ",capitales)

capitales_triées=sorted(capitales)
print("liste des capitales triées : ", capitales_triées)
print("liste des capitales triées : ",sorted(capitales))
print("liste des capitales triées inversée : ",sorted(capitales,reverse=True))
