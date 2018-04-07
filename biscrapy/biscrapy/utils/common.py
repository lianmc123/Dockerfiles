from hashlib import md5


def get_md5(value):
    m = md5()
    m.update(value.encode('utf-8'))
    return m.hexdigest()
