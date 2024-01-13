#pythondagi wikipedia moduli
import wikipedia 



def wiki_malumot(malumot):
  # wikipedia tilini sozlash
  wikipedia.set_lang("uz")
  
  try:
    # Wikipediadan ma'lumotni olish
    result = wikipedia.summary(malumot)
  except:
    #malumot topilmagan holat uchun
    result = "Topilmadi!😔"

  #ma'lumotni chop e'tish
  return result
