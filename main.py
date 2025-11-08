#1-misol
for i in range(1, 31):
    if i % 2 != 0:
        continue
    print(i)

#2-misol
sum = 0
for i in range(1, 51):
    sum += i
    if i % 5 == 0:
        continue

print(sum)

#3-misol
for i in range(-10, 11):
    if i < 0:
        continue
    print(i * i)

#4-misol
sum = 0

for i in range(1, 101):
    if i % 3 == 0:
        continue
    sum += 1

print(sum)
