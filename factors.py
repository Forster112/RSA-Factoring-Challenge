def factors(num):
    fac_num = []
    while num > 1:
        for i in range(1, num + 1):
            if num % i == 0:
                fac_num.append(i)
        break
    print("{}={}*{}".format(num, fac_num[-2], fac_num[1]))
