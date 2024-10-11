a = input()

print('\"'+a+'\"')


print('\"'.join(input().split()).replace('\"', '\'', 1))

if (4) > 3:

    print(True)

m,n = map(int, input().split())
y = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if n not in y and n != 1:
    print(f'{m:02}.{n-1:02} {m:02}.{n+1:02} ')
elif n in y:
    print(f'{m:02}.{n-1:02} {m+1:02}.{1:02} ')
elif n == 1:
    print(f'{m-1:02}.{31:02} {m:02}.{1+1:02} ')

d1, d2 = float(input()), float(input())

d = d1 if d1 > d2 else d2

print(d)