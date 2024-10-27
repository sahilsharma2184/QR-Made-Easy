import requests #Importing requests library to validate the URL which will be entered by the user
import time #Importing time library to make the code wait wherever required

print("Welcome to QR Made Easy! Glad to see you here!\n") #Welcome display message

while True:
    print("Hey!, what should I call you?") #Asking for user's name
    name=input() #Taking input for name

    print("\nHello "+name+", nice to meet you!\n") #Greeting user
    print(name+", what would you like to generate a QR code for today?") #Asking url for which QR is to be generated
    
    url=input() # Taking input for the url

    try:
        #Checking if the url is having correct scheme
        if not url.startswith("https://") or url.startswith("http://"): #Validates the url given to check whether it starts with 'https://' or 'http://'
            print(name+" I guess that you have entered wrong url, kindly check that and enter again.") #Incase there is any mistake in the entered url, then it prompts the user to enter the url again
            continue #this skips the current  iteration for the loop and asks for the url again
        
        response=requests.get(url) #requests.get(url) sends a GET request to the entered url and tries to access the url entered, further the response variable stores the status code that is received back.            
        if response.status_code == 200: #if condition to check that whether the site is responsding not 
                print(name+", the url you entered is valid!\n") #Displaying message for the user to tell that the entered URL is valid
                print("The processing of QR image and text file has started..") #Now as the validity of URL is checked so the next stage begins where the generation of QR image and Text file is started
                time.sleep(2) #The code sleeps for 2 seconds so that the user gets a feel that the processing is going on
                break
        else:
                print(name+" the url that you entered returned an error. Please try again.")

    except requests.exceptions.RequestException as error: #This block catches, handles and displays any errors that occur when trying to access the URL
            print("Error occured: ",error) #Displays the error that occured for review

