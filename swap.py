from PIL import Image

# 이미지 열기
image = Image.open("./out/demo_12/envmap/padded_demo_12_ev-00.png")

# 크기 정보 가져오기
width, height = image.size

# 이미지 좌우 절반 나누기
left_half = image.crop((0, 0, width // 2, height))
right_half = image.crop((width // 2, 0, width, height))

# 좌우 반전해서 새로운 이미지 생성
swapped_image = Image.new("RGB", (width, height))
swapped_image.paste(right_half, (0, 0))
swapped_image.paste(left_half, (width // 2, 0))

# 결과 저장
swapped_image.save("./out/demo_12/raw/swapped_output.png")
swapped_image.show()  # 확인용