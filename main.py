import math
malas_gr=float(input("Ievadi kvadrāta malas garumu lielāku par 5 centimetriem: "))
laukums=math.pow(malas_gr, 2)
uzaugsu_laukums=math.pow((malas_gr+5), 2)
procenti_uzaugsu=((uzaugsu_laukums-laukums)/laukums)*100
print(procenti_uzaugsu)
