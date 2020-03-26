'''
1. 특정 숫자를 포함해서 로또 번호를 생성해주는 기능
2. 특정 숫자를 제외해서 로또 번호를 생성해주는 기능
3. 정해진 자리수만큼 연속 숫자를 포함하는 번호를 생성하는 기능
'''

import numpy

def make_lotto_number(**kwargs):
    rand_number = numpy.random.choice(range(1, 46), 6, replace=False)
    rand_number.sort()

    #최종 로또 번호가 완성될 변수
    lotto = []

    if kwargs.get("include"):
        include = kwargs.get("include")
        lotto.extend(include)

        cnt_make = 6 - len(lotto)

        for _ in range(cnt_make):
            for j in rand_number:
                if lotto.count(j) == 0:
                    lotto.append(j)
                    break

    else:
        lotto.extend(rand_number)

    

    return lotto


print(make_lotto_number(include=[1 ,2]))