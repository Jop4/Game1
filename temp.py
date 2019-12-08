import time

print('=' * 10)
i = 0
while i < 10001:
    time.sleep(0.0000000000000000001)
    print(i)
    i += 1
    continue
    if i > 5:
        break
print('=' * 10)
for j in range(2, 10, 3):
    time.sleep(0.02)
    print(j)
    continue
    if j > 5:
        break

print('=' * 10)
for s in 1, 2, 3:
    print(s)

print('=' * 10)
if i == 9:
    print('да i это 9')
elif i == 10:
    print('да i это 10')
elif i != 9:
    print('что напечатается?')
else:
    print('да i не это 9')
print('=' * 10)
print('ты заешь каков удел слабых')
time.sleep(2)
print('==========')
print('у них свой путь')
time.sleep(1)
print('==========')
print('скоро ты это поймешь')
