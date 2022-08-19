# pip install qrcode

import qrcode
qr_data = 'www.naver.com' # www.naver.com 문자열을 qr_data에 바인딩
qr_img = qrcode.make(qr_data) # 이미지를 만들어 qr_img 변수에 바인딩

# 4. QR코드 생성기 폴더 하위 경로에 www.naver.com.png로 바인딩
save_path = '4. QR코드 생성기\\'+qr_data+'.png'
qr_img.save(save_path)