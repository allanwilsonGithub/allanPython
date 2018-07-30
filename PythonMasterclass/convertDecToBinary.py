number = input("Number: ")
if 0 <= int(number) <= 65535:
     print("Number is ok. Proceeding...")
else:
     print("Invalid number")

binary_number = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]

number = int(number)
count = 0

multiples_of_2 = []
for i in range(15,-1,-1):
    print(i)
    multiples_of_2.append(2**i)
print(multiples_of_2)

for item in multiples_of_2:
    if number >= item:
        binary_number[count] = 1
        number -= item
    count += 1

flag = 0
answer = ""
for i in binary_number:
    if i == 1:
        flag = 1
    if flag:
        answer += str(i)
print(answer)
