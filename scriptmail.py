import smtplib
import getpass
import os



smtp_object = smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()
smtp_object.starttls()


email = getpass.getpass("Enter your email: ")
    #password = (open("p.txt","r"))
password = getpass.getpass("Enter the Gmail Application Password: ")
smtp_object.login(email,password.readline())

print("__________   WELCOME   ___________")

select = input("1/2/3 ?")
while (select <= 3):

       
    print("1. SEND EMAIL")
    print("2. CHECK EMAILS")

    print("3 EXIT")
    select = input("1/2/3 ?")

    if select == 3:
        break
    if select == 2:
        pass
            #from_address = getpass.getpass("Enter your email: ")
            #to_address = getpass.getpass("Enter the email of the recipient: ")
            #subject = input("Enter the subject line: ")
            #message = input("Type out the message you want to send: ")
            #msg = "Subject: " + subject + '\n' + message
            #smtp_object.sendmail(from_address,to_address,msg)
    if select == 1:
        pass
    else:
        print(select + "Is not a valid operation")
        select == 0
smtp_object.quit()        
    




    
