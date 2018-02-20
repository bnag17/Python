import smtplib
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("nagesh.17cs@cmr.edu.in","8008366752anu")
msg="hello world"
s.sendmail("nagesh.17cs@cmr.edu.in","bellamkondanagesh1648@gmail.com",msg)
print("succces")
s.quit()
