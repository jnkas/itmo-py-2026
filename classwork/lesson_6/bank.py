
# Банкхранит деньги
# + Изначально 1000 денег
# Управление через меню, путем ввода текста 1 - Баланс, 2 - Пополнить счет, 3 - вывести со счета, 4 - выход
# написать функции для всех действий со счетом

balance = 1000

def showMenu():
    print('''
        # Меню
        1. Баланс
        2. Пополнить счет
        3. вывести со счета
        4. выход
    ''') 

def deposit():
    global balance
    amount = int(input("Сколько прибавить? "))
    balance = balance + amount
    print(f'Счет увеличился, баланс: {balance}')

def withdraw():
    amount = int(input("Сколько убавить? "))
    balance = balance - amount
    print(f'Счет уменьшился, баланс: {balance}')

def choseMenu(n):
    global balance
    match n:
        case 1:
            print(balance)
        case 2:
            deposit()
        case 3:
            withdraw()
    

def main():
    while True:
        showMenu()

        inp = int(input("Выберите пункт меню: "))
        if type(inp) != type(1):
            print("Введите число")
            inp = int(input("Выберите пункт меню: "))
        
        choseMenu(inp)

        if inp == 4:
            print('Выход из программы') 
            break 

# Запуск всей программы
main()
