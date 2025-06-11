import re

def normalize_phone(phone_number):
    # Прибираємо пробіли і всяке зайве
    phone = phone_number.strip()
    # Залишаємо тільки цифри і плюс
    fixed_numbers = re.sub(r'[^\d+]', '', phone)
    
    # Перевіряємо, чи є +, але не +380, і додаємо +38
    if fixed_numbers.startswith('+'):
        if fixed_numbers.startswith('+380'):
            return fixed_numbers
        else:
            return '+38' + fixed_numbers.lstrip('+')
    # Визначаємо, чи починається з 380, і додаємо +
    elif fixed_numbers.startswith('380'):
        return '+' + fixed_numbers
    # Додаємо +38, якщо це просто номер
    else:
        return '+38' + fixed_numbers

# Тестуємо на наших номерах
numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

# Створюємо порожній список для нормалізованих номерів
fixed_numbers = []
for num in numbers:
    result = normalize_phone(num)
    fixed_numbers.append(result)
    # Виводимо, щоб перевірити, що виходить
    print(f"Було: {num}, стало: {result}")

# Виводимо готові номери для SMS
print("Готові номери для SMS:", fixed_numbers)