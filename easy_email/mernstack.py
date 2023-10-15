from email_service import EmailService

# Recipients and email content
to_recipients = ['hirenjethva33@gmail.com']
subject = 'Exploring Exciting Opportunities - Versatile Software Engineer'
# Read the HTML content from an external file
with open('content/general.html', 'r', encoding='utf-8') as file:
    html_content = file.read()


email_service = EmailService()
email_message = email_service.message_setup(subject, html_content, 'html')
email_service.send_to(email_message, to_recipients)