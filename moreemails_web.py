import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

email = EmailMessage()
email['from'] = 'Kristen Gillen'
email['to'] = 'kristen.k.gillen@gmail.com'
email['subject'] = 'I sent this from a python file!'

html = Template(Path('index.html').read_text())

email.set_content(html.substitute({'name': 'TinTin'}), 'html') #can have multiple library entries from html file here

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('hidden', 'hidden')
  smtp.send_message(email)
  print('all good boss!')