import sys
import cv2

if len(sys.argv)<3 :
    print('特徴量検出するファイルを2つ指定してください')
    sys.exit()

file1=sys.argv[1]
file2=sys.argv[2]

try :
    img1=cv2.imread(file1)
    img2=cv2.imread(file2)
    if (img1 is None) or (img2 is None) :
        raise ValueError('ファイル名が見つかりません。')

    detector=cv2.AKAZE_create()
    point1,desc1=detector.detectAndCompute(img1,None)
    point2,desc2=detector.detectAndCompute(img2,Nonde)

    matcher=cv2.BFMatcher(cv2.NORM_HAMMING,True)
    matches=matcher.match(desc1,desc2)
    img_match=cv2.drawMatches(img1,point1,img2,point2,matches,None,flag=2)




    cv2.imshow(file1+'<-->'+file2,img_match)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



except ValueError as e :
    print(e)

except :
    import traceback
    traceback.print_exc()