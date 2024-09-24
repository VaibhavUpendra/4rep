import yagmail
import os
from dotenv import load_dotenv

load_dotenv()


sender = "nuclearweapon211@gmail.com"
receiver = "ahhkvdqhb@10mail.org"
subject = 'Test Mail using Python'
contents = '''
This is the comment portion of the mail
Suresh Babu is a Hardworking Man
'''
yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
yag.send(to=receiver,subject=subject,contents=contents)
print("Email sent!")