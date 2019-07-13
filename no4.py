def belitelur(tanggal, uang):
    satutelur = 1500
    if tanggal > 1:
        prima = True
        for i in range(2,tanggal):
            if (tanggal % i) == 0: #prima
                    prima = False 
        if (prima):
            normal = uang/satutelur
            lusin = 12
            total = normal 
            for n in range (1,20): 
                if normal == (lusin * n):
                    bonus = 1 * n
                    total = normal + bonus
            print('Total telur:',int(total))

        elif (tanggal % 2) != 0: #ganjil
            normal = uang/satutelur
            kodi = 20
            total = normal
            for n in range (1,20): 
                if normal == (kodi * n):
                    bonus = 3 * n
                    total = normal + bonus
            print('Total telur:',int(total))
        
        else:
            pass

# contoh
belitelur(9,30000)