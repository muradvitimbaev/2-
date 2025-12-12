# Декоратор доступа
def require_role(allowed_roles):
    def access(func):
        def wrapper(*args, **kwargs):
            if args[0]['role'] not in allowed_roles:
                print(f"Доступ запрещён пользователю {args[0]['name']}")
            else:
                func(*args, **kwargs)
        return wrapper
    return access

@require_role(["admin"])
def delete_database(user):
    print(f"База данных удалена пользователем {user['name']}")

user = {"name": "Иван", "role": "manager"}
user1 = {"name": "Егор", "role": "admin"}
delete_database(user)
delete_database(user1)