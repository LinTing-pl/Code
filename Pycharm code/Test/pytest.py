print(int('1111111111111111', 2))
# 55296 55297 55298
# listerror = []
# for i in range(55296, 65536):
#     try:
#         print(chr(i), '  ', i)
#     except UnicodeEncodeError:
#         listerror.append(i)
#         i += 1
# print(listerror)
# '\ud800' '\udfff'
# print(57344 - 55296)
# print(ord('\udbed'))
# print(ord('\ud8f1'))
# print(int('\udfff',16)-int('\ud800',16))
import sys
print(sys.stdout.encoding)
