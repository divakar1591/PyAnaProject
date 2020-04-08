import functools


user = {"username": "jose",  "access_level": "guest"}

def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user['access_level'] == "admin":
            return func()
        return f"No Admin permission for {user['username']}."
    return secure_function

@make_secure
def get_admin_password():
    return "1234"

print(get_admin_password.__name__)

"""
NOTE: By using @make_secure, get_admin_password() is not a register function. It is variable now
print(get_admin_password.__name__),  O/P-secure_function
so now use functools
"""