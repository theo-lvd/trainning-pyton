user_input = input("What's your age ? : ")

try: 
    age = int(user_input)
except:
    print("Please, put a number")