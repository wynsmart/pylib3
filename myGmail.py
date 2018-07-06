import smtplib


def send_email(recipient, subject, body):

    gmail_user = 'wynsmart.test'
    gmail_pwd = 'wynsmart'
    FROM = '{}@gmail.com'.format(gmail_user)
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = "\From: {}\nTo: {}\nSubject: {}\n\n{}".format(
        FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('EMAIL SENT')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    send_email('wyns.smart@gmail.com', 'test message', 'Job is done.')
