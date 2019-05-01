import sys
import smtplib

#######################################################################
#
# USAGE: python sendText.py phoneNumber message
#
#######################################################################
#
# Step 1: Disable 2-step verification:
# https://myaccount.google.com/security?utm_source=OGB&utm_medium=act#signin
#
# Step 2: Allow less secure apps
# https://myaccount.google.com/u/1/lesssecureapps?pli=1&pageId=none
# 
#######################################################################

# -------------------------- getCarrierGateway --------------------------------
def getCarrierGateway(carrier):
  switcher = {
    0: "txt.att.net",       # AT&T
    1: "pm.sprint.com",     # Sprint
    2: "tmomail.net",       # T-Mobile
    3: "vtext.com",         # Verizon
    4: "myboostmobile.com", # Boost Mobile
    5: "sms.mycricket.com", # Cricket
    6: "mymetropcs.com",    # Metro PCS
    7: "mmst5.tracfone.com",# Tracfone
    8: "email.uscc.net",    # U.S. Cellular
    9: "vmobl.com"          # Virgin Mobile
  }
  return switcher.get(carrier, "")

# ----------------------------- sendText --------------------------------------
def sendText(
  sender,
  password,
  smtp_server,
  phoneNum,
  text,
  carrier):

  carrierGateway=getCarrierGateway(carrier)
  if (len(carrierGateway) == 0):
    print("\nUnsupported Carrier!!\n\n")
    exit()

  recipient=phoneNum+"@"+carrierGateway
  print("To  : "+phoneNum)
  print("Text: "+text)

  confirm=input("\n\nsend? (y)? ")
  if ((len(confirm) != 0) and (confirm.lower() != 'y')):
    exit()

  try:
    server=smtplib.SMTP(smtp_server, 587)
    #server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, recipient, text)
    server.quit()
    print("\n\nMessage Sent!\n\n")
  except:
    print("Failed to connect to smtp server")


# ------------------------------- main ----------------------------------------
if (len(sys.argv) != 3):
  print("\nUSAGE: python sendText.py phoneNum message\n\n")
  exit()

phoneNum=sys.argv[1]
text=sys.argv[2]

PASSWORD="password"         # replace it with your password
SENDER="sender@gmail.com"   # replace it with your gmail account
SMTP_SERVER="smtp.gmail.com"
SPRINT=1

sendText(SENDER, PASSWORD, SMTP_SERVER, phoneNum, text, SPRINT)

#######################################################################
#
# Sample run:
#
# USAGE: python sendText.py phoneNumber message
#
# G:\>python sendText.py 1234567890 "hello world!"
# To     : 1234567890
# Message: hello world!
#
#
# send? (y)?
#
#
# Message Sent!
#


