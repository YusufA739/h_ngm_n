import random

def wordselect():
    words=open("wordsforhangman.txt","r") #changed file names 'words 1000'-> 'words 1000 original' and 'words1000'-> 'words 1000' but wordsforhangman.txt (the biggest file by a mile!) is the file that is the main one in use. It has a LOT of words (and rather vague ones at that) so it is my humble opinion that it shold be current word pool. Increase the frequency for words by adding repeats at the bottom. This makes it easier to remove repeats
    data=words.readlines()
    dataFormatted=[]
    for carrier in data:
        dataFormatted=carrier.split(" ")
    try:
        dataFormatted.remove('')
    except:
        pass
    index=random.randint(0,len(dataFormatted)-1)
    word=dataFormatted[index]
    return(word)



def hangmanmain(word):
    #main program
    #print("Chose and option: Start the game (A), Add a new word (B), Exit (C)")
    #choice = input(": ")
    lives=15
    score=0
    guesses=[]
    numbers = ['0','2','3','4','5','6','7','8','9']


    cypher =["_"] * len(word)
    print("the word has",len(word),"characters")
    
    while lives >= 0:#similar to pacman coin system
        letter = input("Input a letter or the word or type 1 for next word:")

        if letter == '1':#quit game
            return(-9999999999)

        numbersPresent = False
        for carrier in letter:
            if carrier in numbers:
                numbersPresent = True
                break

        if letter == "":
            continue
        elif letter in guesses:
            print("Letter already guessed...")
        elif numbersPresent:
            print("Numbers present in guess...")
        else:
            lives -= 1
            if len(letter)==1:
                #print(cypher) old cypher is displayed to compare against new one, but it clutters screen too much imo
                for carrier in range(len(word)):
                    if word[carrier] == letter:
                        score+=10#no need to check for repeated inputs that force more points. This is because of prerequisite check of 'if letter in guesses:'
                        cypher[carrier] = letter

                print(cypher)#print new cypher only

            elif len(letter)>1:
                if letter==word:
                    print(word.split(""))#quickly display the list without doing any cypher iteration
                    score=score+100#rebalance 50->100
                else:
                    print(cypher)

    print("The word was", str(word))
    print(score)
    return(score)
def scoresandnames(score):
    if score == -9999999999:
        return(-1)#tells game to quit in main game loop


    print("upload score?")
    scoreupload=input("(Y/N)>>")
    if scoreupload.upper()=="YES" or scoreupload.upper()=="Y":
        username=input("Input Username:")
        file=open("TABLEOFSCORES.txt","a")
        troll=[["The user known as:",0.2],["The idiot called",0.1],["This dead guy -->",0.2],["Number #1 player:",0.01],["The user by the name of:",0.9]]
        total_probability = 0
        for placeholder in troll:
            total_probability += placeholder[1]
        random_value = random.random() * total_probability
        cumulative_probability = 0
        prename_text = ""
        for placeholder in troll:
            cumulative_probability += placeholder[1]
            if random_value < cumulative_probability:
                prename_text=placeholder[0]
                break
        
        post_texts=[["a weak score of:",0.2],["a really bad score of:",0.1],["an amazing score of:",0.2],["Number #1 player:",0.01],["The user by the name of:",0.9]]
        total_probability = 0
        for placeholder in post_texts:
            total_probability += placeholder[1]
        random_value = random.random() * total_probability
        cumulative_probability = 0
        postname_text = ""
        for placeholder in post_texts:
            cumulative_probability += placeholder[1]
            if random_value < cumulative_probability:
                postname_text=placeholder[0]
                break

        write_data=str(prename_text+" "+username+" has scored "+postname_text+" "+str(score)+"\n")
        file.write(write_data)
        file.close()
        return(1)#shows operation was successful
    else:
        return(2)#shows operation was successful (alternate operation)
        pass

#main game loop
while True:
    semaphore = scoresandnames(hangmanmain(wordselect()))
    if semaphore == -1:
        break
    elif semaphore == 1:
        print("Saved...")
    elif semaphore == 2:
        print("Not saved...")