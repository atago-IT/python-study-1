x = 51
y = 50
z = 45

# すべてが奇数だった場合
if x%2 != 0 and y%2 != 0 and z%2 != 0:
    if y < x and z < x:
        print('xが一番大きな奇数です。')
    elif x < y and z < y:
        print('yが一番大きな奇数です。')
    else:
        print('zが一番大きな奇数です。')
 # xとzが奇数だった場合       
elif x%2 != 0 and y%2 == 0 and z%2 == 0:
    if  y < x and z < x:
        print('xが一番大きな奇数です。')
# yが奇数だった場合
elif  x%2 == 0 and y%2 != 0 and z%2 == 0:
    if x < y and z < y:
        print('yが一番大きな奇数です。')
# zが奇数だった場合
elif x%2 ==0 and y%2 == 0 and z%2 != 0:
    if x < z and y < z:
        print('zが一番大きな奇数です。')
# xとyが奇数だった場合
elif x%2 != 0 and y%2 != 0 and z%2 == 0:
    if x != y:
        if y < x:
            print('xが一番大きな奇数です。')
        else:
            print('yが一番大きな奇数です。')
# xとzが奇数だった場合
elif x%2 != 0 and y%2 == 0 and z%2 != 0:
    if x != z:
        if z < x:
            print('xが一番大きな奇数です。')
        else:
            print('zが一番大きな奇数です。')
# yとzが奇数だった場合
elif x%2 == 0 and y%2 != 0 and z%2 != 0:
    if y != z:
        if z < y:
            print('yが一番大きな奇数です。')
        else:
            print('zが一番大きな奇数です。')
else:
    print('正の変数x, y, zの中に奇数は存在しません。')
