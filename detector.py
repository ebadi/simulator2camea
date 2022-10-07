import os, glob
import time

import requests
import matplotlib.pyplot as plt
import cv2

# Non-blocking mode
plt.ion()
plt.show()
plt.figure(figsize = (10,8))

# List images in
import os
cwd = os.getcwd()

# path = os.path.join(cwd,"LP_DATASET", "CAMEA")
# file_list = glob.glob(os.path.join(path, '*.jpg'))

# path = os.path.join(cwd,"LP_DATASET","INFOTIV", "png")
# file_list = glob.glob(os.path.join(path, '*.png'))

path = os.path.join(cwd,"LP_DATASET", "BERGE", "Normal")
file_list = glob.glob(os.path.join(path, '*.png'))

for file_item in file_list:

    # API documentation https://cloud.cognitechna.cz:8080/docs
    # Rate about 20 LPs/s
    # curl -X POST  -F "file=@img.jpg"  https://cloud.cognitechna.cz:8080/process_image_multipart?type=anpr.gate.europe

    try:
        with open(file_item, 'rb') as f:
            url = 'https://cloud.cognitechna.cz:8080/process_image_multipart?type=anpr.gate.europe'
            files = {'file': f}

            resp = requests.post(url, files=files)

            # Check if response OK
            if resp.status_code != requests.codes.ok:
                print(resp.text)
                print(resp)
                # exit(1)

            #
            resp_json = resp.json()[0]

            points = None

            # Report
            print(file_item)
            print(resp_json)
            print('* ' + resp_json['result']['status'])
            points = []
            for object in resp_json['result']['localizedObjectAnnotations']:
                points.append(object['points'])

                print('+ ' + object['attributes']['ocr'][0])


        # Show image
        img = cv2.imread(file_item)
        img_converted = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        plt.cla()

        for pt in points:
            x1 = [pt[0][0], pt[1][0]]
            y1 = [pt[0][1], pt[1][1]]
            x2 = [pt[1][0], pt[2][0]]
            y2 = [pt[1][1], pt[2][1]]
            x3 = [pt[2][0], pt[3][0]]
            y3 = [pt[2][1], pt[3][1]]
            x4 = [pt[3][0], pt[0][0]]
            y4 = [pt[3][1], pt[0][1]]
            print("dx", pt[0][0]-pt[1][0], "dy", pt[0][1]-pt[2][1])
            plt.plot(x1, y1, x2, y2, x3, y3, x4, y4, color="green", linewidth=2)

        plt.axis('off')
        plt.imshow(img_converted)
        plt.draw()
        plt.savefig(file_item + '-RESULT.jpg') # save the result
        plt.pause(0.5)
        # time.sleep(1)
    except:
        pass

