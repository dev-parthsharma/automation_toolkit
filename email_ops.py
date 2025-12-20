from email.message import EmailMessage
from smtplib import SMTP

msg = EmailMessage()

msg["From"] = "sender's gmail"
msg["To"] = "receiver's gmail"
msg["Subject"] = "your subject"

msg.set_content("your content")

try:
    smtp = SMTP("smtp.gmail.com", 587)

    smtp.starttls()
    smtp.login("your gmail", 'your password')
    smtp.send_message(msg)
    smtp.quit()
    print("SMTP connected sucessfully")


except Exception as e:
    print(f"Error: {e}")
