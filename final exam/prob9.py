import requests
import urllib.request as request
import cv2

# API 키
REST_API_KEY = '97cf548860dc985e3084d0e95518fa73'

# 이미지 파일 경로
image_url = 'https://t1.daumcdn.net/alvolo/_vision/openapi/r2/images/07.jpg'

# API 요청 URL
url = 'https://dapi.kakao.com/v2/vision/thumbnail/crop'

# 헤더 설정
headers = {
    'Authorization': f'KakaoAK {REST_API_KEY}'
}

# API 요청
response = requests.post(url, headers=headers, data={'image_url': image_url, 'width': 200, 'height': 200})
response_data = response.json()
print(response_data)

# 화면에 출력
thumb = "thumbnail.jpg"
request.urlretrieve(response_data["thumbnail_image_url"], thumb)
img = cv2.imread(thumb)
cv2.imshow("thumb", img)
cv2.waitKey(0)
cv2.destroyAllWindows()