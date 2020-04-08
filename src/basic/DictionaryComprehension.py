import json

users = [
  (0, "divakar", 60.55),
  (1, "divakar1", 61.55),
  (2, "divakar2", 62.55),
  (3, "divakar3", 63.55)
]

username_mapping = {user[1]: user for user in users}

jsn = json.dumps(username_mapping)
print(jsn)