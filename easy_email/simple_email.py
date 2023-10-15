from email_service import EmailService

# Recipients and email content
to_recipients = ['mamtag962000@gmail.com']
subject = 'Test Email'
message = 'Customizable message content.\nHello, this is the email body.'

email_service = EmailService()
email_message = email_service.message_setup(subject, message, 'plain')
email_service.send_to(email_message, to_recipients)