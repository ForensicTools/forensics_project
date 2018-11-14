import re

def preformatPhone(phone):

    phone = re.sub('/[\s+\-()]*/g', '', phone)

    if len(phone) == 11 and phone[0] == '1':
        phone = phone[1::]

    return phone


data = preformatPhone("phone number here")
print(data)
