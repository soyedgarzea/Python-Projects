from pathlib import Path
import smtplib
from email.message import EmailMessage
from string import Template
from sys import path

root = path[0]

html = Template(Path(f'{root}/index.html').read_text())

email = EmailMessage()
email['from'] = 'Edgar Zea'
email['to'] = 'email@test.com'
email['subject'] = 'Email Tester'
email.set_content(html.substitute(name='Test'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email@test.com', 'password')
    smtp.send_message(email)
    print('all good')
