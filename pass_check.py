import getpass
password = getpass.getpass("Enter your password: ")


print ( " CHECKING ISSUES WITH YOUR PASSWORD.....")



issuecount = 0 
print("The issues with your password: ")

if len(password)<8:
    print("-too small to be difficult")
    issuecount += 1 
if not any(char.isdigit() for char in password):
    issuecount += 1
    print("-may add some numbers to it ")
if all(char.isalnum() for char  in password):
    issuecount += 1 
    print("-special characters are missing")
if not any(char.isupper() for char in password):
    issuecount+=1
    print("-enter a uppercase character")
if not any(char.islower() for char in password):
    issuecount+=1
    print("-enter a lowecase character")
    
if issuecount == 0:
    print('THERE ARE NO ISSUES!, perfect!')
elif issuecount <= 2:
    print("PASSWORD STATUS : strong")
elif issuecount <= 4:
    print("PASSWORD STATUS : bad password")
else:
    print("not eligible to be a password , do it again!")