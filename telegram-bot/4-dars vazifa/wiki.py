#pythondagi wikipedia moduli
import wikipedia 
 
# wikipedia tilini sozlash
wikipedia.set_lang("uz")
 
try:
  # Wikipediadan ma'lumotni olish
  result = wikipedia.summary("Alisher Navoiy")
except:
  #malumot topilmagan holat uchun
  result = "Topilmadi!😔"

#ma'lumotni chop e'tish
print(result)