# Importing all the required Python files and library
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date
from api import api_news
from email_html import embeded_image
from config import *
import smtplib

# Storing Email Subject with today's Date
subject = f"Your Automated News for {date.today()}"

# Connecting to the server and logging-in
agent = smtplib.SMTP_SSL("smtp.gmail.com", 465)
agent.login(sender_email,sender_email_app_password)


for email in client_details.keys():
    client = client_details[email]
    em = MIMEMultipart()
    em["From"] = sender_email
    em["To"] = email
    em["Subject"] = subject

    # Attaching and mailing news for individual News-letter Client
    em.attach(MIMEText(embeded_image(api_news(client["topic"])), "html"))
    agent.sendmail(sender_email, email, em.as_string())

    print( f"Mail send to {client['name']} ({email}) about {client['topic']}\n")

print("\nTask Finshed")