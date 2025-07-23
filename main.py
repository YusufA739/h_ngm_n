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
    lives=16
    valid = False
    score=0
    
    
    cypher =["_"] * len(word)
    print("the word has",len(word),"characters")
    
    while not valid:
        emptyspaces = 0
        letter = input("Input a letter or the word:")
        if letter == "":
            continue

        elif len(letter)==1:
            
            count = 0
            print(cypher)
            for carrier in range(len(word)):
                if word[carrier] == letter:
                    score+=10
                    count+=1
                    cypher[carrier] = letter
                    
            for carrier in range(len(cypher)):
                if cypher[carrier] == "_":
                    pass
                else:
                    emptyspaces = emptyspaces + 1
            if emptyspaces == len(word):
                valid = True
                                 
            print(cypher)

        elif len(letter)>1:
            #code
            if letter==word:
                temp_list=[]
                for carrier in letter:
                    temp_list.append(carrier)
                print(temp_list)
                #for aesthetics
                valid=True
                
                score=score+50
            else:
                print(cypher)
        
        elif valid==False:
            
            if lives==0:
                print("you lost!")
                valid=True
            else:
                lives=lives-1
    print("The word was", str(word))
    print(score)
    return(score)
def scoresandnames(score):
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
    else:
        pass

def run():
    scoresandnames(hangmanmain(wordselect()))
run()