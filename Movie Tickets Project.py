def city():
    print("Which city you want to watch a movie \n ")
    print(" 1. Pune \n 2. Mum \n 3. Delhi \n 4. Bang")
    city = int(input())
    if city == 1 or 2 or 3 or 4:
        select_theater()
    else:
        print("Please selcet out of given choices only \n")
        city = int(input())
        select_theater()


def select_theater():
    theater = int(input("Please select theater (type number) \n \n 1.Inox \n 2.PVR \n 3.Bollywood \n "))
    select_movie()


def select_movie():
    print("Select from below available movies:\n ")
    print(" 1. PK \n 2. Dhoom \n 3. KGF")

    movie = int(input())
    timing(movie)


def number_tickets():
    n1 = int(input("Enter number of tickets : \n "))
    return n1


def timing(movie):
    if movie == 1:
        print(''' Pk is screening in "Screen 1" all day \n''')
        dict_1 = {'1': "9.00 am to 11.59 am",
                  '2': "1.00 pm to 4.00 pm",
                  '3': "5.00 pm to 8.00 pm"}
        print(dict_1)
        t = input("Choose time :\n ")
        timee = (dict_1[t])
        n1 = number_tickets()

        print(f'''Congratulations {n1} ticket of movie "Dhoom" at time slot '{timee}' booked  ''')

    if movie == 2:
        print(''' Dhoom is screening in "Screen 2" all day \n ''')
        dict_1 = {'1': '9.15 am to 11.00 am',
                  '2': '1.15 pm to 4.15 pm',
                  '3': '5.15 pm to 8.15 pm'
                  }
        print(dict_1)
        t = input("Choose time : \n")
        timee = (dict_1[t])
        n1 = number_tickets()

        print(f'''Congratulations {n1} ticket of movie "PK" at time slot '{timee}' booked  ''')

    if movie == 3:
        print(''' KGF is screening in "Screen 3" all day \n''')
        dict_1 = {'1': '9.15 am to 11.00 am',
                  '2': '1.15 pm to 4.15 pm',
                  '3': '5.15 pm to 8.15 pm'}
        print(dict_1)
        t = input("Choose time :\n ")
        timee = (dict_1[t])

        n1 = number_tickets()

        print(f'''Congratulations {n1} ticket of movie "KGF" at time slot '{timee}' booked  \n''')


name = input("Enter your name : \n")
print(
    f"\nHello {name} ...! Welcome to Movie-Buzz 🙋‍ \nWanna book movie tickets ? It all starts here. All latest movie bookings available.\n")

city()

print("Note : Login with the same ID there will be special discounts next time with snacks vouchers ")

