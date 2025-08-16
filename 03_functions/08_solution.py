def print_kwargs(**kwargs):
    for key , value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="batman" , power="lazer")
print_kwargs(name="batman")
print_kwargs(name="batman" , power="lazer" , enemy = "thor")