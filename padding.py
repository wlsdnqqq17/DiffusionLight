import sys
import os
from PIL import Image, ImageOps

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <input_image_path>")
        sys.exit(1)

    input_path = sys.argv[1]

    folder = os.path.dirname(input_path)
    basename = os.path.basename(input_path)
    name, ext = os.path.splitext(basename)

    # 저장 폴더: imgs/demo_1/
    output_folder = os.path.join(folder, name)
    os.makedirs(output_folder, exist_ok=True)

    # 저장 경로: imgs/demo_1/padded_demo_1.jpg
    output_path = os.path.join(output_folder, f"padded_{name}{ext}")

    desired_size = 1024
    padding_color = (0, 0, 0)

    img = Image.open(input_path)

    w, h = img.size
    if w >= h:
        new_w = desired_size
        new_h = int(h * (desired_size / w))
    else:
        new_h = desired_size
        new_w = int(w * (desired_size / h))
    img_resized = img.resize((new_w, new_h), resample=Image.Resampling.LANCZOS)

    padded_img = ImageOps.pad(img_resized, (desired_size, desired_size), color=padding_color, centering=(0.5, 0.5))

    padded_img.save(output_path)
    print(f"Saved padded image at {output_path}")
