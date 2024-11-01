import requests #Importing requests module to validate the URL which will be entered by the user
import time #Importing time module to make the code wait wherever required
import qrcode #Importing qrcode module to generate the qrcode for the url given by the user
import smtplib #Importing smtplib module to send emails using the Simple Mail Transfer Protocol(SMTP)
from email.mime.multipart import MIMEMultipart #MIMEMultipart can hold multiple parts like images/PDFs/files/plain text or HTML message
from email.mime.text import MIMEText #MIMEText creates the HTML or text part of email body, allows to specify the content of mail. After creation the text component can be addded to the MIMEMultipart container to form the body of the mail
from email.mime.base import MIMEBase #MIMEBase is a base class to add the attachments to your mail
from email import encoders  #encoders is used to emcode attachments in base64 since they can be binary(images/PDFs), for transmission over SMTP

print("Welcome to QR Made Easy! Glad to see you here!\n") #Welcome display message

print("Hey, Let's have a quick introduction!\n") #Asking for user's name
print("What should I call you ?")
name=input() #Taking input for name

print("\nHello "+name+", nice to meet you!\n") #Greeting user

while True:
    print(name+", what would you like to generate a QR code for today?") #Asking url for which QR is to be generated
    url=input() # Taking input for the url

    try:
        #Checking if the url is having correct scheme
        if not (url.startswith("https://") or url.startswith("http://")): #Validates the url given to check whether it starts with 'https://' or 'http://'
            print(name+", I guess that you have entered wrong url, kindly check that and enter again.\n") #Incase there is any mistake in the entered url, then it prompts the user to enter the url again
            continue #this skips the current  iteration for the loop and asks for the url again
        
        response=requests.get(url) #requests.get(url) sends a GET request to the entered url and tries to access the url entered, further the response variable stores the status code that is received back.            
        
        if response.status_code == 200: #if condition to check that whether the site is responsding not 
                print(name+", the url you entered is valid!\n") #Displaying message for the user to tell that the entered URL is valid
                print("The processing of QR image and text file has started...\n") #Now as the validity of URL is checked so the next stage begins where the generation of QR image and Text file is started
                time.sleep(2) #The code sleeps for 2 seconds so that the user gets a feel that the processing is going on
                break
        else:
                print(name+" the url that you entered returned an error. Please try again.")

    except requests.exceptions.RequestException as error: #This block catches, handles and displays any errors that occur when trying to access the URL
            print("Error occured: ",error) #Displays the error that occured for review
#End of while loop

#Creation of the QR code object
qr = qrcode.QRCode( #This is helpful incase of customizations
    version=1, #Specifies the size of the code
    error_correction=qrcode.constants.ERROR_CORRECT_L, #Defines the error correction level i.e. data that can be recovered incase the part of QR code is dirty / damaged 
    box_size=10, #Sets size of QR Code i.e. pixels, here 10x10
    border=4, #Sets white thickness around the QR code, here giving width of 4 boxes
)
qr.add_data(url) #Encoding the URL into the QR Code
qr.make(fit=True) #Making sure that the information is encoded into the QR code image
image=qr.make_image(fill_color="black", back_color="white") #Customizable options for color, here black and white
image.save("qrcode.png") #Saving the QR code image in .png format

print(name+", now that your QR code has been generated, do you want me to send it to your email?") #Asking user if he/she wants the qr code to be sent on their mail
print("Enter 'Yes' or 'No' as per your choice") #Asking user for their wish
consent=input() #They need to enter 'Yes' or 'No'

if consent == 'Yes': #If the user enters 'Yes' then the if block will be executed

    print("Provide me your mail id below") #Prompting user to enter their mail id
    receiver=input()
    sender="qrmadeeasy1@gmail.com"

    #making instance of the MIMEMultipart to hold different parts of mail, including the subject,body and attachments
    instance=MIMEMultipart()

    instance['From'] = sender #storing sender's mail address
    instance['To'] = receiver #storing receiver's mail address

    instance['Subject'] = name+", your QR Code is here!" #storing subject of the mail

    body = name+", we were glad that you chose us. We are attaching the QR Code as you requested." #body message added in the mail which is to be sent to the receiver

    instance.attach(MIMEText(body, 'plain')) #the body content is attached as plain text without any formatting

    file = "qrcode.png" #file that is to be sent in the mail
    attachment = open("D:\QR_Made_Easy\qrcode.png", "rb") #the file is opened in binary read mode as a qr code is generated as an image and aren't considered plain text as they contain pixels, colors; so the opening helps in ensuring that data is read correctly without any data loss or modification and in binary read mode all the bytes are preserved
    
    MIMEBase_instance = MIMEBase('application', 'octet-stream') #instance of MIMEBase class(part of email.mime package) for attachment, a MIMEBase object to handle binary data as email attachment. 'application' is primary type of data to be sent, used for data tha is not specifically text; the 'octet-stream' is subtype of 'application', it is generic binary data type and indicates that data format is unknown / arbitrary. 
    MIMEBase_instance.set_payload((attachment).read()) #used to add the content of the attachment i.e. QR code image to the MIMEBase_instance object inorder to send it as an email attachment. The set_payload is method of MIMEBase class used to store binary data with the MIMEBase_instance so that it becomes the payload of the attachment part in the email.
    encoders.encode_base64(MIMEBase_instance) #encoding of payload so that the it can be sent reliably over email protocols and making sure that it is compatible with email transmission stds.

    MIMEBase_instance.add_header('Content-Disposition', "attachment; filename=%s" %file) #add_header adds header to the MIMEBase_instance which defines the email client how to handle/display/interact with the attachment. Content-Disposition makes sure that the attachment appears as a separate downloadable file in the recipient’s email and not inline.

    instance.attach(MIMEBase_instance) #'instance.attach' is method of MIMEMultipart object and here it attaches qr code which is represented by the MIMEBase_instance

    SMTP_session = smtplib.SMTP('smtp.gmail.com', 587) #smtp session is created to connect wit the Gmail SMTP server, smtplib.SMTP is function in the 'smtplib' library. The 'smtp.gmail.com' specifies the SMTP server address for Gmail and 587 is port no. for Gmail SMTP server.
    SMTP_session.starttls() #enabling tls, Transport Layer Security encrypts the connection to protect data which is sent over the internet.

    SMTP_session.login(sender, "app_password") #replace the app password with the actual app password that was generated with your mail account. Authentication of sender with SMTP server is done to prevent spam and unauthorized email sending

    text = instance.as_string()

    SMTP_session.sendmail(sender, receiver, text)

    SMTP_session.quit()

    print(name+", We have shared the QR Code with you. Check your mail!")
else:
    print(name+", We're glad to provide you with our services!") #Incase user doesn't wants the QR code to be mailed on their mail id then else block will be executed 
