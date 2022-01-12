def look_and_say(number):
    """
    This Function gets a number and convert it to another number as if someone is reading the
    sequence of numbers, for example: number = 23, converted number is gonna be 'one 2 one 3'
    --->1213
    or if the number is 11221, the converted number would be: 'two 1, two 2, one 1' ---> 212211
    """
    i = 0
    resultList = []
    while i < len(number):
        count = 1
        while i + 1 < len(number) and number[i] == number[i + 1]:
            count += 1
            i += 1
        resultList.append(str(count) + number[i])
        i += 1

    return (''.join(resultList))


# now if you want to repeat this conversion multiple times, the program could
# ask the user about number of the repetitions; for example: if seq == 3:
# number = 1 ---> 11 ---> 21 ---> 1211
seq = int(input("How many sequences you want this conversion?\n"))
num = input("Please insert a number\n")
for k in range(seq):
    num = look_and_say(num)
    print(num)
