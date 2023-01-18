import time
import random

#MAKING A KEY SQUARE
def keySquareinMaking(key):
    keySquare = [[], [], [], [], []]

    row = 0;
    for i in range(0, len(key)):
        keySquare[row].append(key[i])
        if (len(keySquare[row]) == 5):
            row+=1;

    for i in range(97, 123):
        if chr(i) in key:
            continue
        elif(i!=106):
            keySquare[row].append(chr(i));
            
        if (len(keySquare[row]) == 5):
            row+=1;
    return (keySquare)

#REMOVING SPECIAL CHARACTERS, SPACE AND 'J' FROM TEXT
def textValidation(text):
    checkText = text;
    text = '';
    for i in checkText:
        if ord(i)>123 or ord(i)<97:
            continue;
        elif i=='j':
            text = text+"i";
        else:
            text = text+i;
    return text;


#CHECKING IF KEY CONTAINS A LETTER MORE THAN ONCE, SPACE AND 'J'
def keyValidation(key):
    temp = True;
    for i in range(97, 123):
        for j in range(0, len(key)):
            if key[j] == 'j':
                temp = False;
                break;
            elif j<=len(key)-2:
                for k in range(j+1, len(key)):
                    if key[k]==key[j]:
                        temp = False;
                        break;
            if temp==False:
                break;

    return temp;
            


#GENERATE A NEW RANDOM KEY
def genKey():
    keyLength = random.randint(3, 7);
    key = ''
    for i in range(97, 123):
        a = random.randint(0, 1);
        if a and chr(i)!='j':
            key = key+chr(i);
        if len(key)==keyLength:
            break;
    return key;

#SPLITTING THE PLAIN TEXT INTO PAIRS
def splitLetters(text):
    wordSplit = []
    flag = 0;
    while True:
        if (flag==len(text)):
            break;
        elif (flag==len(text)-1):
            if text[flag]!= 'x':
                wordSplit.append(text[flag]+"x");
            else:
                wordSplit.append(text[flag]+"q");
            break;
        elif (text[flag]==text[flag+1]):
            if text[flag]!= 'x':
                wordSplit.append(text[flag]+"x");
            else:
                wordSplit.append(text[flag]+"q");
            flag+=1;
        else:
            wordSplit.append(text[flag]+text[flag+1]);
            flag+=2;

    return(wordSplit)


#ENCRYPTING THE TEXT
def encrypt(wordSplit):
    encoded = '';
    for w in range(0, len(wordSplit)):
        for i in range(0, 5):
            for j in range(0, 5):
                    if (keySquare[i][j]==wordSplit[w][0]):
                        ai = i;
                        aj = j;
                    elif (keySquare[i][j]==wordSplit[w][1]):
                        bi = i;
                        bj = j;
        if (ai==bi):
            if aj==4:
                aj = 0;
            elif bj ==4:
                bj = 0;
            encoded = encoded + keySquare[ai][aj+1] + keySquare[bi][bj+1]
        elif (aj==bj):
            if ai==4:
                ai = 0;
            elif bi==4:
                bi = 0;
            encoded = encoded + keySquare[ai+1][aj] + keySquare[bi+1][bj]
        else:
            encoded = encoded + keySquare[ai][bj] + keySquare[bi][aj]
            
    return(encoded)


#DECRYPTING THE TEXT
def decrypt(encoded):
    encodedPairs = [encoded[i:i+2] for i in range(0, len(encoded), 2)]
    decoded = '';
    for w in range(0, len(encodedPairs)):
        for i in range(0, 5):
            for j in range(0, 5):
                    if (keySquare[i][j]==encodedPairs[w][0]):
                        ai = i;
                        aj = j;
                    elif (keySquare[i][j]==encodedPairs[w][1]):
                        bi = i;
                        bj = j;
        if (ai==bi):
            if aj==0:
                aj = 5;
            elif bj ==0:
                bj = 5;
            decoded = decoded + keySquare[ai][aj-1] + keySquare[bi][bj-1]
        elif (aj==bj):
            if ai==0:
                ai = 5;
            elif bi==0:
                bi = 5;
            decoded = decoded + keySquare[ai-1][aj] + keySquare[bi-1][bj]
        else:
            decoded = decoded + keySquare[ai][bj] + keySquare[bi][aj]

    return decoded;



key = "life"
keySquare = keySquareinMaking(key)


while True:
    print("*******************************************")
    print("PLAY FAIR CIPHER'S MENU DRIVEN PROGRAM")
    print("*******************************************")
    print("0. EXIT");
    print("1. ENCRYPT TEXT");
    print("2. DECRYPT TEXT");
    print("3. ENTER NEW KEY");
    print("4. GENERATE A RANDOM KEY");
    print("5. SHOW KEY\n");
    print("*******************************************")
    choice = int(input("Enter your choice: "))
    
    if (choice==0):
        break;
    elif (choice==1):
        text = input("Enter plain text: ").lower();
        text = textValidation(text);
        wordSplit = splitLetters(text);
        encoded = encrypt(wordSplit);
        print("Encrypted Text: ", encoded);
    elif (choice==2):
        print("\n*NOTE: THE DECRYPTED TEXT MAY CONTAIN BOGUS LETTERS*\n")
        text = input("Enter text to decrypt: ").lower();
        decoded = decrypt(text)
        print("Decrypted Text: ", decoded);
    elif (choice==3):
        newkey = input("Enter new key: ");
        valid = keyValidation(newkey);
        if valid==False:
            print("The entered key is not valid. \n\
A key cannot contain 'j' and and repeated letters")
        else:
            key = newkey;
            keySquare = keySquareinMaking(key);
    elif (choice==4):
        key = genKey();
        keySquare = keySquareinMaking(key);
    elif (choice==5):
        print("Current Key: ", key);

    print("\n")
    time.sleep(2) 

