# import formula

# a = 6
# b = 10

# natija = formula.ekuk(a,b)

# print(natija)

# import math 

# print(math.ceil(2.1))

import random as r

# random_son = r.randint(1,10)
# print(random_son)

royhat = ["Boborahim","Diyorbek","Fayozbek"]

# navbatchi = r.choice(royhat)
# result = r.choices(royhat, weights=[10,1,1],k=3)
# print(result)
# print(f"Bugungi navbatchi: {navbatchi}")
# r.shuffle(royhat)
# print(royhat)

# uz_eng_words = {"mashina":"car","muhim":"essential","eshik":"door","qiziqarli":"interesting","qon":"blood","devor":"wall","daftar":"notebook"}

# chance = 3
# score = 0
# print("So'zlarni inglizcha tarjimasini toping!\n")
# questions = list(uz_eng_words.keys())
# r.shuffle(questions)
# questions_count = len(questions)
# index = 0
# while True:

#   if chance==0 or (index == questions_count):
#     if round(score*100/questions_count,2) >= 60:
#       print(f"Tabriklaymiz siz {round(score*100/questions_count,2)}% natija bilan {score}ta so'zni topdingiz.🎉")
#     else:
#       print(f"Afsuski siz {round(score*100/questions_count,2)}% natija bilan {score}ta so'zni topdingiz.😔")
#     break
#   else:
#     answer = input(f"{uz_eng_words[questions[index]]}: ").lower()
#     if uz_eng_words.get(answer) == uz_eng_words[questions[index]]:
#       print(f"To'g'ri ✅ {chance}ta imkoniyatingiz qoldi.")
#       score = score + 1
#     else:
#       chance = chance - 1
#       print(f"Noto'g'ri ❌ {chance}ta imkoniyatingiz qoldi.")
#     index = index + 1

# natija = r.randrange(10,100,12)
# print(list(range(10,100,12)))
# print(natija)

# def addAB(a,b):
#     return a+b

# a= int(input("a="))
# b= int(input("b="))
# print(f"natija{addAB(a,b)}")
