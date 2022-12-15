vize=int(input("vize notunu giriniz:"))
vize2=int(input("vize2 notunu giriniz:"))
final=int(input("final notunu giriniz:"))

not_hesaplaması=(vize*(3/10))+(vize2*(3/10))+(final*(2/5))

if(not_hesaplaması>=90):
    print("harf notunuz AA")
elif(not_hesaplaması>=85):
    print ("harf notunuz BA")
elif (not_hesaplaması >= 80):
    print("harf notunuz BB")
elif (not_hesaplaması >= 75):
    print("harf notunuz CB")
elif (not_hesaplaması >= 70):
    print("harf notunuz CC")
elif (not_hesaplaması >= 65):
    print("harf notunuz DC")
elif (not_hesaplaması >= 60):
    print("harf notunuz DD")
elif(not_hesaplaması>=55):
    print ("harf notunuz FD")
else:
    print("harf notunuz FF")