a = [1, 2, 3]
b = a
c = b
b[1] = 5
print(a, b, c)
print(b)
print(b[0])
print(b[1])
print(b[2])
b[1]=100
print(a, b, c)
a[2]=27
print(a, b, c)
c="006"
print(a, b, c)
b[2]="Apartment"
print(a, b, c)
# why?
