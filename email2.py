import smtplib

to = "sender@email.com"

content='''Your Message'''

# content="https://ceziot.tech"

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email@demo.com', 'Password')
    server.sendmail('email@demo.com', to, content)
    server.close()

sendEmail(to, content)
