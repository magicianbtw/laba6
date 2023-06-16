class Entry:
    def __init__(self, name, surname, date_of_birth, phone_number):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number


class Directory:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def remove_entry(self, entry):
        self.entries.remove(entry)

    def search_entries(self, attribute, value):
        results = []
        for entry in self.entries:
            if getattr(entry, attribute) == value:
                results.append(entry)
        return results

    def sort_entries(self, attribute):
        self.entries.sort(key=lambda entry: getattr(entry, attribute))


directory = Directory()

name1 = input("Введите имя для первого человека: ")
surname1 = input("Введите фамилию для первого человека: ")
dob1 = input("Введите дату рождения для первого человека (YYYY-MM-DD): ")
phone1 = input("Введите телефон для первого человека: ")

entry1 = Entry(name1, surname1, dob1, phone1)

name2 = input("Введите имя для второго человека: ")
surname2 = input("Введите фамилию для второго человека: ")
dob2 = input("Введите дату рождения для второго человека (YYYY-MM-DD): ")
phone2 = input("Введите телефон для второго человека: ")

entry2 = Entry(name2, surname2, dob2, phone2)

directory.add_entry(entry1)
directory.add_entry(entry2)

surname_query = input("Введите фамилию для поиска: ")
results = directory.search_entries("surname", surname_query)
if results:
    print("Соответствующие записи:")
    for entry in results:
        print(
            f"Имя: {entry.name}, Фамилия: {entry.surname}, Дата рождения: {entry.date_of_birth}, Телефон: {entry.phone_number}")
else:
    print("Подходящие записи не найдены.")

print("Все записи:")
for entry in directory.entries:
    print(
        f"Имя: {entry.name}, Фамилия: {entry.surname}, Дата рождения: {entry.date_of_birth}, Телефон: {entry.phone_number}")

entry_to_remove = input("Введите имя записи, которую нужно удалить: ")
for entry in directory.entries:
    if entry.name == entry_to_remove:
        directory.remove_entry(entry)
        print("Запись успешна удалена!")
        break

print("Все записи:")
for entry in directory.entries:
    print(
        f"Имя: {entry.name}, Фамилия: {entry.surname}, Дата рождения: {entry.date_of_birth}, Телефон: {entry.phone_number}")