import functools


user = {"username": "jose"}

def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if access_level == "admin":
                return func(*args, **kwargs)
            return f"No {access_level} permission for {user['username']}."
        return secure_function
    return decorator

@make_secure("admin")
def get_admin_password():
    return "admin: 1234"

@make_secure("guest")
def get_dashboard_password():
    return "user: user password"


print(get_admin_password())
print(get_dashboard_password())
