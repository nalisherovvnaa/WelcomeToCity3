# 3 Welcome to the City
def welcome(name, city, state):
    full_name = ' '.join(name)
    return f"Hello, {full_name}! Welcome to {city}, {state}!"

print(welcome(['John', 'Smith'], 'Phoenix', 'Arizona'))
