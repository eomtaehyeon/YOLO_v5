# Overview.
- YOLO v5 코드를 직접 작성해보면서 Computer Vision에 대해 공부할 수 있습니다.
- 이 DataSet을 사용하여 사람 탐지 및 추적수행을 공부할 수 있습니다.

# Download Dataset.
- Udacity Self Driving Car Dataset
  - export(folder)
    - images (.jpg)
    - labels (class, x, y, width, height)
  - README.dataset.txt
  - README.roboflow.txt
  - data.yaml

## roboflow에 있는 publicdataset을 code로 다운로드 받기 / Jupyter에서 다운받기.
'''
curl -L "https://public.roboflow.com/ds/T0Vkvfrh2F?key=eTwXOGu8XG" > roboflow.zip; unzip roboflow.zip; rm roboflow.zip
'''

# Clone YOLO v5 at github.
- git clone으로 yolov5 가져오기
- yolov5를 위한 패키지 설치하기

## git clone 으로 yolov5 가져오기
- %cd : change dir

'''
cd /content (At Jupyter)
git clone https://github.com/ultralytics/yolov5.git
'''

## yolov5를 위한 패키지 설치하기
- %cd is the shell command to change the working directory.
'''
cd /yolov5 
pip install -r requirements.txt
'''

# Adjustment Dataset.

## Dataset/data.yaml을 조정을 위해 cat으로 확인
- cat is a shell command found in UNIX-based operating systems such as macOS and Linux.
- cat is a short form for concatenate.
'''
cat ./Dataset/data.yaml
'''
- train : trainset의 경로
- val : valset의 경로
- nc : class 갯수를 확인.
- name : class name 11개.

## train과 val 경로 수정.
- glob 모듈의 glob 함수는 사용자가 제시한 조건에 맞는 파일명을 리스트 형식으로 반환한다.
'''
from glob import glob  

img_list = glob('./dataset/export/images/*.jpg')
'''
- img_list에 img가 몇장인지 확인. 29800장 확인
'''
print(len(img_list))
'''

## dataset을 trainset과 valset으로 나누기.
'''
from sklearn.model_selection import train_test_split

train_img_list, val_img_list = train_test_split(img_list, test_size=0.2, random_state=2000)

print(len(train_img_list),len(val_img_list))
'''

## train_img, val_img 경로를 txt파일로 저장.

open()로 .txt파일에 join()를 이용해 리스트를 작성.
'''
f = open('/content/Dataset/train.txt', 'w')
f.write('\n'.join(train_img_list) + '\n')

f = open('/content/Dataset/val.txt', 'w')
f.write('\n'.join(val_img_list) + '\n')
'''

## data.yaml 파일을 수정.
'''
import yaml

with open('/content/Dataset/data.yaml', 'r') as f:
  data = yaml.load(f, Loader=yaml.FullLoader)    # .load(f) 가 오류로 .safe_load(f)를 사용.Loader argument 입력.

print(data)

data['train'] = '/content/Dataset/train.txt'
data['val'] = '/content/Dataset/val.txt'

with open('/content/Dataset/data.yaml', 'w') as f:
  yaml.dump(data, f)

print(data)
'''

# Model Training.
'''
cd ./yolov5/
'''
- Train YOLOv5s on COCO128 for 3 epochs
- python train.py --img 640 --batch 16 --epochs 3 --data coco128.yaml --weights yolov5s.pt
'''
python train.py --img 416 --batch 16 --epochs 50 --data YOLO_v5/dataset/data.yaml --cfg /models/yolov5s.yaml --weights yolov5s.pt --name Driving_yolov5s_results
'''

# 동영상
'''
python detect.py --source ../wearing_the_mask.mp4 --weights ../best.pt
...

- Results saved to yolov5\runs\detect\exp