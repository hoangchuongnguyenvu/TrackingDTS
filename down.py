import os
import requests
import zipfile
from tqdm import tqdm

# Tạo thư mục để lưu dataset
os.makedirs('OTB', exist_ok=True)

# Link download OTB-100
otb_url = "http://cvlab.hanyang.ac.kr/tracker_benchmark/seq/tb100.zip"
output_path = 'OTB/tb100.zip'

# Tải file với thanh tiến trình
print("Đang tải OTB dataset...")
response = requests.get(otb_url, stream=True)
total_size = int(response.headers.get('content-length', 0))

with open(output_path, 'wb') as file, tqdm(
    desc=output_path,
    total=total_size,
    unit='iB',
    unit_scale=True,
    unit_divisor=1024,
) as pbar:
    for data in response.iter_content(chunk_size=1024):
        size = file.write(data)
        pbar.update(size)

# Giải nén file
print("\nĐang giải nén...")
with zipfile.ZipFile(output_path, 'r') as zip_ref:
    zip_ref.extractall('OTB')

print("Hoàn thành!")