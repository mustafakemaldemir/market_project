print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><MKD BAKKAL OTOMASYONU><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n\n\n")

menu_secen = "" ## boş karakter dizisi yaratır ve menü arakarında gezinmek içibn gereken key olcak

d_yiyecekler  = {'kek' : 1 , 'kola' : 3 , 'nestlecikolata' : 1 }

d_kisiler  =  {'helin' : 0 , 'mustafakemal' : 100}

def sozlukte_var_mi(sozluk_ismi, aranan_kelime):  # ürünün daha önce kaydının olup olmadığına bakar.

	return bool(list(sozluk_ismi.keys()).count(aranan_kelime))



while menu_secen != "exit" :

	print("########### BURASI ANA MENÜMÜZ ###########\n\n\n") 

	print ("-->>Ürün ve Fiyatlarını Görmek VEYA Güncellemek İçin 1'i SEÇİNİZ!\n\n\n")

	print ("-->>Müşteri Bilgilerini Görebilmek VEYA Düzenlemek İçin 2'yi SEÇİNİZ!\n\n\n")

	print ("***ATTENTİON*** [Program Notu] :Programdan çıkmak için ana menüde 'exit' yazınız !\n\n\n")
	
	menu_secen=input ("Lütfen seçiminizi yapınız ! \n") 
	
	print("\n########### MENÜ BİTİŞİ ###########\n\n\n")


	"""Ürün ve Fiyatlarını Görme Veya Güncelleme Kısmında Dolanıyor """

	if (menu_secen == "1") : # ilk secimde

		while True :

			print("########### MENÜ BAŞLANGICI ###########\n\n\n") 

			print ("-->>Hangi Ürünlerin Marketinizde olduğunu görmek İçin 1'i SEÇİNİZ : \n\n\n")

			print ("-->>Ürünlerinizi Güncellemek veya Ürün Eklemek İçin 2'yi SEÇİNİZ : \n\n\n")

			print ("-->>Bir üstteki menüye dönmek için 'tamam' yazınız ! \n\n\n")

			menu_secen = input ("-->>Lütfen Seçiminizi Yapınız  : \n")

			print("\n########### MENÜ BİTİŞİ ###########\n\n\n")

			if menu_secen.lower() == "tamam" :

				break

			elif (menu_secen == "1") :

				print ("######################\n\n\n")

				print ("Güncel Ürün Listesi Aşşağıdaki Gibidir\n\n")

				for k,v in d_yiyecekler.items() :

					print (k + "  :  "+str(v))

				print("\n########### MENÜ BİTİŞİ ###########\n\n\n")

			elif (menu_secen == "2") :

				while True:
				
					print("Girisi durdurmak icin 'tamam' yazınız\n\n\n")

					urun_adi = input("->Ürün adı giriniz: ")

					if urun_adi.lower() == "tamam" :

						break

					urun_fiyatı = input("->Ürün fiyatı giriniz: ")

					if urun_fiyatı.lower() =="tamam":

						break

					else:

						if sozlukte_var_mi(d_yiyecekler, urun_adi):#Eğer ürün varsa ürün fiyatı güncellenir

							print("######################\n")				
							
							print("Bu ürün kayıtlıdır fiyatı güncellenecektir\n")
							
							print("######################\n")

						
						if urun_fiyatı.isdecimal(): #Ürün yoksa kataloğa eklenir
								
							d_yiyecekler[urun_adi] = int(urun_fiyatı)

							print ("Güncel Ürün Listesi Aşşağıdaki Gibidir\n")

							for k,v in d_yiyecekler.items() :

								print (k + "  :  "+str(v))

							print ("\n\n")	

						else:

							print("######################")
							
							print("Lütfen ürün fiyatını düzgün giriniz")
							
							print("######################")

	elif (menu_secen == "2") : # kullanıcı bilgileri kısmında seçim yapacak

		while True :

			print ("-->>Müşteri Girişi Yapmak İçin 1'i SEÇİNİZ : \n\n\n")

			print ("-->>Müşteri Borç Listelemek İçin 2'i SEÇİNİZ: \n\n\n")

			print ("-->>Müşteriye Ürün Satışı Yapıp Borç Güncellemek İçin 3'ü SEÇİNİZ: \n\n\n")

			print ("-->>Müşteri Borcu Silmek veya Azaltmak İçin 4 'ü SEÇİNİZ\n\n")

			print ("-->>Bir üstteki menüye dönmek için 'tamam' yazınız ! \n\n\n")

			menu_secen = input ("-->>Lütfen Seçiminizi Yapınız  : \n")

			print("\n########### MENÜ BİTİŞİ ###########\n\n\n")

			if menu_secen.lower() == "tamam" :

				break
			
			elif menu_secen == "1" :

				while True :

					print ("Girişi durdurmak için 'tamam' yazınız'\n")

					musteri_adi = input ("Yeni müşteri adını giriniz\n")

					if musteri_adi.lower() == "tamam" :

						break

					musteri_borc = input ("Yeni müşterinin güncel borcunu giriniz\n")

					if musteri_borc.lower() == "tamam" :

						break

					elif list(d_kisiler.keys()).count(musteri_adi) == 1  :

						print("Bu müşteri zaten kayıtlıdır lütfen yeni bir müşteri ekleyiniz \n")

					elif musteri_borc.isdecimal() :

						d_kisiler[musteri_adi] = musteri_borc

			elif menu_secen == "2" :

				print ("######################\n\n")

				for k,v in d_kisiler.items() :

					print (k + "  :  "+str(v))

					print ("######################")

			elif menu_secen == "3" :

				while True :

					print ("Bir üstteki menüye dönmek için 'tamam' yazınız\n\n")

					musteri_adi = input ("Lütfen ürün satışı yaptığınız müşteri adını giriniz \n\n")

					if musteri_adi.lower() == "tamam" :

						break 

					elif list (d_kisiler.keys()).count(musteri_adi) == 0 :

						print ("######################\n\n")

						print ("Böyle bir müşteri mevcut değildir\n\n")

						print ("######################\n\n") 

					else :

						print ("Bir üstteki menüye dönmek için 'tamam' yazınız \n\n")

						urun_adi = input ("Urun adı giriniz\n\n")

						if (urun_adi.islower()=="tamam") :

							break 

						elif list (d_yiyecekler.keys()).count (urun_adi) == 0 :

							print("#####################\n")

							print("Böyle bir ürünümüz mevcut değildir\n")

							print("#####################\n")

						else :

							print ("Bir üstteki menüye dönmek için 'tamam yazınız' \n\n")

							urun_adedi = input ("Lütfen ürün adedi girini\n\n")

							print("#####################\n")

							if urun_adedi.lower() == "tamam" :

								break

							elif urun_adedi.isdecimal() :

								d_kisiler[musteri_adi] += d_yiyecekler[urun_adi] * int(urun_adedi)

							else :

								print("#####################\n")

								print("Urun adedini yanlış girdiniz\n")
								
								print("#####################\n")

			elif menu_secen == "4" :

				print ("Bir üstteki menüye dönmek için 'tamam' yazınız\n")

				while True :

					musteri_adi = input ("Borcunu Ödemek İsteyen Müşteri adını giriniz\n\n")

					if musteri_adi.lower () == "tamam" :

						break 

					elif list (d_kisiler.keys()).count (musteri_adi) == 0 :

						print("#####################\n")

						print("Böyle bir kişi mevcut değildir\n")

						print("#####################\n")

					else :

						print ("Bir üstteki menüye dönmek için 'tamam' yazınız \n\n")

						odenecek_miktar = input ("Müşterinin ödemek istediği miktarı giriniz \n\n")

						if (odenecek_miktar.lower () == "tamam") :

							break 

						elif odenecek_miktar.isdecimal() :

							if (int (odenecek_miktar) > int (d_kisiler [musteri_adi]) ) :

								print ("Yazılan miktar kişinin borç bilgisinden yüksektir lütfen sınır olarak kişi borcu kadar giriniz\n\n")

							else :

								d_kisiler[musteri_adi] = d_kisiler[musteri_adi] - int (odenecek_miktar)

								print ("Kişinin Güncel Borç Bilgisi : " + str (d_kisiler[musteri_adi])) 

								print ("\n\n######################\n\n")

						else :

							print ("Ödenecek miktar yanlış girilmiştir\n\n")

