import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
type(conn)
#<class 'smtplib.SMTP'>

conn.ehlo()
#(250, b'smtp.gmail.com at your service, [2a02:a31b:339:9e00:d127:8b73:c148:18d9]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')

conn.starttls()
#(220, b'2.0.0 Ready to start TLS')

conn.login('gani89@gmail.com', ‘<password>’)
conn.sendmail('gani.89@gmail.com', 'gani.89@gmail.com', 'Hi there..')
