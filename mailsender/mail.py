import os
import smtplib
from mailsender.html_template import HTMLTemplate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class Mail:
    def __init__(self, template, sender):
        """
        Create a mail
            :param template: A template object
            :param sender: The sender credentials
        """
        if isinstance(template, HTMLTemplate):
            self.template = template
        elif isinstance(template, str):
            self.template = HTMLTemplate(template)
        else:
            raise "Invalid template!"

        self.smptName = sender['smtp'].split(':')[0]
        self.smtpPort = int(sender['smtp'].split(':')[1])

        self.senderMail = sender['mail']
        self.senderPass = sender['password']
        self.senderName = sender['name']

        pass

    def send_mail(self, recipients, subject, values, attachment):
        """
        Send the email to the recipient
            :param recipients: The recipient email or an array of recipients
            :param values: The values that will be used in for this mail in the template
            :param attachment: The path to the attached file
        """
        wasSent = False
        try:
            server = smtplib.SMTP(self.smptName, self.smtpPort)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(self.senderMail, self.senderPass)

            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = self.senderMail
            html = MIMEText(self.template.new_mail(values), 'html')

            dirname = os.path.dirname(__file__)
            path = os.path.join(dirname, attachment)
            filename = attachment.split('/')[-1]
            attachment = open(path, "rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                            "attachment; filename= %s" % filename)

            msg.attach(part)
            if isinstance(recipients, list):
                for recipient in recipients:
                    msg['To'] = recipient

                    msg.attach(html)
                    server.sendmail(self.senderMail, recipient,
                                    msg.as_string())
            elif isinstance(recipients, str):
                msg['To'] = recipients

                msg.attach(html)
                server.sendmail(self.senderMail, recipients, msg.as_string())
            else:
                raise "Invalid Recipient"

            wasSent = True
            server.quit()
        finally:
            return wasSent
