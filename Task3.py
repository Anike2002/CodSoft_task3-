import random 

print("Welcome to the Password generator")

while True:
    Characters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    characters = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','@','#','$','%','^','&','*','(',')','/','"','{','}','-',':',';','[',']','_','<','>','=','+'] 

    length = int(input("Enter the password length :"))
    
    Uppercase = Characters
    print("Uppercase letters {}".format(Uppercase))
    lowercase = characters
    print("lowerercase letters {}".format(lowercase))
    digits = numbers 
    print("Numbers {}".format(numbers))
    special_characters = symbols
    print("Special characters {}".format(special_characters))

    if length < 4:
        print("Invaid length. Enter again ")
        continue 
    
    all_characters = Uppercase + lowercase + digits + special_characters 
    characters = random.sample(all_characters,length)
    print(characters)

    password = "".join(characters)
    print("Generated password {}".format(password))
    