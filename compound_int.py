p = float(input("Enter principal value: "))
r = float(input("Enter rate of intrest: "))
t = float(input("Enter time duration: "))


A = p*(1 + r/100)**t
print("The amount of interest is", A)

CI = A - p
print("The compound of interest is", CI)
