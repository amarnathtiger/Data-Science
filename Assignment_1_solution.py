#Question 1
x, y = map(int, input("Enter X,Y: ").split(","))
result = [[i * j for j in range(y)] for i in range(x)]
print(result)

#Question 2
items = input("Enter words: ").split(",")
items.sort()
print(",".join(items))

#Question 3
words = input("Enter words: ").split()
print(" ".join(sorted(set(words))))

#Question 4
res = [str(num) for num in range(1000, 3001) if all(int(d) % 2 == 0 for d in str(num))]
print(",".join(res))

#Question 5
s = input("Enter sentence: ")
letters = sum(c.isalpha() for c in s)
digits = sum(c.isdigit() for c in s)
print("LETTERS", letters)
print("DIGITS", digits)

#Question 6
s = input("Enter sentence: ")
upper = sum(c.isupper() for c in s)
lower = sum(c.islower() for c in s)
print("UPPER CASE", upper)
print("LOWER CASE", lower)

#Question 7
balance = 0
while True:
    try:
        entry = input().split()
        if not entry: break
        type_, val = entry[0], int(entry[1])
        if type_ == 'D':
            balance += val
        elif type_ == 'W':
            balance -= val
    except:
        break
print(balance)

#Question 8
import re
passwords = input("Enter passwords: ").split(",")
valid = []
for pwd in passwords:
    if (6 <= len(pwd) <= 12 and
        re.search("[a-z]", pwd) and
        re.search("[A-Z]", pwd) and
        re.search("[0-9]", pwd) and
        re.search("[$#@]", pwd)):
        valid.append(pwd)
print(",".join(valid))

#Question 9
lines = []
while True:
    try:
        line = input()
        if not line: break
        lines.append(tuple(line.split(",")))
    except:
        break
print(sorted(lines, key=lambda x: (x[0], int(x[1]), int(x[2]))))

#Question 10
import math
x = y = 0
while True:
    try:
        move = input().split()
        if not move: break
        dir_, step = move[0], int(move[1])
        if dir_ == "UP": y += step
        elif dir_ == "DOWN": y -= step
        elif dir_ == "LEFT": x -= step
        elif dir_ == "RIGHT": x += step
    except:
        break
print(round(math.sqrt(x**2 + y**2)))

#Question 11
s = input()
res = ""
count = 1
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        res += s[i-1] + str(count)
        count = 1
res += s[-1] + str(count)
print(res)

#Question 12
s = input()
import re
letters = re.findall("[a-zA-Z]", s)
numbers = re.findall("[0-9]+", s)
for i in range(len(numbers)):
    if sum(map(int, list(numbers[i]))) == 9:
        print(letters[i] + "," + letters[i+1])

#Question 13
s = input()
count_ones = s.count("1")
print(count_ones * (count_ones - 1) // 2)

#Question 14
valid = list(map(int, input("Enter valid currency: ").split(",")))
money = int(input("Enter money: "))
valid.sort(reverse=True)
for v in valid:
    if money >= v:
        cnt = money // v
        money %= v
        print(f"{v}-{cnt}")

#Question 15
import math
n, m = map(int, input().split())
ways = math.comb(n - m + 1, m)
print(ways)

#Question 16
scores = {"A":0, "B":0}
rules = {"Stone":"Scissor", "Scissor":"Paper", "Paper":"Stone"}
while scores["A"]<5 and scores["B"]<5:
    a, b = input("Player A, Player B: ").split()
    if a == b: print("DRAW")
    elif rules[a] == b:
        print("Player A wins")
        scores["A"] += 1
    else:
        print("Player B wins")
        scores["B"] += 1

#Question 17
import re
email = input()
if re.fullmatch("[a-z0-9._]+@[a-z0-9]+\\.[a-z]{2,}", email):
    print("Valid")
else:
    print("Invalid")

#Question 18
# (a)
def pattern_a(n):
    num = 1
    for i in range(1, n+1):
        row = []
        for j in range(i):
            row.append(str(num))
            num += 1
        print(" * ".join(row))


# (b)
def pattern_b(n):
    
    for i in range(1, n+1):
        print(" " * (n - i), end="")
        print(" ".join("*" * i))
    
    for i in range(n-1, 0, -1):
        print(" " * (n - i), end="")
        print(" ".join("*" * i))


# (c)
def pattern_c(n):
    num = 1
    rows = []
    for i in range(1, n+1):
        row = []
        for j in range(i):
            row.append(str(num))
            num += 1
        rows.append(" * ".join(row))
    for r in rows:
        print(r)
    for r in reversed(rows[:-1]):
        print(r)


# (d)
def pattern_d(n):
    for i in range(n):
        if i == 0:
            print(" " + "*"*3)
        elif i < n//2:
            print(" *")
        elif i == n//2:
            print(" *" + "*"*3)
        elif i < n-1:
            print(" *" + " "*(n-2) + "*")
        else:
            print(" " + "*" + " " + "*" + " ")


# (e)
def pattern_e(n):
    for i in range(n):
        row = []
        for j in range(n):
            if i == 0 or i == n-1 or j == n//2:
                row.append("1")
            else:
                row.append("0")
        print(" ".join(row))

#Question 19
t = int(input())
s = input().strip("'")
k = int(input())
for _ in range(k):
    if t == 1:  # left shift
        s = s[1:] + s[0]
    else:       # right shift
        s = s[-1] + s[:-1]
    print(s)

#Question 20
healthy = {"Sugar level":15, "Blood pressure":32, "Heartbeat rate":71, "weight":65, "fat percentage":10}
patient = {}
for key in healthy:
    patient[key] = int(input(f"Enter {key}: "))
diff = {k: patient[k] - healthy[k] for k in healthy}
print(diff)
for k,v in diff.items():
    if v<0: print(f"{k} {abs(v)} less than ideal")
    elif v>0: print(f"{k} {v} more than ideal")
    else: print(f"{k} is ideal")

#Question 21
n = int(input())
s = sum(int(d)**len(str(n)) for d in str(n))
print("Armstrong number" if s == n else "Not Armstrong")

#Question 22
n = int(input())
res = ""
while n > 0:
    res = str(n % 2) + res
    n //= 2
print(res)

#Question 23
n = int(input())
s = sum(i for i in range(1, n) if n % i == 0)
print("Perfect number" if s == n else "Not perfect")
