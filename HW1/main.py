# H1-1
# read input, reverse capitalize (a -> A, A -> a) and print
print(input().swapcase())

# H1-2
# read m, n, calcluate sum of odd even numbers and print
m, n = map(int, input().split())
print(sum(i for i in range(m, n + 1) if i % 2 == 1))


# H1-3
# read n, find the nearest prime number and print.
# if two primes are equidistant, print the smaller one.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
for i in range(n):
    a = int(input())
    next_move = 1
    while True:
        if is_prime(a - next_move):
            print(a - next_move)
            break
        if is_prime(a + next_move):
            print(a + next_move)
            break
        next_move += 1

# H1-4
# read n, and read n students & their grades, format: name, gradeA, gradeB.
# sort by gradeA desc, gradeB desc, name asc and print name gradeA gradeB
n = int(input())
students = [input().split() for _ in range(n)]
students.sort(key=lambda x: (-int(x[1]), -int(x[2]), x[0]))
for student in students:
    print(student[0], student[1], student[2])

# H1-5
# read N M, there's M companies producing the same product, but at different prices.
# read M prices and the max amount they can produce per cycle, calculate the min money to buy N products.
n, m = map(int, input().split())
prices = [list(map(int, input().split())) for _ in range(m)]
prices.sort(key=lambda x: x[0])
money = 0
for price, amount in prices:
    if n > amount:
        money += price * amount
        n -= amount
    else:
        money += price * n
        break
print(money)

# H1-6
# read n and n numbers, for each number, split them into digits and calculate the amount of digit that could divide the number.
n = int(input())
for i in range(n):
    num = input()
    print(sum(1 for digit in num if digit != '0' and int(num) % int(digit) == 0))


# H1-7
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

def F(n):
    if n == 0:
        return 7
    if n == 1:
        return 11
    return F(n - 1) + F(n - 2)

while True:
    tmp = input()
    if tmp == "":
        break
    n = int(tmp)
    print("yes" if F(n) % 3 == 0 else "no")

# H1-8
# regex that match: <a href="/<number>.mp3" singer="<singer>"><song></a>
# read lines till \n, for each line, if match, add singer and song to a list of tuple, print
import re
songs = []
while True:
    line = input()
    if line == "":
        break
    match = re.search(r'<a href="/(\d+).mp3" singer="(.+?)">(.+?)</a>', line)
    if match:
        songs.append((match.group(2), match.group(3)))

print(songs)

# H1-9
# input like H1-8, this time find all http(s) links and print
import re
links = []
while True:
    line = input()
    if line == "":
        break
    match = re.findall(r'https?://[^"]*', line)
    if match:
        links.extend(match)

print(links)

#request https://iplogger.com/2K6tN4
import urllib

url = "https://iplogger.com/2K6tN4"
response = urllib.request.urlopen(url)
print(response.read().decode("utf-8"))