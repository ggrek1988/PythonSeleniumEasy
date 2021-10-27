import re
phone = str('48 123456345')
print phone
#validacja telefonu
if re.match(r"(^[0-9]{2}(?: [0-9]{9})?$)", phone): # if the email is valid
    print("dobry telefon!")
else:
    print("zly telefon!") # or raise exception to stop execution