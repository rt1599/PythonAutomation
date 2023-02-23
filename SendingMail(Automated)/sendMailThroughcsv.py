import yagmail
import time
from datetime import datetime as dt
import pandas

sender="rishabh1599@gmail.com"
receiver="rishabh1599@gmail.com"

subject="Test Mail"
contents= """
Here is the content
"""
df =pandas.read_csv("Contacts.csv")
print (df) 
#yag=yagmail.SMTP(user=sender,password="yvzs tuzj sgiv bien")
#os.getenv()
#yag.send(to=receiver,subject=subject,contents=contents)
#print("Email sent!")