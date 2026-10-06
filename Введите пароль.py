password = input("Введите пароль")

if len(password) < 8:
    print('Короткий')
elif password.isdigit():
    print("только цифры")
else:
    print('норм')