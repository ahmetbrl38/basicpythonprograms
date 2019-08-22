from random import randint
print("*" * 30 + "\nSayı Tahmin Etme Oyununa hoşgeldiniz.\n" + "*" * 30)
print("Oyun Kuralları\nProgram tarafından rastgele atanan sayıyı bulmanız gerekmektedir.")
print("1-7 deneme içinde bulduğunuz her sayı için + 50 puan")
print("7-15 deneme içinde bulduğunuz her sayı için + 25 puan")
print("15-25 deneme içinde bulduğunuz her sayı için + 10 puan alırsınız.")
print("25 kezden fazla denedikten sonra sayıyı bulsanız bile puan alamazsınız.\n")
print("Zorluk Seviyesi\n1.Kolay: 1 - 30 arası\n2.Orta: 1-50 arası\n3.Zor: 1-100 arası\n4.İmkansız: 1-200 arası")
sayac = 0
puan = 0

zorluk = int(input())
if(zorluk ==1):
    sayı = randint(1,30)
elif(zorluk ==2):
    sayı = randint(1,50)
elif(zorluk ==3):
    sayı = randint(1,100)
elif(zorluk ==4):
    sayı = randint(1,200)
else:
    print("Lütfen bir dahaki sefere 1,2,3 veya 4 giriniz. Zorluk seviyesi : Orta")
    sayı = randint(1, 50)
while(True):
    num = int(input("Tahmin ettiğiniz sayıyı giriniz : \n"))
    sayac += 1
    if(num < sayı):
        print("Daha yüksek.... : ")
    if(num > sayı):
        print("Daha düşük.... : ")
    if(num == sayı):
        print("Doğru tahmin! Sayı",sayı,"idi.",sayac,". denemede bulmayı başardınız.")
        if(sayac >=1  and sayac <=7):
            print("50 puan kazandınız.")
        if (sayac >= 8 and sayac <= 15):
            print("25 puan kazandınız.")
        if (sayac >= 15 and sayac <= 25):
            print("10 puan kazandınız.")
        if (sayac >=25):
            print("Maalesef tahmin sayısını aştığınız için puan alamadınız.")
        break
