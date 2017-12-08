# MIME    Mail Interchange Message Extension format

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#import mhtpwd

#-- End SendEmailMsgWithAttachment -------------------------------------------------------
def SendEmailMsgWithAttachment(fromuser, tolist, subject, message, \
                               attachmentfilename="No Filename.txt", \
                               attachmentContent="No Content"):

    msg = MIMEMultipart()
    msg.attach(MIMEText(message))

    msg['From'] = fromuser
    msg['To'] = ', '.join(tolist)
    msg['Subject'] = subject

    #attachment = MIMEText(open(attachmentfilename,"r").read())
    attachment = MIMEText(attachmentContent)
    attachment.add_header('Content-Disposition', 'attachment', filename=attachmentfilename)
    msg.attach(attachment)

    smtpObj = smtplib.SMTP('smtp.office365.com', 587)
    smtpObj.starttls()
    smtpObj.login('username', "password")
    smtpObj.sendmail(fromuser, tolist, msg.as_string())
    smtpObj.quit()

    return

def SendEmailMsgWithAttachmentFilename(fromuser, tolist, subject, message, attachmentfilename):

    SendEmailMsgWithAttachment(fromuser, tolist, subject, message, \
                               attachmentfilename, \
                               open(attachmentfilename, "r").read())
    return

#-- End SendEmailMsgWithAttachment -------------------------------------------------------

if __name__ == "__main__":


    print("Sending message with attachment")


    SendEmailMsgWithAttachmentFilename('angh@spu.edu', \
                           ['angh@spu.edu'], \
                           'Secret Santa Homies Group 2017', \
                           'raw line.txt.', \
                           'sendemailMIMEmsg.py')
    print("Done")

