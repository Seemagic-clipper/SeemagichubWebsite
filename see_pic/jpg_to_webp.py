from PIL import Image
import os

# 设置输出 WebP 图片质量（0~100）
QUALITY = 90

# 获取当前目录
current_dir = os.getcwd()

# 遍历当前目录下所有文件
for filename in os.listdir(current_dir):
    if filename.lower().endswith(".jpg"):
        jpg_path = os.path.join(current_dir, filename)
        webp_filename = os.path.splitext(filename)[0] + ".webp"
        webp_path = os.path.join(current_dir, webp_filename)
        
        # 打开 JPG 并保存为 WebP
        with Image.open(jpg_path) as img:
            img.save(webp_path, "webp", quality=QUALITY)
        
        print(f"Converted: {filename} -> {webp_filename}")

print("All JPG images have been converted to WebP.")
