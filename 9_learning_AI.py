age = input("What's your age? : ")

if age.isdigit():
    age = int(age)
    if age < 13:
        print("You are a child.")
    elif age < 18:
        print("You are a teenager.")
    else:
        print("You are an adult.")