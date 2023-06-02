import smtplib
toaddrs = 'ReciverAddress@gmail.com'  # TARGET EMAIL ADDRESS GOES HERE
fromaddrs = 'Example@gmail.com'         # YOUR EMAIL ADDRESS GOES HERE

message = 'WE GO TO MIAMI BABY!'        # THE MESSAGE YOU WANT TO SEND GOES HERE 
with smtplib.SMTP('smtp.gmail.com', '587') as smtpserver:
  smtpserver.ehlo()
  smtpserver.starttls()
  smtpserver.ehlo()
  smtpserver.login('example@gmail.com', 'APP PASSWORD SHOULD BE 16 CHAR')  #YOUR EMAIL ADDRESS GOES FIRST, THEN AN "APP" GMAIL PASSWORD
  for i in range(30):                             # THE NUMBER OF EMAILS YOU WANT TO SEND
    smtpserver.sendmail(fromaddrs, toaddrs, message)
    print(i)
