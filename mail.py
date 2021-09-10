import smtplib, ssl

class Email():
    def __init__(self, sender_email, password, receiver_email):
        self.sender = sender_email
        self.password = password
        self.rect = receiver_email
    
    def sendMail(self, title, content):
        if title[0:8] == "Subject: ":
            title = title[8:]
        message = f"""\
Subject: {title}

{content}
        """

        context = ssl.create_default_context()
        self.email = smtplib.SMTP("smtp.gmail.com", 587)
        self.email.ehlo()  
        self.email.starttls(context=context)
        self.email.ehlo()
        self.email.login(self.sender, self.password)
        self.email.sendmail(self.sender, self.rect, message.encode("UTF-8"))