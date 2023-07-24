

def fun(s):
    user = website = ext = ''
    try:
        user, web = s.split('@')
        website, ext = web.split('.')
    except:
        print(1)
        return False
    if user.replace('-', '').replace('_', '').isalnum() == False:
        print(2)
        return False
    elif website.isalnum() == False:
        print(3)
        return False
    elif len(ext) > 3:
        print(4)
        return False
    else:
        return True

email = 'chekwubeutomi@gmail.com'
result = fun(email)
print(result)
