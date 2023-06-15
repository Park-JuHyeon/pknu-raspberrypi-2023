import cv2

# 01. 일반이미지
# img = cv2.imread('./Day07/test.jpg')

# 02. 흑백이미지
# img = cv2.imread('./Day07/test.jpg', cv2.IMREAD_GRAYSCALE)

# 04. 원본을 그대로 두고 흑백을 추가
img = cv2.imread('./Day07/test.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                
# 03. 이미지 사이즈 축소
# img_small = cv2.resize(img, (200, 120))

# 05. 이미지 자르기
height, width, channel = img.shape
print(height, width, channel)

img_crop = img[:, :int(width / 2)]  # height, width
gray_crop = gray[:, :int(width / 2)]

# 06. 이미지 블러처리
img_blur = cv2.blur(img_crop, (10,10))

cv2.imshow('Blur half', img_blur)
cv2.imshow('Gray', gray_crop)

cv2.waitKey(0)
cv2.destroyAllWindows()