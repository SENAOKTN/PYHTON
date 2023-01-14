#Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı
# sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.
a=input("bir sayı giriniz:")
basamak_sayısı=len(a)
a=int(a)
toplam=0
basamak=0
gecici_sayı=a
while(gecici_sayı>0):
    basamak=gecici_sayı%10
    toplam+=basamak**basamak_sayısı
    gecici_sayı//=10

if(a==toplam):
    print("Girilen sayı bir amstrong sayıdır.")
else:
    print("Girilen sayı bir amstrong sayı değildir.")

