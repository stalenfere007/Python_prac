a = float(input("enter first side: "))
b = float(input("enter second side: "))
c = float(input("enter third side: "))

s = (a+b+c)/2
area = (s*((s-a)*(s-b)*(s-c)))**0.5
print("The area of the triangle is", area)
