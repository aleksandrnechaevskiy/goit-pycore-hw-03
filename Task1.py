from datetime import datetime

def get_days_from_today(date_str):
    try:
        # Перетворюємо рядок у дату
        input_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        # Визначаємо поточну дату
        today = datetime.today().date()
        # Різниця в днях
        delta = today - input_date
        return delta.days
    except ValueError:
        # Обробка некоректного формату дати
        print("Помилка: дата має бути у форматі 'РРРР-ММ-ДД'")
        return None
print(get_days_from_today('2028-10-01'))  # Тестуємо виведення результату функції



