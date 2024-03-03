import sys
print("Hoşgeldiniz bu program şifre kırıcı konusunda size yardımcı olabilir kötü kullanımında ben sorumlu değilim")
ad = input("adınızı giriniz:")
soyad = input("Soyadınızı giriniz:")
doğum_yılı = input("doğum yılınız:")
tel_no_2_harfi = input("telefon numaranızın son 2 hanesi:")
ensonşifre = input("hesabınızda en son hatırladığınız şifre:")
yaş = input("yaşınız:")

devam = input("işleme devam etmek istiyormusunuz evet/hayır")
if devam == "evet":
    print("devam ediliyor...")
else:
    print("hoşçakalın")
    sys.exit()

print("şifreler oluşturuluyor...")

print("""
##############################################################
1.deneme şifreleriniz hepsini deneyin veya 2.denemeyi bekleyin
TUTMA İHTİMALİ:%86
##############################################################
""")
print("123456",ad)
print(ad,"123456",ad)
print("admin",soyad)
print(soyad,"admin",soyad)
print("1235665656565")
print(doğum_yılı,ad,doğum_yılı)
print(soyad,doğum_yılı)
print(ad,doğum_yılı)
print(ad,"turktelekom",doğum_yılı)
print("123456")

print("""
###########################################################
2.deneme şifreleriniz hepsini deneyin veya 3.denemeye bakın
TUTMA İHTİMALİ:%71
###########################################################
""")
print(tel_no_2_harfi,ad,"1234")
print(tel_no_2_harfi,ad,tel_no_2_harfi)
print(ad,soyad,doğum_yılı)
print(doğum_yılı,soyad)
print(doğum_yılı)
print(doğum_yılı,"9939")
print("123456789987654321")
print(ensonşifre,"123456789")
print(yaş,"9939")
print(ensonşifre)

print("""
#############################################
3.deneme(son) şifreleriniz hepsini deneyin
TUTMA İHTİMALİ:%21
#############################################
""")
print("123456")
print("123456789")
print("12345")
print("superonline")
print("abc")
print("abcd")
print("asdasd")
print("asdasdasdasd")
print("asdasdasdasdasdasdasdasd")
print("123com")








