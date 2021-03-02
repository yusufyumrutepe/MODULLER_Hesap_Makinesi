import math
print("***lütfen önce birinc sayıyı spnra ikinci sayıyı ve daha sonra yapmak istediğiniz işlemin numarasını giriniz....")
print("***eğer faktoriyel hesaplaması yapmak istiyorsanız iki sayıyıda aynı girin")
print("***Çıkmak isterseniz isteğiniz işlem yerine q harfine basınız")
print("""        1.toplama
        2.çıkarma
        3.çarpma
        4.bölme
        5.faktoriyel
""")
while True:
    birinci_sayı = int(input("lütfen birinci sayıyı giriniz :"))
    ikinci_sayı = int(input("lütfen ikinci sayıyı giriniz :"))
    istenilen = input("lütfen yapmak istediğiniz sayıyı seçiniz :")
    if(istenilen== "q"):
        print("program sonlandırıldı")
        break
    elif(istenilen == "1"):
        print("işleminizin sonucu {}".format(birinci_sayı+ikinci_sayı))
    elif(istenilen == "2"):
        print("işleminizin sonucu {}".format(birinci_sayı-ikinci_sayı))
    elif(istenilen == "4"):
        print("işleminizin sonucu {}".format(birinci_sayı/ikinci_sayı))
    elif(istenilen == "3"):
        print("işleminizin sonucu {}".format(birinci_sayı*ikinci_sayı))
    else:
        print("işleminizin sonucu {}".format(math.factorial(birinci_sayı)))
#eklemek istediğin işlemi modulden çağır