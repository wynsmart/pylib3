import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(recipient, subject, html_body):

    gmail_user = 'wynsmart.test'
    gmail_pwd = 'wynsmart'
    me = '{}@gmail.com'.format(gmail_user)
    you = recipient

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = you
    msg.attach(MIMEText(html_body, 'html'))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(me, you, msg.as_string())
        server.close()
        return True
    except Exception as e:
        if __name__ == '__main__':
            print(e)
        return False


if __name__ == '__main__':
    send_email('wyns.smart@gmail.com', 'test message', '<strong>Job is done.</strong>')
    print('EMAIL SENT')
