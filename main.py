import helper

while True:
    choice = int(input("1 – Запустить помощник\n0 – Выйти\n\nВвод: "))
    if choice == 1:
        one = int(input("\nПервое: "))
        two = int(input("Второе: "))
        r = helper.helper_module(one, two)
        print(f"\nResult: {r}")
    elif choice == 0:
       exit()
    else:
        continue
   