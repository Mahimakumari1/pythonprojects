s1 = int(input("Enter the marks in first sub: "))
s2 = int(input("Enter the marks in first sub: "))
s3 = int(input("Enter the marks in first sub: "))

if(s1<33 or 2<33 or s3<33):
    print("You are fail")
elif(s1+s2+s3)/3 < 40:
    print("You are fail")
else:
    print("Congatulations! You are pass in the exam")