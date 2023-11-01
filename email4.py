def valid_pass(func):
    def wrapper(*args, **kwargs):
        if len(args[0]) < 8:
            print("sxal (wrong) password")
            return None

        mecatar = 0
        poqratar = 0
        tiv = 0
        xary = 0
        for i in args[0]:
            if ord(i) >= 65 and ord(i) <= 90:
                mecatar += 1
            if ord(i) >= 97 and ord(i) <= 122:
                poqratar += 1
            if ord(i) >= 48 and ord(i) <= 57:
                tiv += 1
            if i in '!@#$%^&*':
                xary += 1
        if mecatar == 0 or poqratar == 0 or tiv == 0 or xary == 0:
            print("sxal (wrong) password")
            return None
        print("Good password")
        return func(*args, **kwargs)

    return wrapper


@valid_pass
def passs(kody):
    return kody


def valid_repet(funt):
    def wraper(*args, **kwargs):
        if args[0] != args[1]:
            print('ivalid')
            return None
        print("password good")
        return funt(*args, **kwargs)

    return wraper


@valid_repet
def refpass(kody, repkody):
    return repkody


def valid_number(func):
    def wrapper(*args, **kwargs):
        phone_num = args[0]
        while ' ' in phone_num:
            phone_num = phone_num.replace(" ", '')
            phone_num = phone_num.replace("-", ' ')

        if len(phone_num) != 12 and len(phone_num) != 9:
            print("Invalid")
            return None

        for i in phone_num:
            if (ord(i) >= 48 and ord(i) <= 57) or ord(i) == 43:
                if ord(i) == 43:
                    if phone_num.index(i) != 0:
                        print("Invalid")
                        return None
            else:
                print("Invalid")
                return None

        print("lav el hamar unes ")
        return func(*args, **kwargs)

    return wrapper


@valid_number
def phone(num):
    return num


def valid_email(func):
    def wrapper(*args, **kwargs):
        hasce = args[0].lower()

        countshnik = 0
        doticount = 0
        if " " in args[0]:
            return None
        if '@' in args[0] and '.' in args[0]:
            index_shnik = hasce.index('@')
            if '.' in args[0][index_shnik:]:
                for i in args[0][:index_shnik].lower():
                    if i not in 'abcdefghijklmnopqrstuvwxyz.':
                        return None
                indxe_dot = args[0][index_shnik:].index('.') + index_shnik

                for i in args[0][index_shnik + 1:indxe_dot]:
                    if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
                        countshnik += 1
                    else:
                        print("Invalid axper jan")
                        return None
                else:
                    if countshnik < 2 or countshnik > 7:
                        print("invalid axper jan")
                        return None

                for i in args[0][indxe_dot + 1:]:
                    if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
                        doticount += 1
                    else:
                        print("invalid axper jan")
                        return None
                else:
                    if doticount < 2:
                        print("invalid axper jan")
                        return None


            else:
                print("invalid axper jan")
                return None

        else:
            print("invalid axper jan")
            return None
        print('Good Email')
        return func(*args, **kwargs)

    return wrapper


@valid_email
def email(elpost):
    return elpost


def valid_nick(func):
    def wrapper(*args, **kwargs):
        if 5 > len(args[0]) or len(args[0]) > 20:
            print(" Invallid nick")
            return None

        if 'admin' == args[0].lower() or 'root' == args[0].lower():
            print("invalid nick")
            return None
        for i in args[0].lower():
            if ord(i) < 97 and ord(i) > 122:
                print("Invalid nick")
                return None

        print("Good nick")
        return func(*args, **kwargs)

    return wrapper


@valid_nick
def makanun(klichka):
    return klichka


flag = True
while flag:
    while flag:
        nikename = input("Pleas enter your nick \n")
        nikename = makanun(nikename)
        if nikename == None:
            print("If you want try again press 1")
            print("want to go out press 0")
            if int(input()):
                flag = True
            else:
                flag = False
                break
        else:
            break
    while flag:
        poshta = input("Enter your email \n")
        poshta = email(poshta)
        if poshta == None:
            print("If you want try again press 1")
            print("want to go out press 0")
            if int(input()):
                flag = True
            else:
                flag = False
                break
        else:
            break
    while flag:
        number = input("Enter Your Number If +374(you need 11 number if 099 you need 9  \n")
        number = phone(number)
        if number == None:
            print("If you want try again press 1")
            print("want to go out press 0")
            if int(input()):
                flag = True
            else:
                flag = False
                break
        else:
            break
    while flag:
        code = input("enter yor password\n")
        code = passs(code)
        if code == None:
            print("If you want try again press 1")
            print("want to go out press 0")
            if int(input()):
                flag = True
            else:
                flag = False
                break
        else:
            break
    while flag:
        pavtor = input("Password Repea \n")
        pavtor = refpass(code, pavtor)
        if pavtor == None:
            print("If you want try again press 1")
            print("want to go out press 0")
            if int(input()):
                flag = True
            else:
                flag = False
                break
        else:
            flag = False
            break


###

# def nickname_validation(func):
#     def wrapper(nick):
#         if len(nick) < 8 or len(nick) > 20:
#             raise ValueError("Wrong nick !")
#         return func(nick)
#     return wrapper
# @nickname_validation
# def nickname(nick):
#     return nick
#
#
# def auth(nick: str, email: str, phone: str, password: str, password_repeat: str) -> None:
#     nickname_input = nickname(nick)
#
#
# if __name__ == "__main__":
#     try:
#         auth("a", None, None, None, None)
#     except Exception as e:
#         print(e)

