import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    plen = int(input("Enter a Password Length \n"))

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    ### Type 1
    # random.shuffle(s)
    #
    # print("Your password is :")
    # pwd = "".join(s[0:plen])
    # print(pwd)

    ### Type 2
    pwd = "".join(random.sample(s,plen))
    print("Your password is :")
    print(pwd)





