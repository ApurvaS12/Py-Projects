import smtplib , ssl

host = "smtp.gmail.com"  

port = 465

username = "llmappdev@gmail.com"
password = "fbmlikbfgudexpqn"

receiver = "llmappdev@gmail.com"

message = """\
Subject: Hi!
hello, 
how are you?
bye"""
context = ssl.create_default_context()

with smtplib.SMTP_SSL(host, port, context= context)as server:
    server.login(username, password)
    server.sendmail(username, receiver, message )

