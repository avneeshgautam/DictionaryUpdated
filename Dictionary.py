import time
from csv import DictReader,DictWriter

###########  FUNCTOINS  ###############

#$$$$$$$$$$$$$$$$$$$$$$$$4 CREATING NEW FILE $$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def file_create():
    f1=open('dictionary_list.csv','a')
    f1.close()

# $$$$$$$$$$$$$$$ LOGOUT FUNCTION $$$$$$$$$$$$$$$$$$$$$$$$$$$4444
def logout():
    exit()

# $$$$$$$$$$$$$$$ OPEN FILE $$$$$$$$$$$$$$$$$$$$$$$$$$$
def open_dir():
    with open('dictionary_list.csv','r') as rf:
        csv_reader = DictReader(rf)
        for row in csv_reader:
            dict[row['word']]=row['meaning']


# $$$$$$$$$$$$$$$$$$$ WELCOME SCREEN $$$$$$$$$$$$$$$$$$$$$
def welcome():
    print("\n\tWELCOME TO AVNEESH DICTIONARY")
    print("-------------------------------------------------------")
    print("\t# 1. ADMIN \n \t# 2. USER \t\t|")
    print("-------------------------------------------------------")

# $$$$$$$$$$$$$$$$$$$ SHOW WORDS MEANING $$$$$$$$$$$$$$$$$

def show():
    if dict_list ==[]:  
        print("Dictionary is empty: \n Add word in dictionary:")
        print("Exiting..\n")
        time.sleep(0.5)
        print("\t\tGOODBYE")
        print("-------------------------------------------------------")

            # if dictionary list is not empty ##    
    else:
        for i in dict_list:
            print(i)
        print("-------------------------------------------------------")

 ############# word show or add ############ 
def admin_show_add():
    print("############ OPTION #########")
    print("1. SHOW \n2. ADD \n3. Remove \n4. Logout")
    print("-------------------------------------------------------")
    time.sleep(0.3)
    val= input("Enter Choice (show / add / remove / logout): ")
    print("-------------------------------------------------------")
    if val=='show':
        print("###### WORDS FOUND ###########")
        show()
        print("\n--------------------------------------")
        admin_show_add()

    ############## ADDING Word/meaing in dictnary List #############    
    elif val =='add':
        print(dict_list)
        print("-------------------------------------------------------")

        # ############# WRITNG in Dictionat_list.csv file #######
        with open('dictionary_list.csv','a') as f:
            csv_writer = DictWriter(f,fieldnames=['word','meaning'])
            csv_writer.writeheader()

            ######### adding word ################
            while(1):
                more=input("Do you want add more (Press 1): ")
                if more == '1' or more == 1:
                    more_add(csv_writer)
                
                else:
                    print("-------------------------------------------------------")
                    print("\n")
                    admin_show_add()
    
    elif val =='remove':    # REMOVE FILE
        print("feature is not found\n")
        admin_show_add()
    
    elif val == 'logout':   # LOGOUT FILE 
        print("-----------------------------------")
        print("\t GOODBYE ADMIN...........")
        time.sleep(0.7)
        print("\n################################################\n")
        welcome()
        main_func()
    
    else:
        print("Wrong choice...\n Try again...........")
        admin_show_add()

# $$$$$$$$$$$$$$$$$$$$$  ADDING MORE WORDS $$$$$$$$$$$$$$$$$$$$$$$$

def more_add(csv_writer):
    word=input("\nEnter the word: ")
    meaning=input("Enter the meaning: ")
    print("\n")
    csv_writer.writerow({
    'word':word,'meaning':meaning
    })



############### ADMIN FUNCTION ##############
def admin():
    username=input("Enter username: ")   #USERNAME
    password=input("Enter the password: ") 
    print("-------------------------------------------------------")
    print("LOGIN..........\n")
    time.sleep(0.6)

    ############# login password #######333333
    if username == 'avneesh' and password =='12345':
        print("\n\t\tWELCOME ADMIN")
        print("-------------------------------------------------------")

        ############# word show or add ############   
        admin_show_add()

    else:
        print("-------------------------------------------------------")
        print("Username or Password is incorrect")
        print("\nTry Again...")
        admin()

######################## FINDING BY FIRST LETTER ########################

def by_letter():
    enter=input("\nEnter first letter: ")
    print("--------------------------------------------")
    print("\tFinding........")
    time.sleep(1)
    
    print("\nWORD:\t\tMEANING")
    print("------------------------------------")
    for i in dict_list:
        if enter == i[0]:
            # print(i)
            print(i+"\t\t"+str(dict[i]))
    print("\n")

######################## FINDING BY WORD ########################
def Full_word():
    word=input("\nEnter the Word: ")
    print("--------------------------------------------")
    print("\tFinding........")
    time.sleep(1)
    
    if word in dict.keys():
        print("\nWORD:\t\tMEANING")
        print("------------------------------------")
        print(word+"\t\t"+str(dict[word]))
        print("\n")
    else:
        print("\nNot found:\n")   

######################################33
def more_new():
    print("\n############################################")
    more=input("Do you want find more Meaning (yes/no): ")
    if more in yes:
        user_finding()    #user finding function calling
    else:
        print("\n-------------------------------------")
        print("OK Exiting..........")
        time.sleep(0.5)
        print("\t GOOD BYEE")
        print("-------------------------------------")
        logout()


################ USER FINDING #################


def user_finding():
        print("\n################# OPTION ##################")
        print("1. Find by First letter \n2. Find by word")
        find=input("Press (1 OR 2 ): ")

        ###############  YES ################
        if find == '1' or find == 1:
            by_letter()
            more_new()

        elif find == '2' or find == 2:
            print("-------------------------------------------------------")
             # find by word 
            Full_word()
            more_new()

        else:
            print("\nINVALID CHOICE")
            print("Try again..........")
            time.sleep(0.4)
            user_finding()


def main_func():
    ad_user=input("You are Admin or User: ")
    print("-------------------------------------------------------")

    ############# ADMIN SECTION #########################

    if ad_user == 'admin':
        admin()

    ############### USER SECTION ################
    elif ad_user == 'user':
        print("-------------------------------------------------------")
        ####### finding words ##############
        print("\nFinding All Word in dictionary:")
        print("\tFinding........\n")
        time.sleep(1.2)
        print("------------------------------------")
            ################   check dictionary ############## 
        if dict_list ==[]:
            print("Dictionary is empty:")       
            print("\t Try Again later....")
            print("------------------------------------")
            exit()
        else:
	    print(dict_list)
            #for i in dict_list:
                #print(i)
		#new_list.append(i)
	    #print(str(new_list))
		
            print("------------------------------------")

        ################  FINDING MEANING OF WORD BY LETTER
            user_finding()



word =[]
meaning=[]
dict={}

# create file with name dictionary_file.csv
file_create()

# now open file
open_dir()


## normal list
list=dict.keys()
# sort words from dic to list
dict_list=sorted(list)
yes=['yes','YES','Yes']
no=['no','No','NO']

########### welcome screen ############
welcome()
main_func()
