import time, random

ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')

def makeNew():
    u''' ��������µ�18Ϊ���֤���� '''
    t = time.localtime()[0]
    x = '%02d%02d%02d%04d%02d%02d%03d' %(random.randint(10,99),
                                        random.randint(01,99),
                                        random.randint(01,99),
                                        random.randint(t - 80, t - 18),
                                        random.randint(1,12),
                                        random.randint(1,28),
                                        random.randint(1,999))
    y = 0
    for i in range(17):
        y += int(x[i]) * ARR[i]

    return '%s%s' %(x, LAST[y % 11])

def isTrue():
    u''' ��֤���֤�����Ƿ���ʵ���� '''
    print u'���������֤����'
    x1 = raw_input('?')

    xlen = len(x1)
    if xlen != 18 and xlen != 15:
        return u'���֤���볤�ȴ���'

    try:
        if xlen == 18:
            x2 = x1[6:14]
            x3 = time.strptime(x2, '%Y%m%d')
            if x2 < '19000101' or x3 > time.localtime():
                return u'ʱ����󣬳��������ʱ�䷶Χ'
        else:
            x2 = time.strptime(x1[6:12], '%y%m%d')
    except:
        return u'ʱ����󣬷ǺϷ�ʱ��'

    if xlen == 18:
        y = 0
        for i in range(17):
            y += int(x1[i]) * ARR[i]

        if LAST[y % 11] != x1[-1].upper():
            return u'��֤�����'

    return u'YES'

def old2new():
    u''' 15λ���֤����ת��Ϊ18λ���֤���� '''
    print u'������15λ�����֤����'
    x1 = raw_input('?')
    if len(x1) != 15:
        return u'���֤��������������֤���볤�Ȳ�Ϊ15λ'

    oldcard = '%s19%s' %(x1[:6], x1[6:])
    y = 0
    for i in range(17):
        y += int(oldcard[i]) * ARR[i]

    return '%s%s' %(oldcard, LAST[y % 11])