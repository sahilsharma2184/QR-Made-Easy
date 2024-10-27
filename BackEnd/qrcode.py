import requests #importing requests library to validate the URL which will be entered by the user

print("Welcome to QR Made Easy! Glad to see you here!\n") #Welcome display message

print("What should I call you?") #asking for user's name
name=input() #taking input for name

print("\nHello "+name+", nice to meet you!\n") #Greeting user

print(name+", what would you like to generate a QR code for today?") #Asking url for which QR is to be generated
url=input() #taking input for the url

try:
    response=requests.get(url) #requests.get(url) sends a GET request to the entered url and tries to access the url entered, further the response variable stores the status code that is received back.
    if response.status_code == 200:
        


