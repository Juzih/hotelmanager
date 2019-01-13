import zifuchuan


def jiaozheng_ruzhu(a,b,c,d,e):# 校正入住数据格式

    zf = 1
    alen,blen,clen,dlen,elen = len(a),len(b),len(c),len(d),len(e)
    if (alen<=5)and(blen==18)and(clen==11)and(dlen==8)and(elen==8):
        zf = 1
        for i in range(alen):
            if zifuchuan.is_chienes(a[i]):zf=1
            else:
                zf=0
                return zf
        for i in range(blen):
            if zifuchuan.is_number(b[i]):zf=1
            else:
                zf=0
                return zf
        for i in range(clen):
            if zifuchuan.is_number(c[i]):zf=1
            else:
                zf=0
                return zf
        for i in range(dlen):
            if zifuchuan.is_number(d[i]):zf=1
            else:
                zf=0
                return zf
        for i in range(elen):
            if zifuchuan.is_number(e[i]):
                zf = 1
            else:
                zf = 0
                return zf
        if d<e:zf=1
        else:zf=0
    else:zf = 0

    return zf


def jiaozheng_xuding(a,b):  # 矫正续住数据格式
    zf = 1
    alen,blen = len(a),len(b)
    if alen!=3 or blen!=8:
        zf = 0
        return zf
    else:
        for i in range(alen):
            if zifuchuan.is_number(a[i]):zf=1
            else:
                zf=0
                return zf
        for i in range(blen):
            if zifuchuan.is_number(b[i]):zf=1
            else:
                zf =0
                return zf
    return zf


def jiaozheng_tuifang(a):  # 矫正退房数据
    zf = 1
    alen = len(a)
    if alen != 3:
        zf = 0
        return zf
    for i in range(alen):
        if zifuchuan.is_number(a[i]):
            zf = 1
        else:
            zf = 0
            return zf
    return zf
