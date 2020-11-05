# Exemplu: Date de intrare  -5  -3  1  8  12  17  20  21  18  10  6  -2 
t=0
tl=0
tp=0
tn=0
x=0
z=0
while tl<12:
    t = eval(input("dati temperatura: "))
    if t>=0:
        tp+=t
        x+=1
    else:
        tn+=t
        z+=1
    tl+=1
Medp=tp/x
Medn=tn/z
t1=f"{Medp:.2f}"
t2=f"{Medn:.2f}"
print("Media temperaturii pozitive este",t1,"Grade Celsius")
print("Media temperaturii pozitive este",t2,"Grade Celsius")