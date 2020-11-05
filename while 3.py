#Exemplu: Date de intrare  7  4   6   2   1   9   Date de ieşire 12
n=eval(input("Dati numarul:"))
s=0
while (n%2==0)or(n%3!=0):
    n=eval(input("Dati numarul:"))
    if n%2==0:
        s+=n
print(s)