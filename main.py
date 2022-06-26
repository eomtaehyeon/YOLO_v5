import glob
from sklearn.model_selection import train_test_split
import yaml

# glob 모듈의 glob 함수는 사용자가 제시한 조건에 맞는 파일명을 리스트 형식으로 반환한다.

img_list = glob.glob('./dataset/train/images/*.jpg', recursive=True)

# img_list에 img가 몇장인지 확인. 
print(len(img_list))

# dataset을 trainset과 valset으로 나누기.
train_img_list, val_img_list = train_test_split(img_list, test_size=0.2, random_state=2000)

print(len(train_img_list),len(val_img_list))

# train_img, val_img 경로를 txt파일로 저장.
f = open('./dataset/train.txt', 'w')
f.write('\n'.join(train_img_list) + '\n')

f = open('./dataset/val.txt', 'w')
f.write('\n'.join(val_img_list) + '\n')

# data.yaml 파일을 수정.
f = open('./dataset/data.yaml', 'r')

 # .load(f) 가 오류로 .safe_load(f)를 사용.Loader argument 입력.
data = yaml.load(f, Loader=yaml.FullLoader)   

print(data)

data['train'] = './dataset/train.txt'
data['val'] = './dataset/val.txt'

f =  open('./dataset/data.yaml', 'w')

yaml.dump(data, f)

print(data)