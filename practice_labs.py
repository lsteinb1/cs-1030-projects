def main():
    age = int(input("How old are you?: "))
    if ((age >= 13) and (age <= 17)):
        print("You are a teenager.")
    elif ((age >= 18) and (age <= 49)):
        print("You are an adult.")
    elif (age >= 50):
        print("You are getting old.")
        
main()