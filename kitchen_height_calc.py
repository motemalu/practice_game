import sys
import kitchen

if len(sys.argv)<2 :
    print('表示したい名前を指定してください。')
    sys.exit()
my_name=sys.argv[1]

#計算結果の表示メッセージ
kitchen_message=my_name+'さんの最適なキッチンの高さ（そのn）は'

#身長と今のキッチンの高さ情報をひとまとめにする
kitchen_elements=[0.0,0.0]
kitchen_messages=['身長(cm)','今のキッチンの高さ(kg)']

#2つの項目を入力
num=0
for entry in kitchen_messages :
    kitchen_elements[num]=input(entry+'を入力してください：')
    num=num+1

print('-------')

try:

    #それぞれの高さ情報を文字から浮動小数点に変換
    human_height=float(kitchen_elements[0])
    kitchen_height=float(kitchen_elements[1])

    print(f'あなたの身長は{human_height}cmです。')
    print('--------')

    #計算結果の表示メッセージ
    kitchen_message='最適なキッチンの高さ(そのn)は'

    #キッチンの高さの目安計算（その1）
    #キッチンの高さ＝身長[cm]÷2+5cm
    kitchen1=kitchen.calc1(height=human_height)
    message=kitchen_message.replace('そのn','その1')
    print(f'{message}{kitchen1}cmです。')

    #今のキッチンの高さと比較し目安と同じなら適合
    #それ以外なら高い・低いと表示する
    #if kitchen1 == kitchen_height :
        #print('最適な高さです。')
    #elif kitchen1>kitchen_height :
        #print('目安よりも低いようです')
        #print('腰痛に注意しましょう')
    #else:
        #print('目安より高いようです')
        #print('肩こりに注意しましょう')

    kitchen.resultmessage(calc_kitchen=kitchen1,now_kitchen=kitchen_height)

    print('-------')
    #キッチンの高さの目安計算（その2）
    #キッチンの高さ=肘高cm-10cm
    #肘高はおおよそ「身長[cm]-60cm」と言われています。
    kitchen2=kitchen.calc2(height=human_height)
    message=kitchen_message.replace('そのn','その2')
    print(f'{message}{kitchen2}cmです。')

    #今のキッチンの高さと比較し目安と同じなら適合
    #それ以外なら高い・低いと表示する
    #if kitchen2 == kitchen_height :
        #print('最適な高さです。')
    #elif kitchen2>kitchen_height :
       # print('目安よりも低いようです')
       # print('腰痛に注意しましょう')
    #else:
        #print('目安より高いようです')
        #print('肩こりに注意しましょう')

    kitchen.resultmessage(calc_kitchen=kitchen2,now_kitchen=kitchen_height)

    print('-------')

except ValueError as e :
    print('身長または今のキッチンの高さを見直してください')
    print(e)
except:
    import traceback
    traceback.print_exc()
