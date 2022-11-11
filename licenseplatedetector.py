import os, glob
import time
import requests
import matplotlib
import matplotlib.pyplot as plt
import cv2
import json

matplotlib.use('Agg')

cwd = os.getcwd()
path = os.path.join("LP_DATASET", "BERGE", "Normal")

######## STEP 3 : Send the resulting files and evaluate the results  ########

file_list = glob.glob(os.path.join(path, '*.png'))
for file_item in file_list:
    # API documentation https://cloud.cognitechna.cz:8080/docs
    # Rate about 20 LPs/s
    # curl -X POST  -F "file=@img.jpg"  https://cloud.cognitechna.cz:8080/process_image_multipart?type=anpr.gate.europe
    # Non-blocking mode
    plt.cla()
    plt.ioff()
    plt.figure(figsize = (16,16), dpi= 256) # 2048 = 128 * 16
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

            resp_json = resp.json()[0]

            points = None

            # Report
            print(file_item, ":", resp_json['result']['status'])
            points = []
            for object in resp_json['result']['localizedObjectAnnotations']:
                points.append(object['points'])
                print('\n>>>>>>  CAMEA Detected License Plate:  ' + object['attributes']['ocr'][0])
                        # Show image
                img = cv2.imread(file_item)
                img_converted = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                
                plt.imshow(img_converted)
                for pt in points:
                    x1 = [pt[0][0], pt[1][0]]
                    y1 = [pt[0][1], pt[1][1]]
                    x2 = [pt[1][0], pt[2][0]]
                    y2 = [pt[1][1], pt[2][1]]
                    x3 = [pt[2][0], pt[3][0]]
                    y3 = [pt[2][1], pt[3][1]]
                    x4 = [pt[3][0], pt[0][0]]
                    y4 = [pt[3][1], pt[0][1]]
                    print(">>>>>>  LicensePlate Location:", pt, "\n")
                    plt.plot(x1, y1, x2, y2, x3, y3, x4, y4, color="green", linewidth=2)

                # plt.axis('off')

                plt.draw()
                plt.savefig(file_item + '-RESULT.jpg', bbox_inches='tight',transparent=True) # save the result
                plt.pause(0.1)
                plt.close()
                # time.sleep(1)




    except:
        print("ERROR: something went wrong!")
        pass

