def string2bit(m):
    output = []
    result = []
    a = [ord(i) for i in m]
    num = 0
    for i in range(len(a)):
        b = bin(a[i]).replace('0b', '')
        lenth = len(b)
        space = 8 - lenth % 8
        c = f'{0:0{space}}{b}'
        for j in range(len(c)):
            num += 1
            result.append(int(c[j]))
            while i == len(a) - 1 and j == len(c) - 1 and num < 64:
                num += 8
                result.extend([0, 0, 1, 1, 0, 0, 0, 0])
            if num >= 64:
                output.append(result)
                num = 0
                result = []
    return output


a='123456789'
print(string2bit(a))
print(len(string2bit(a)[1]))
print(bin(ord(' ')))
