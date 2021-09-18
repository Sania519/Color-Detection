import pandas as pd
import cv2
global xpos, ypos, cname, r, g, b, clicked
clicked = False

img_path = input("Enter path: ")
#img_path = "Color detection/pic1.jpg"
csv_path = "colors.csv"

img = cv2.imread(img_path)
img = cv2.resize(img,(500,500))

index = ["Color", "Color_name", "Hex", "R", "G", "B"]
color_data = pd.read_csv(csv_path, names=index, header=None)
print(color_data)

def get_color(r, g, b):
        min = 1000
        cname = ""
        for i in range(len(color_data)):
            sum = abs(r - color_data.loc[i, 'R']) + abs(g - color_data.loc[i, 'G']) + abs(b - color_data.loc[i, 'B'])
            if sum<=min:
                min = sum
                cname = color_data.loc[i, "Color_name"]

        return(cname)



def draw_function(event, x, y, flags, params):
        global xpos, ypos, r, g, b, clicked
        if event == cv2.EVENT_LBUTTONDBLCLK:
            clicked = True
            b, g, r= img[y, x]
            print(b, g, r)
            b = int(b)
            g = int(g)
            r = int(r)
            xpos = x
            ypos = y
            cname = get_color(r, g, b)
            print(cname)


cv2.namedWindow("Image")
cv2.setMouseCallback("Image", draw_function)

while(True):
        cv2.imshow("Image", img)
        if clicked:
            cv2.rectangle(img,(20, 20), (300, 60), (b, g, r), -1)
            text = get_color(r, g, b)
            cv2.putText(img, text,org=(22, 50), fontFace=2,fontScale=0.8, color=(0,0,0), thickness=1, lineType= cv2.LINE_AA)
            if r + g + b < 600:
                cv2.putText(img, text, org=(22, 50), fontFace=2, fontScale=0.8, color=(255, 255, 255), thickness=1,
                                lineType=cv2.LINE_AA)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break


cv2.destroyAllWindows()

