num_teste = int(input())
for c in range (0, num_teste):
    C = int(input())
    XM, YM, ZM, WM = input().split()
    XM = int(XM)
    YM = int(YM)
    ZM = int(ZM)
    WM = int(WM)
    B = int(input())
    if ZM != B and ZM != C and ZM != YM and ZM != WM and XM != B and XM != C and XM != YM and XM != WM and YM != C and YM != B and YM != ZM and YM != XM and WM != C and WM != B and WM != ZM and WM != XM and C != XM and C != YM and C!=ZM and C != WM and B != XM and B != YM and B !=ZM and B != WM and C + XM + YM + ZM + WM + B == 21 and C != 0 and XM != 0 and YM != 0 and ZM != 0 and WM != 0 and B != 0:
        if C + B == 7 and WM + YM == 7 and XM + ZM == 7:
            print('SIM')
        else:
            print('NAO')   
    else:
        print('NAO')


