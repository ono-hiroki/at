# x = int(input())
x = 200
h = 21 if x < 60 else 22;
m = x % 60
print('{}:{:02}'.format(h, m))