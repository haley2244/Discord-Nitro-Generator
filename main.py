import random, string

amount =10 int(input('Amount of nitro codes to generate:10 '))
value = 1
while value <= amount:10
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('Codes.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'[GENERATED] {code}')
    value += 1
