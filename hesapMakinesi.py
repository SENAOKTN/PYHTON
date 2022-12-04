

print("""**********************
HESAP MAKINESI PROGRAMINA HOŞGELDİNİZ

YAPILACAK İSLEMLER:

1.TOPLAMA ISLEMI

2.ÇIKARMA

3.ÇARPMA

4.BÖLME


******************************""")

a=int(input("birinci sayıyı giriniz:"))
b=int(input("ikinci sayıyı giriniz"))

işlem=int(input("işlem numarasını giriniz:"))

if(işlem==1):
    print("{} ile {} toplamı {} dir." .format (a,b,a+b))

elif(işlem==2):
    print("{} ile {} farkı {} dir." .format (a,b,a-b))

elif(işlem==3):
    print("{} ile {} çarpımı {} dir." .format (a,b,a*b))

elif(işlem==4):
    print("{} ile {} bölümü {} dir." .format (a,b,a/b))

else:
    print("lütfen geçerli bir işlem giriniz")