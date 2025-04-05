print(range(1, 11)) # range(1, 11)

for number in range(1, 11):
    print(number) # 1 to 10
    
for number in range(1, 11, 3):
    print(number) # 1, 4, 7, 10
    
# gauss challenge
total = 0
for number in range(1, 101):
    total += number
print(total) # 5050