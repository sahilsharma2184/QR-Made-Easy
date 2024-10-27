import requests  # Importing requests library to validate the URL
import time  # Importing time library to make the code wait wherever required

print("Welcome to QR Made Easy! Glad to see you here!\n")  # Welcome display message

print("What should I call you?")  # Asking for user's name
name = input()  # Taking input for name

print("\nHello " + name + ", nice to meet you!\n")  # Greeting user

while True:
    print(name + ", what would you like to generate a QR code for today?")  # Asking URL for QR code generation
    url = input()  # Taking input for the URL

    try:
        # Check if the URL has the correct scheme
        if not (url.startswith("http://") or url.startswith("https://")):
            raise ValueError("Invalid URL format. Please make sure the URL starts with 'http://' or 'https://'.")

        # Send a GET request to the entered URL
        response = requests.get(url)

        # Check if the URL is valid (status code 200)
        if response.status_code == 200:
            print(name + ", the URL you entered is valid!\n")
            print("The processing of the QR image and text file has started...")
            time.sleep(2)
            break  # Exit the loop once a valid URL is entered

        else:
            print("The URL you entered returned an error. Please check and try again.")

    except ValueError as ve:
        print(ve)  # Print the error if URL format is incorrect

    except requests.exceptions.RequestException as error:
        print("An error occurred while accessing the URL:", error)
        print("Please check the URL and try again.")
