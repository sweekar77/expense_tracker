#calc
o = float(input("enter first num"))
p = input(" enter operation")
q = float(input("enter second num"))
if p == "*":
    print(f"{o}{p}{q}=",o*q)
elif p == "/":
    print(f"{o}{p}{q}=",o/q)
elif p =="+":
    print(f"{o}{p}{q}=",o+q)
elif p == "//":
    print(f"{o}{p}{q}=",o//q)
elif p == "%": 
    print(f"{o}{p}{q}=",o*q)
elif p == "-":
    print(f"{o}{p}{q}=",o-q)
else:
    print("invalid operation")

#project:grade calculator
u = str(input("enter your name"))
y = float(input("enter marks of first subject"))
y2 = input("enter name of first subject")
t = float(input("enter marks of second subject"))
t2 = input("enter name of second subject")
r = float(input("enter marks of third subject"))
r2 = input("enter name of third subject")
l = int(input("enter full marks of first subject"))
k = int(input("enter full marks of second subject")) 
j= int(input("enter full marks of third subject"))
total = k+l+j
print("full marks=",total)
marks = y+t+r
average = marks/3
print("average=",average)
if average < 40:
    print("you failed")
else:
    print("you passed")
if average >= 80:
    print("you got an A")
elif average >= 60:
    print("you got a B")
elif average >= 40:
    print("you got an C")
else:
    print("you failed. Better luck next time")
 