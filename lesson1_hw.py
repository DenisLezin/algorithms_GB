
num = input('Input the number: ')
num_sum = 0
num_mult = 1

for i in range(len(num)):
    num_sum += (int(num) // (1 * (10 ** i)) % 10)
    num_mult *= (int(num) // (1 * (10 ** i)) % 10)

print(num_sum)
print(num_mult)