from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    # Отримуємо поточну дату
    today = datetime.today().date()
    
    # Створюємо список для результатів
    upcoming_birthdays = []
    
    # Перевіряємо кожного користувача
    for user in users:
        # Перетворюємо день народження з рядка в об'єкт дати
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # Визначаємо дату народження в поточному році
        birthday_this_year = birthday.replace(year=today.year)
        
        # Перевіряємо, чи день народження вже минув цього року
        if birthday_this_year < today:
            # Якщо минув, беремо дату на наступний рік
            birthday_this_year = birthday.replace(year=today.year + 1)
        
        # Визначаємо різницю в днях між сьогодні і днем народження
        days_difference = (birthday_this_year - today).days
        
        # Перевіряємо, чи день народження в межах 7 днів (включаючи сьогодні)
        if 0 <= days_difference <= 7:
            # Визначаємо дату привітання
            congratulation_date = birthday_this_year
            
            # Перевіряємо, чи день народження припадає на вихідний (субота=5, неділя=6)
            if congratulation_date.weekday() >= 5:
                # Переносимо на наступний понеділок
                days_to_monday = 7 - congratulation_date.weekday()
                congratulation_date = congratulation_date + timedelta(days=days_to_monday)
            
            # Форматуємо дату привітання у рядок
            congratulation_date_str = congratulation_date.strftime("%Y.%m.%d")
            
            # Додаємо користувача і дату привітання до списку
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date_str
            })
            
            # Виводимо для дебагу, щоб бачити, що відбувається
            print(f"Користувач: {user['name']}, день народження: {user['birthday']}, привітаємо: {congratulation_date_str}")
    
    # Повертаємо список привітань
    return upcoming_birthdays

# Тестуємо на наших користувачах
users = [
    {"name": "John Doe", "birthday": "1985.06.10"},
    {"name": "Jane Smith", "birthday": "1990.06.15"},
    {"name": "Bob Johnson", "birthday": "1975.06.14"},  # Субота
    {"name": "Alice Brown", "birthday": "1988.06.16"}
]

# Отримуємо список привітань
result = get_upcoming_birthdays(users)

# Виводимо готові привітання
print("Список привітань на цьому тижні:", result)