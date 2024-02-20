#Exclusive Network
print("\tExclusive Computer Network")
print("\t\t memebers only!!\n")
security=0
username=""
while not username:
    username=input("username:")
password=""
while not password:
    password=input("password:")

    if username=="M.Dawson" and password=="secret":
        print("Hi,Mike")
        security=5
    elif username=="S.Meier"and password=="Civilization":
        print("Hey,Sid.")
        security=3
    elif username== "S.Mitamoto" and password=="mariobros":
        print("What's up.Shigeru?")
        security=3
    elif username=="maturity" and password=="mass":
        print("YOh bro!!")
        security=3
    elif username=="huyaaa"and password=="Ijali":
        print("living life")
        security=1
    else:
        print("login failed.You are not so exclusive")
