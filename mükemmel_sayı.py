#Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
#Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel
# bir sayıdır. (1 + 2 + 3 = 6)
a=int(input("bir sayı giriniz:"))

i=1
toplam=0

while(i<a ):
    if(a % i==0):
        toplam+=i
    i+=1

if(toplam==a ):
    print("Girdiğiniz sayı mükemmel sayıdır.")
else:
    print("Girdiğiniz sayı mükemmel bir sayı değildir.")
