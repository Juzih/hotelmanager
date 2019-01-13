def is_chienes(a):
    if '\u4e00' <= a<='\u9fff':
        return True
    else:
        return False

# 判断一个unicode是否是汉字
def is_chinese(uchar):
    if '\u4e00' <= uchar <= '\u9fff':
        return True
    else:
        return False


# 判断一个unicode是否是数字
def is_number(uchar):
    if '\u0030' <=  uchar <= '\u0039':
        return True
    else:
        return False


# 判断一个unicode是否是英文字母
def is_alphabet(uchar):
    if ('\u0041' <= uchar <= '\u005a') or ('\u0061' <= uchar <= '\u007a'):
        return True
    else:
        return False

