# Challenge 3
# Browsing history

import webbrowser
#dictionary does not allow duplicate
DATABASE = {}

#defining intialisation method(run only when it is called)
class Webpage:
    def __init__(self, URL):
        self.URL = URL

#recording URL visited
def record():
    while True:
        URL = str(input('\nEnter the url you want to visit: '))
        webbrowser.open(URL)
        New_URL = Webpage(URL)
        DATABASE[URL] = New_URL
        break

#History of Url visited
def history():
    while True:
        #when database is empty
        if len(DATABASE)==0:
            print("No URL was visited\n")
            break
        #database is not empty
        else:
            for items in DATABASE:
                print("*",items)
            break


while True:
    print("\nOptions:")
    print('1. Visit the website')
    print('2. View all the URLs visited\n')
    choice = int(input("Select an option: "))
    if choice == 1:
        record()
    elif choice == 2:
        print("\nHistory")
        history()

    else:
        print("invalid option, try again")