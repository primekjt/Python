# 야구게임
def baseball(target_num, check_num):
    s = 0
    b = 0
    idx_x = 0
    idx_y = 0
    for x in target_num:
        idx_y = 0   # 초기화
        for y in check_num:
            if x == y:
                if idx_x == idx_y:
                    s = s + 1
                    print("*** x is %d(%d), y is %d(%d) : Stlike" % (x, idx_x, y, idx_y))
                else:
                    b = b + 1
                    print("*** x is %d(%d), y is %d(%d) : Ball" % (x, idx_x, y, idx_y))
            print("x is %d(%d), y is %d(%d) : %dS, %dB" % (x, idx_x, y, idx_y, s, b))
            idx_y = idx_y + 1
        idx_x = idx_x + 1
    print("result : %d Stlike, %d Ball" % (s, b))
    return 0

target_num = [1, 2, 3]
check_num = []


a = input("★본인의 숨김 숫자를 입력하세요 : ")
target_num[0] = int(a[0])
target_num[1] = int(a[1])
target_num[2] = int(a[2])
# print(target_num)
a = input("★확인할 숫자를 입력하세요 : ")
max = len(a)

# print(max)
i = 0
for i in range(max):
    check_num.append(int(a[i]))
# print(check_num)

baseball(target_num, check_num)
