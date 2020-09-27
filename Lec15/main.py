from model.user import User 

u1 = User(
    username="Bob",
    password="12345secret",
    email="bob@bob.com"
)

u2 = User(
    username="Alice",
    password="secret_secret",
    email="alice@alice.com"
)

# Проверка правильности создания объектов
users = [u1, u2]
for user in users:
    print(user)


# Добавлю все объекты в бд
for user in users:
    user.save()

# Поменяю адреса электронной почты
users[0].update_email("bob@yandex.ru")
users[1].update_email("alice@rambler.ru")

print("Есть ли кто с именем `bob`? : ", User.check_by_name("bob"))

# Получим всех пользователей
all_users = User.get_all_users()
for us in all_users:
    print(us)

# Удаляем бобов
users[0].delete()
users[1].delete()

