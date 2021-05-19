lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3,
-52]

#print the max number
print("biggest munber: ", max(lista))

#print the min number
print("smallest number: ", min(lista))

#even number
for number in lista:
    if number % 2 == 0 and number > 0:
        print(number)

# number of occurrences
for rnumber in lista:
    count =0
    if rnumber == lista[0]:
        count += 1
        print("occurrences of first number: {}".format(count))

#average
for anumber in lista:
    average = 0
    average = sum(lista)/len(lista)
print("average: {}".format(average))
