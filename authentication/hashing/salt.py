import random
import string
import hashlib


def make_salt():
    return ''.join(random.choice(string.hexdigits) for x in range(8))


def make_pw_hash(name, pw):
    salt = make_salt()
    my_hash = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (my_hash, salt)


print(make_pw_hash('maize', '_Cipher96'))
