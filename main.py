# Kodni bu yerga yozing

while True:

    choice = int(input("""===== Loop Lab: Interaktiv Topshiriqlar =====
    1. 🎯 Maxfiy sonni toping (Random son o'yini)
    2. 🔄 So'zni teskari yozish
    3. 🔢 Sonlar orasidagi eng kichigini topish
    4. 🧮 FizzBuzz o'yini (1 dan N gacha)
    0. ❌ Dasturdan chiqish
    =============================================
    Tanlang: """))


    if choice == 1:
        
        from random import randint

        print("\n=====🎯 Maxfiy sonni toping (Random son o'yini)=====\n")
        print("1 dan 20 oralig'ida raqam o'ylab qo'ydim. Topa olasizmi?")
        print("Sizga 5 marta imkoniyat beraman\n")

        number = randint(1, 20)

        attempts = 0

        while attempts < 5:

            answer = int(input(f"{attempts + 1}-urinish: "))
    
            attempts += 1

            if answer == number:
                print("Topdingiz!")
                break

            elif answer > number:
                print("Katta")

            else:
                print("Kichik")

        else:
            print("Topolmadiz")
            print(f"To'g'ri javob: {number}")


    elif choice == 2:

        print("\n=====🔄 So'zni teskari yozish o'yini=====\n")
        print("Xoxlagan so'z yozing teskarisiga chiqarib beraman\n")

        text = input("So'z kiriting: ")
        reverse = ""

        for letter in text:
            reverse = letter + reverse

        print(reverse)


    elif choice == 3:

        print("\n=====🔢 Sonlar orasidagi eng kichigini topish o'yini=====\n")
        print("Xoxlagan 5 ta son kiriting. Eng kichigini topib beraman\n")

        min = 0
        number = int(input("1-sonni kiriting: "))
        min = number

        for i in range(4):
            number = int(input(f"{i+2}-sonni kiriting: "))
        
            if min <= number:
                min = min

            else:
                min = number 

        print("Eng kichik son:", min)


    elif choice == 4:
        print("\n=====🧮 FizzBuzz o'yini (1 dan N gacha)=====\n")
        print("1 dan boshlab siz istagan songacha 3 va 5 ga bo'linadigan sonlarni chiqarib beraman\n")

        number = int(input("Son kiriting: "))

        if number <= 1:
            print("Iltimos 1 dan katta son kiriting")

        else:
            for son in range(1, number+1):
                if son % 5 == 0 and son % 3 == 0:
                    print("FizzBuzz")

                elif son % 3 == 0:
                    print("Fizz")

                elif son % 5 == 0:
                    print("Buzz")
        
                else:
                    print(son)


    elif choice == 0:
        print("Dastur yakunlandi. Xayr!")
        break


    else:
        print("Iltimos faqat 0 dan 4 gacha son kiriting")