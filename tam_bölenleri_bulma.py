def tambolenleribulma(sayı):
    tam_bolenler= []

    for i in range (2,sayı):

        if(sayı % i == 0):
            tam_bolenler.append(i)
    return tam_bolenler

while True:
    sayı= input("Sayı:")

    if (sayı=="q"):
        print("program sonlandırılıyor")
        break
    else:
        sayı=int(sayı)

        print("tam bölenler:", tambolenleribulma(sayı))

