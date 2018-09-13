import os
from email import generator
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

html_data = """\
        <html>
            <head></head>
            <body>
                <p> hello world </p>
            </body>
        </html>
        """

msg = MIMEMultipart('alternative')
msg['Subject'] = 'this is subject'
msg['From'] = 'from@gmail.com'
msg['To'] = 'to@gmail.com'
msg['Cc'] = 'cc@gmail.com'
msg['Bcc'] = 'bcc@gmail.com'
headers = {'X-Unsent': '1'}

for key in headers:
    value = headers[key]
    if value and not isinstance(value, str):
        value = str(value)
    msg[key] = value

part = MIMEText(html_data, 'html')
msg.attach(part)

outfile_name = os.path.join("data", "email_sample.eml")
with open(outfile_name, 'w') as outfile:
    gen = generator.Generator(outfile)
    gen.flatten(msg)

print("=========== DONE ============")
