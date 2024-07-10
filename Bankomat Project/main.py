from random import *
import requests
url = 'http://api.exchangeratesapi.io/v1/latest?access_key=2e9fd14872e68750f79aac70efb70d2c'

A = 0
B = 0
CARD_NUMBER = 0
CARD_PASS = 0
MONEY = 0       
PHONE_NUM = 0
account = []

print(f"""
            Tilni Tanlang:
    [1] - O'zbek tili 
    [2] - Rus tili
    [3] - Ingliz tili
""")
LANGUAGE = int(input("Tanlang: "))


# --------------------- UZBEK TILI -----------------------------


if LANGUAGE == 1:
        print("""
                Bizning platformaga
                 Xush kelibsiz!""")
        account_create = int(input("""
                Account yaratamiz!
            [1] - Ha        [2] - Yo'q
    """))
        if account_create == 1:
            phone = int(input("""
                Telefon raqamingizni kiriting:
            +998"""))
            PHONE_NUM += phone          
            name = input("""
                Ismingizni kiriting: 
    """).capitalize()
            
            account.append(name)
            surname = input("""
                Familyangizni kiriting: 
    """).capitalize()
            
            account.append(surname)
            age = int(input("""
                Yoshingizni kiriting: 
    """))
            account.append(age)
            if account[2]>=16:
                A += 1
                yes = int(input("""
                        Kartangiz bormi?
                    [1] - Ha         [2] - Yo'q
                """))  
                if yes == 2:
                    card = randint(1000000000000000, 9999999999999999)
                    print(f"""
                    Sizning yangi karta raqamingiz: {card}""")
                    card_p = randint(1000, 9999)
                    CARD_NUMBER += card
                    CARD_PASS += card_p
                    print(f"Sizning karta parolingiz: {CARD_PASS}\nParolni unutmang!")
            else:
                print("Siz hali balog'at yoshiga to'lmagansiz!")
                A += 0
        elif account_create == 2:
            print("Account yaratmasdan ishlata olmaysiz!")
            A += 0
while A:
        print("""
                    Bizning platformaga
                      Xush kelibsiz!
        """)
        card_num = int(input("""
                Karta raqamingizni kiriting: 
        """))
        card_pass = int(input("""
                Karta parolingizni kiriting: 
        """))
        if CARD_NUMBER==card_num and CARD_PASS==card_pass:
                print(f"Assalomu aleykum {account[0]} {account[1]}!")
                print("""
                [1] - Karta parolini o'zgartirish\t[3] - Valyuta kalkulyatori
                [2] - Mablag'ni tekshirish       \t[4] - To'lov qilish
                [5] - Operatsiyani yakunlash  
            """) 
                tanlangan_variant = int(input("Tanlang: ")) 
                if tanlangan_variant==1:
                    new_pass = int(input('Yangi parol kiriting: '))
                    re_enter_pass = int(input("Qayta kiriting: "))
                    if new_pass==re_enter_pass:
                        print('Parol muvaffaqiyatli o\'zgartirildi')
                        CARD_PASS=new_pass
                        print(CARD_PASS)
                    else:
                        print("Parol xato! Qayta kiriting!")
                elif tanlangan_variant==2:
                    print(f"Sizning mablag'ingiz {MONEY}") 
                    print(f"""
                    [1] - Mablag' yechish\t[2] - Mablag'ni to'ldirish
            """)
                    variant = int(input("Tanlang: "))
                    if variant ==1:
                        money1 = int(input("Mablag'ni kiriting: "))
                        MONEY -= money1
                        if money1<= MONEY:
                            print(f"Mablag' yechildi! Sizning hisobingizda {MONEY} qoldi!")
                        else:
                            print("Sizning mablag'ingiz yetarli emas!")
                    elif variant == 2:
                        sum = int(input("Summa kiriting: "))
                        MONEY += sum
                        print("To'lov muvaffaqiyatli amalga oshirildi!")
                elif tanlangan_variant==3:  
                    def currency_conversion():
                        from_currency = input("Qaysi valyutani ayirboshlamoqchisiz: ")
                        to_currency = input("Qaysi valyutaga: ")
                        amount = int(input("Summa: "))
                        response = requests.get(url)
                        rate = response.json()['rates'][from_currency]
                        amount_in_USD = amount/rate
                        amount = amount_in_USD*(response.json()['rates'][to_currency])
                        amount = int(round(amount,2))
                        print(amount)

                    currency_conversion()
                elif tanlangan_variant==4:
                    print(f"""
                    [1] - Mobil operatorlar uchun to'lov
                    [2] - Komunal to'lovlar
            """)
                    tolov = int(input("Tanlang: "))
                    if tolov == 1:
                        nomer = int(input("Nomeringizni kiriting: +998"))
                        nomer_tolov = int(input("Summa kiriting: "))
                        MONEY -= nomer_tolov
                        if nomer_tolov<=MONEY:
                            print("Sizning to'lovingiz muvaffaqiyatli bajarildi!")
                        else:
                            print("Sizning mablag'ingiz yetarli emas!")
                    elif tolov == 2:
                        print(f"""
                        [1] - Elektr quvvati   \t[4] - Internet 
                        [2] - Issiq suv        \t[5] - Uy va maktab
                        [3] - Gaz              \t[6] - Axlat chiqindilar
            """)
                        kom_tanglang = int(input("Tanlang: "))
                        kom_tolov = int(input("Summani kiriting: "))
                        MONEY -= kom_tolov
                        if kom_tolov<=MONEY:
                            print("Sizning to'lovingiz muvaffaqiyatli bajarildi!")
                        else:
                            print("Sizning mablag'ingiz yetarli emas!")
                    elif tanlangan_variant==5:
                        print("Operatsiya yakunlandi!")
                        break
                    else:
                        print("Bunday tanlov yo'q")
                elif tanlangan_variant==5:
                    A == 0
                    break
                    
        else:
            print("Karta raqami yoki parol xato!")


