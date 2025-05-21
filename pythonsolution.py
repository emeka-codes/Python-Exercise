#Solution One
def fizzbuzz(n):
    for number in range(1, (n+1)):
        if number % 2 == 0:
            continue
        elif number % 3 == 0 and number % 5 == 0:
            print('Data2bots')
        elif number % 3 == 0:
            print('Data2')
        elif number % 5 == 0:
            print('Bots')
fizzbuzz(30)


#Solution Two
def conversion(celcius):
    fahrenheit= (celcius * 9/5) + 32
    F= int(fahrenheit)
    print (f'{celcius}°C is = {F}°F')
conversion(40)

#Solution three
#for currentValue in range(6):
with open("book.txt") as f:
    for line in f:
        
        stringedLine= str(line)
        firstLetter= stringedLine[0:1]
        length= len(stringedLine)
        print(f'The code name for {line} is {firstLetter}{length}')





