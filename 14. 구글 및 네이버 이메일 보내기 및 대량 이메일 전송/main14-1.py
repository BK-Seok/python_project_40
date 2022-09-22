import smtplib
from email.mime.text import MIMEText

send_email = "idev0323@naver.com"
send_pwd = "Qlalf**0323"
recv_email = "qudrlfbbung@naver.com"

smtp_name = "smtp.naver.com" 
smtp_port = 587

text = """
여러줄
"""
msg = MIMEText(text)

msg['Subject'] ="메일제목은 여기에 넣습니다"
msg['From'] = send_email
msg['To'] = recv_email
print(msg.as_string())

s=smtplib.SMTP( smtp_name , smtp_port )
s.starttls()
s.login( send_email , send_pwd )
s.sendmail( send_email, recv_email, msg.as_string() )
s.quit()