# -------------- RUS TILI ---------------------


if LANGUAGE == 2:
        print("""
                Добро пожаловать на платформу PDPAY""")
        account_create = int(input("""
                Давайте создадим аккаунт!
            [1] - Да        [2] - Нет
    """))
        if account_create == 1:
            phone = int(input("""
                Введите свой номер телефона:
            +998"""))
            PHONE_NUM += phone          
            name = input("""
                Введите ваше имя:
    """).capitalize()
            
            account.append(name)
            surname = input("""
                Введите фамилию:
    """).capitalize()
            
            account.append(surname)
            age = int(input("""
                Введите свой возраст:
    """))
            account.append(age)
            if account[2]>=16:
                B += 1
                yes = int(input("""
                        У вас есть карта?
                    [1] - Да         [2] - Нет
                """))  
                if yes == 2:
                    card = randint(1000000000000000, 9999999999999999)
                    print(f"""
                    Ваш новый номер карты:{card}""")
                    card_p = randint(1000, 9999)
                    CARD_NUMBER += card
                    CARD_PASS += card_p
                    print(f"Пароль вашей карты: {CARD_PASS}\nНе забудьте пароль!")
            else:
                print("Извините наш платформа только ")
                B += 0
        elif account_create == 2:
            print("Вы не сможете использовать PDPAY без создания учетной записи!")
            B += 0
while B:
        print("""
                    Добро пожаловать!
              
            """)
        card_num = int(input("""
                Введите номер вашей карты:
        """))
        card_pass = int(input("""
                Введите пароль вашей карты: 
        """))
        if CARD_NUMBER==card_num and CARD_PASS==card_pass:
                print(f"Привет {account[0]} {account[1]}!")
                print("""
                [1] - Сменить пароль карты\t[3] - Калькулятор валют
                [2] - Баланс              \t[4] - Оплата
                [5] - Завершить операцию  
            """) 
                tanlangan_variant = int(input("Выбирайте:")) 
                if tanlangan_variant==1:
                    new_pass = int(input('Введите новый пароль: '))
                    re_enter_pass = int(input("Повторно введите: "))
                    if new_pass==re_enter_pass:
                        print('Пароль успешно изменен')
                        CARD_PASS=new_pass
                        print(CARD_PASS)
                    else:
                        print("Ошибка пароля! Введите еще раз!")
                elif tanlangan_variant==2:
                    print(f"Ваши средства {MONEY}") 
                    print(f"""
                    [1] - Снятие\t[2] - Пополнить баланс
            """)
                    variant = int(input("Выбирайте:: "))
                    if variant ==1:
                        money1 = int(input("Введите сумму: "))
                        MONEY -= money1
                        if money1<= MONEY:
                            print(f"Сумма снята! На вашем счету осталось {MONEY}!")
                        else:
                            print("У вас недостаточно средств!")
                    elif variant == 2:
                        sum = int(input("Введите сумму: "))
                        MONEY += sum
                        print("Оплата прошла успешно!")
                elif tanlangan_variant==3:  
                    def currency_conversion():
                        from_currency = input("Какую валюту вы хотите обменять: ")
                        to_currency = input("На какую валюту: ")
                        amount = int(input("Введите сумму:: "))
                        response = requests.get(url)
                        rate = response.json()['rates'][from_currency]
                        amount_in_USD = amount/rate
                        amount = amount_in_USD*(response.json()['rates'][to_currency])
                        amount = int(round(amount,2))
                        print(amount)

                    currency_conversion()
                elif tanlangan_variant==4:
                    print(f"""
                    [1] - Оплата для мобильных операторов
                    [2] - Оплата за коммунальные услуги
            """)
                    tolov = int(input("Выбирайте: "))
                    if tolov == 1:
                        nomer = int(input("Введите свой номер: +998"))
                        nomer_tolov = int(input("Введите сумму:: "))
                        MONEY -= nomer_tolov
                        if nomer_tolov<=MONEY:
                            print("Ваш платеж успешно обработан!")
                        else:
                            print("У вас недостаточно средств!")
                    elif tolov == 2:
                        print(f"""
                        [1] - Электроэнергия   \t[4] - Интернет
                        [2] - Горячая вода     \t[5] - Дом и школа
                        [3] - Газ              \t[6] - Мусора и отходы
            """)
                        kom_tanglang = int(input("Выбирайте:: "))
                        kom_tolov = int(input("Введите сумму:: "))
                        MONEY -= kom_tolov
                        if kom_tolov<=MONEY:
                            print("Ваш платеж успешно обработан!")
                        else:
                            print("У вас недостаточно средств!")
                    elif tanlangan_variant==5:
                        print("У вас недостаточно средств!")
                        break
                    else:
                        print("Нет такого выбора")
                elif tanlangan_variant==5:
                    B == 0
                    break    
        else:
            print("Номер карты или пароль неправильный!")

