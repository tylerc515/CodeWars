

def create_phone_number(numbers):
    
    phoneString = ''
    areaCode = ''
    prefix = ''
    lastFour = ''
    
    for i in numbers:
        phoneString += str(i)
    
    areaCode = '(' + phoneString[:3] + ') '
    prefix = phoneString[3:6] + '-'
    lastFour = phoneString[6:]
    
    phoneString = areaCode + prefix + lastFour

    return phoneString

formattedPhoneNumber = create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(formattedPhoneNumber)