import statistics
print("---Calcular la suma y el promedio de 10 numeros dados---")
x = 10
listnum = []
for i in range(x):
    listnum.append(int(input("Deme un numero: ")))

print(f"La suma de los numeros dados {listnum} es: {sum(listnum)}")
print(f"El promedio de los numeros dados {listnum} es: {statistics.mean(listnum)}")