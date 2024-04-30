import smtplib,ssl


def send_email(message):
    
   



    host = "smtp.gmail.com"
    port= 465

    username = "llmappdev@gmail.com"
    with open("password.txt" , "r") as file:
        password = file.readline()

    receiver1= "llmappdev@gmail.com"
 

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username, password)
        server.sendmail(username,receiver1,message)
     #  server.sendmail(username,receiver2,message)






