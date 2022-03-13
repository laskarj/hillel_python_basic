from csv import DictWriter, DictReader
"""
Task #4
Exchanger UA - USD
Сложность
4 / 4
Реализовать функционал обменника USD и UAH валют посредством Python.

User Story:
После запуска файла пользователь отдает команду на
- получение курса и остатков COURSE USD
- система проверяет доступость валюты, ее курс и остаток

COMMAND?
>> > COURSE
USD
RATE
27.5, AVAILABLE
13500.98

COMMAND?
>> > COURSE
UAH
RATE
27.3, AVAILABLE
39345.5

COMMAND?
>> > COURSE
BCH
INVALID
CURRENCY
BCH

- обмен

EXCHANGE
UAH
100
- система проверяет дотупно ли нужное количество USD в соответствии с курсом, если количество доступно - поизводит
обмен и обновляет баллансы

COMMAND?
>> > EXCHANGE
UAH
100
USD
3.6363, RATE
0.036363

EXCHANGE
USD
100
- система проверяет дотупно ли нужное количество UAH в соответствии с курсом, если количество доступно - поизводит обмен
и обновляет баллансы
COMMAND?
>> > EXCHANGE
USD
100
UAH
2730, RATE
27.3

- если баланса валюты недостаточно
COMMAND?
>> > EXCHANGE
USD
2000
UNAVAILABLE, REQUIRED
BALANCE
UAH
54600, AVAILABLE
39345.5

- остановку сервиса
STOP
- программа завершается

COMMAND?
>> > STOP
SERVICE
STOPPED

Tech
Requirements:
Ввод данных с помощью функции input. Состояние системы(курс и доступный баланс для каждой валюты) считывается и
хранится в отдельном файле(формат файла на усмотрение разработчика).
"""


def unpacking_data(args: str):  # Name file
    """Function for open file end add data"""
    with open(args) as file:
        read: iter = DictReader(file)
        for items in read:
            data_money: dict = items
            for k, v in data_money.items():
                if v != float:  # We need a float for calculations
                    data_money[k] = float(v)
            return data_money  # return the read data


def course_money(user: str, data: dict):
    """Check rate and money in data exchanger"""
    if user == 'UA':
        return print(f'RATE:\n{data["UA"]},\nAVAILABLE:\n{data["AVAILABLE_UA"]}')
    elif user == 'USD':
        return print(f'RATE:\n{data["USD"]},\nAVAILABLE:\n{data["AVAILABLE_USD"]}')
    else:
        print(f'INVALID CURRENCY: {user}')


def exchange_money(user: str, data: dict, how_match: float):
    """Exchange function"""
    if how_match >= 0:
        if user == 'UA':
            users_usd = how_match / data['UA']
            if data["AVAILABLE_USD"] >= users_usd:
                data["AVAILABLE_UA"] = data["AVAILABLE_UA"] + how_match
                data["AVAILABLE_USD"] = data["AVAILABLE_USD"] - users_usd
                print(f'YOUR MONEY: \n{users_usd}$\nBALANCE:\n{data["AVAILABLE_USD"]}$')
                return data
            elif data["AVAILABLE_USD"] < users_usd:
                print(f"UNAVAILABLE, REQUIRED BALANCE UAH {users_usd}, AVAILABLE {data['AVAILABLE_USD']}")
                return data

        elif user == 'USD':
            users_ua = how_match * data['USD']
            if data["AVAILABLE_UA"] >= users_ua:
                data["AVAILABLE_USD"] = data["AVAILABLE_USD"] + how_match  #
                data["AVAILABLE_UA"] = data["AVAILABLE_UA"] - users_ua  #
                print(f'YOUR MONEY: \n{users_ua}$\nBALANCE:\n{data["AVAILABLE_UA"]}$')
                return data
            elif data["AVAILABLE_UA"] < users_ua:
                print(f"UNAVAILABLE, REQUIRED BALANCE UAH {users_ua}, AVAILABLE {data['AVAILABLE_UA']}")
                return data
        else:
            print(f'INVALID CURRENCY: {user}')
    else:
        raise ValueError('NEGATIVE AMOUNT IS NOT ACCEPTED')


def save_data(data: dict, file: str, ):
    """Save data in file csv"""
    with open(file, 'w') as csvfile:
        # fieldnames = ['UA', 'AVAILABLE_UA', 'USD', 'AVAILABLE_USD']
        writer = DictWriter(csvfile, fieldnames=data.keys())  # Table header = key in data
        writer.writeheader()  # Save head
        return writer.writerow(data)  # Save and return data in csv file


if __name__ == "__main__":  # If main to start
    data_exchanger: dict = unpacking_data('exchanger_money.csv')
    user_inquiry: str = input('COMMEND?\n>').upper()
    if user_inquiry == "COURSE":
        user_currency: str = input('UA or USD?\n>').upper()
        course_money(user_currency, data_exchanger)
    elif user_inquiry == "EXCHANGE":
        user_currency: str = input('UA or USD?\n>').upper()
        many_money = float(input('HOW MUCH OF YOUR MONEY\n>'))
        finish_data = exchange_money(user_currency, data_exchanger, many_money)
        save_data(finish_data, 'exchanger_money.csv')
    elif user_inquiry == "STOP":
        print(f'SERVICE STOPPED')
        exit()
    else:
        print(f"COMMAND NOT FOUND:{user_inquiry}")
