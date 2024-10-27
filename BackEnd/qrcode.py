import requests #importing requests library to validate the URL which will be entered by the user
import time #importing time library to make the code wait wherever required
print("Welcome to QR Made Easy! Glad to see you here!\n") #Welcome display message

print("What should I call you?") #asking for user's name
name=input() #taking input for name

print("\nHello "+name+", nice to meet you!\n") #Greeting user

while True:
    print(name+", what would you like to generate a QR code for today?") #Asking url for which QR is to be generated
    url=input() #taking input for the url

    if not url.startswith("https://") or not url.startswith("http://"): #checking if the url is 
        print(name+" I guess that you have entered wrong url, kindly check that and enter again!")
    try:
        response=requests.get(url) #requests.get(url) sends a GET request to the entered url and tries to access the url entered, further the response variable stores the status code that is received back.
        if response.status_code == 200: #if condition to check that whether the site is responsding not 
            print(name+", the url you entered is valid!\n")
            print("The processing of QR image and text file has started..")
            time.sleep(2)
            break
        else:
            print(name+" I guess that you have entered wrong url, kindly check that and enter again!")
            url=input()
    except requests.exceptions.RequestException as error:
        print("Error occured: ",error)

