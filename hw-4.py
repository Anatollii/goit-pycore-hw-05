from typing import Callable


# Декоратор для обробки помилок
def input_error(func: Callable):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "❌ Помилка: контакт не знайдено."
        except ValueError:
            return "❌ Помилка: введіть ім'я та телефон через пробіл."
        except IndexError:
            return "❌ Помилка: введіть аргументи для команди."
    return inner


# Парсинг команди та аргументів
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


# Додати контакт
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"✅ Контакт {name} додано."


# Змінити існуючий контакт
@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"🔁 Контакт {name} оновлений."


# Показати телефон за ім'ям
@input_error
def show_phone(args, contacts):
    name = args[0]
    return f"📱 Телефон контакту {name}: {contacts[name]}"


# Показати всі контакти
def show_all(contacts):
    if not contacts:
        return "Контактів поки немає."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


# Тестуємо
def main():
    contacts = {}
    print("📞 Ласкаво просимо в помічник-бота!")

    while True:
        user_input = input("Введіть команду: ").strip()
        if not user_input:
            continue

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("👋 До побачення!")
            break
        elif command == "hello":
            print("Привіт! Як я можу вам допомогти?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("❓ Невідома команда. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
