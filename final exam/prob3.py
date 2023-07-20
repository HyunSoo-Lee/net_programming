import getpass
import paramiko
import time
import smtplib
from email.message import EmailMessage
import filetype

BUFF_SIZE = 65535

cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)

user = input("Username: ")
pwd = getpass.getpass("Password: ")

cli.connect("114.71.220.5", username=user, password=pwd)
channel = cli.invoke_shell()  # 새로운 셸 세션(channel) 생성

# 채널을 통해 명령어 전송
channel.send("mkdir 20201514\n")
time.sleep(0.5)
channel.send("cd 20201514\n")
time.sleep(0.5)     
channel.send("echo iot > iot.txt\n")
time.sleep(0.5)
channel.send("cat /proc/meminfo > mem.txt\n")
time.sleep(0.5)
channel.send("cd ..\n")
time.sleep(0.5)
channel.send("zip -r 20201514.zip 20201514\n")
time.sleep(0.5)
sftp = cli.open_sftp()
sftp.get("20201514.zip", "20201514.zip")
sftp.close()
cli.close()

output = channel.recv(BUFF_SIZE).decode() # 명령어 실행결과를 수신
print(output)

# 보내는 메일 서버
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

recipient = ["daeheekim@sch.ac.kr", "ninanooo@gmail.com"]

for addr in recipient:
    # 송신자, 수신자, 비밀번호
    sender = "oceanyum@gmail.com"
    recipient = addr
    password = "imsesiikegzljkjj"

    # 메시지 생성하기
    msg = EmailMessage()
    msg["Subject"] = "네트워크 프로그래밍 기말고사"
    msg["From"] = sender
    msg["To"] = recipient
    text = "네트워크 프로그래밍 기말고사 답안 제출합니다."
    msg.set_content(text)

    # 첨부할 파일 열기
    with open("20201514.zip", "rb") as f:
        zip_data = f.read()

    # add_attachment 함수를 이용해 파일 첨부. 파일 첨부시 첨부된 파일의 mime-type 지정
    msg.add_attachment(
        zip_data,
        maintype="application",
        subtype=filetype.guess_mime(zip_data),
        filename="20201514.zip",
    )

    # SMTP 객체 생성 후, 메시지 전송
    s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    s.ehlo()
    s.starttls()
    s.login(sender, password)
    s.send_message(msg)
    s.quit()