# ---------------------------------- INGLIZ TILI -------------------------

if LANGUAGE == 3:
        print("""
                Welcome to PDPAY!""")
        account_create = int(input("""
                Let's create an account!
            [1] - Yes        [2] - No
    """))
        if account_create == 1:
            phone = int(input("""
                Enter your phone number:
            +998"""))
            PHONE_NUM += phone          
            name = input("""
                Enter first your name:
    """).capitalize()
            
            account.append(name)
            surname = input("""
                Enter your surname name:
    """).capitalize()
            
            account.append(surname)
            age = int(input("""
                Enter your age:
    """))
            account.append(age)
            if account[2]>=16:
                B += 1
                yes = int(input("""
                        Do you have a card?
                    [1] - Yes         [2] - No
                """))  
                if yes == 2:
                    card = randint(1000000000000000, 9999999999999999)
                    print(f"""
                    Your new card number:{card}""")
                    card_p = randint(1000, 9999)
                    CARD_NUMBER += card
                    CARD_PASS += card_p
                    print(f"Your card password: {CARD_PASS}\nDon't forget your password!")
            else:
                print("You are not an adult yet!")
                B += 0
        elif account_create == 2:
            print("You can not use our platform without creating an account")
            B += 0
while B:
        print("""
                    Welcome to our platform!""")
        card_num = int(input("""
                Enter your card number:
        """))
        card_pass = int(input("""
                Enter your card password:
        """))
        if CARD_NUMBER==card_num and CARD_PASS==card_pass:
                print(f"Привет {account[0]} {account[1]}!")
                print("""
                [1] - Change card password \t[3] - Currency calculator
                [2] - Balance              \t[4] - Payment
                [5] - Complete""") 
                tanlangan_variant = int(input("Choose:")) 
                if tanlangan_variant==1:
                    new_pass = int(input('Enter a new password: '))
                    re_enter_pass = int(input("Re-enter: "))
                    if new_pass==re_enter_pass:
                        print('Password changed successfully')
                        CARD_PASS=new_pass
                        print(CARD_PASS)
                    else:
                        print("Password error! Enter again!")
                elif tanlangan_variant==2:
                    print(f"Your balance {MONEY}") 
                    print(f"""
                    [1] - Get cash \t[2] - Top up
            """)
                    variant = int(input("Choose:: "))
                    if variant ==1:
                        money1 = int(input("Enter amount: "))
                        MONEY -= money1
                        if money1<= MONEY:
                            print(f"The amount has been withdrawn! Your balance {MONEY}!")
                        else:
                            print("You don't have enough money!")
                    elif variant == 2:
                        sum = int(input("Enter amount: "))
                        MONEY += sum
                        print("Payment succesfull!")
                elif tanlangan_variant==3:  
                    def currency_conversion():
                        from_currency = input("From currency: ")
                        to_currency = input("To currency: ")
                        amount = int(input("Amount:: "))
                        response = requests.get(url)
                        rate = response.json()['rates'][from_currency]
                        amount_in_USD = amount/rate
                        amount = amount_in_USD*(response.json()['rates'][to_currency])
                        amount = int(round(amount,2))
                        print(amount)

                    currency_conversion()
                elif tanlangan_variant==4:
                    print(f"""
                    [1] - Оплата для мобильных операторов
                    [2] - Счета за коммунальные услуги
            """)
                    tolov = int(input("Choose: "))
                    if tolov == 1:
                        nomer = int(input("Enter phone number: +998"))
                        nomer_tolov = int(input("Enter amount:: "))
                        MONEY -= nomer_tolov
                        if nomer_tolov<=MONEY:
                            print("Payment was succesfull!")
                        else:
                            print("You don't have enough money!")
                    elif tolov == 2:
                        print(f"""
                        [1] - Electricity      \t[4] - Internet
                        [2] - Hot water        \t[5] - School
                        [3] - Gas              \t[6] - Garbage
            """)
                        kom_tanglang = int(input("Choose:: "))
                        kom_tolov = int(input("Enter amount:: "))
                        MONEY -= kom_tolov
                        if kom_tolov<=MONEY:
                            print("Your payment has been successfully processed!")
                        else:
                            print("You don't have enough money!")
                    elif tanlangan_variant==5:
                        print("You don't have enough money")
                        break
                    else:
                        print("Нет такого выбора")
                elif tanlangan_variant==5:
                    B == 0
                    break    
        else:
            print("The card number or password is incorrect!")