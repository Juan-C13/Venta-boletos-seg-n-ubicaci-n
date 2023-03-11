boletosG=int(input("Digite la cantidad de boletos en ubicación general:"))
boletosP=int(input("Digite la cantidad de boletos en preferencial:"))
if boletosG+boletosP>5:
    valorUG=8000
    valorP=10000
else:
    valorUG=12000
    valorP=15000
T1=valorUG*boletosG
T2=valorP*boletosP
TP=T1+T2
print("Total a pagar:",TP)
