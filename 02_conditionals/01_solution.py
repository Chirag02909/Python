age = int(input("Enter an age : "))

if age < 13:
    print("user is child")
elif age < 20:
    print("user is teenager")
elif age < 60:
    print("user is adult")
else:
    print("user is senior")