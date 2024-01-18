1-topshiriq
#oson
IndexError va KeyError hosil qiladigan kod yozing

2-topshiriq
#oson
TypeError hosil qiladigan kod yozing

3-topshiriq
#qiyin
1- va 2- topshiriqda yozgan kodingizni try/except ichida yozib, ekranga errorni chiqaradigan kod yozing


4-topshiriq
#juda_qiyin
Har 2 soniyada ekranga vaqtni ko'rsatadigan kod yozing.
Ctrl + C bosilganda (kod to'xtatilganda) ekranga "stopped" deb yozib, loopni to'xtating.

Ayni vaqtni o'lish uchun "datetime" kutubxonasidan foydalaning. https://docs.python.org/3/library/datetime.html
https://strftime.org/

Example:
from datetime import datetime
now =  datetime.now()
print(now.strftime("%X"))
