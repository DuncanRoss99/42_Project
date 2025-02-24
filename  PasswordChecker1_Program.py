
# Duncan Ross
# 24-02-2025
# PasswordChecker1
'''
PSEUDO CODE:
PROGRAM PasswordChecker1
OUTPUT the name of the program and my name
INPUT password                          {Input phase}
IF password_input = only numbers THEN   {Processing phase}
    OUTPUT only numbers - weak
IF password_input = only letters THEN
    OUTPUT only letters - weak
IF password_input = combination THEN
    OUTPUT password strong              {Output phase}
END PasswordChecker1
'''

#Title of program and developer
print("PasswordChecker1 program developed by: “Duncan”")

#Password input
password_input = input("Please enter a password, with no spaces, to be checked: \n")

#Checks if inputted password only contains numbers
if password_input.isdigit():
    print("Password only contains numbers - weak.")

#Checks if inputted password only contains letters
elif password_input.isalpha():
    print("Password only contains letters - weak.")

#Confirms password is a combination of letters and numbers
else:
    print("Password strong")
