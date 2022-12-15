boy=float(input("boyunuzu giriniz:"))
kilo=int(input("kilonuzu giriniz:"))

bki=kilo/boy**2

if (bki<18.5):
    print("ZAYIF")

elif (18.5<=bki and bki<25):
    print("NORMAL KILOLU")

elif(25<=bki and bki<30):
    print("FAZLA KILOLU")

else:
    print("OBEZ")
