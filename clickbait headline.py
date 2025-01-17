#Oliver Borowski
#Clickbait generator
#Functions
#offers three different types of headlines for the reader to devide from
def believe_headline(): #healine tht makes sense
    noun = input("Please enter a noun: ")
    ppronoun = input("Please enter a possesive pronoun: ")
    place = input("Please enter a place: ")
    print("You won't believe what this " + noun + " found in " + ppronoun + " " + place + ".")
def surprising_headline():#healine that will likely surpruse the user
    num = input("Please enter a number: ")
    adj = input("Please enter a adjective: ")
    pronoun = input("Please enter a pronoun: ")
    print(str(num) + " " + adj + " SE0 Trick " + pronoun + " Don't Know.")
def program_headline():
    num = input("Please enter a number: ")
    type = input("Please enter a type of program: ")
    person = input("Please enter a type of person: ")
    print(str(num) + " " + "reasons why " + person + " love this " + type + " program.")

#Main
believe_headline()
surprising_headline()
program_headline()
