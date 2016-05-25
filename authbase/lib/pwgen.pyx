import random


def CreatePassword():

    choicesymb = 8
    i = 0
    password = ''
    symbols = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']

    while i<choicesymb:
        tempsymbol = ''
        tempsymbol += random.choice(symbols)
        password += tempsymbol
        i += 1
    return password
    