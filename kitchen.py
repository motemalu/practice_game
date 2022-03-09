def calc1(height) :
    kitchen=height/2+5
    return kitchen

def calc2(height) :
    kitchen=height-60-10
    return kitchen

def resultmessage(calc_kitchen,now_kitchen) :
    k_messages=(
    ('最適な高さです','スリッパの厚みを変えて微調整してみましょう'),
    ('目安より低いようです','腰痛に注意しましょう'),
    ('目安より高いようです','肩こりに注意しましょう')
 )

    if calc_kitchen == now_kitchen :
        print(k_messages[0][0])
        print(k_messages[0][1])
    elif calc_kitchen > now_kitchen :
        print(k_messages[1][0])
        print(k_messages[1][1])
    else :
        print(k_messages[2][0])
        print(k_messages[2][1])
     