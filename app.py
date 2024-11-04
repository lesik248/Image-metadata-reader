from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import os
import zipfile
from io import BytesIO
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
diag = 15  # Diagonal for DPI calculation

mode_to_bits = {
    "1": 1,       # 1-bit pixels, black and white
    "L": 8,       # 8-bit pixels, grayscale
    "P": 8,       # 8-bit pixels, color-mapped
    "RGB": 24,    # 3x8-bit pixels, true color
    "RGBA": 32,   # 4x8-bit pixels, true color with alpha channel
    "CMYK": 32,   # 4x8-bit pixels, CMYK color model
    "YCbCr": 24,  # 3x8-bit pixels, YCbCr color model
    "LAB": 24,    # 3x8-bit pixels, L*a*b color space
    "HSV": 24     # 3x8-bit pixels, HSV color space
}

def image_info(image_path):
    img = Image.open(image_path)
    name = os.path.basename(image_path)
    width, height = img.size
    resolution = round((width ** 2 + height ** 2) ** (1 / 2) / diag, 2)
    depth_mode = img.mode
    depth = mode_to_bits.get(depth_mode, "Unknown")
    compression = img.info.get("compression", "N/A")
    
    return {
        "name": name,
        "size": f"{width}x{height}",
        "dpi": resolution,
        "color_depth": depth,
        "compression": compression
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'folder' not in request.files:
        return redirect(url_for('index'))
    
    file = request.files['folder']
    if file.filename == '':
        return redirect(url_for('index'))
    
    folder_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
    
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(folder_path)
    
    image_data = []
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.lower().endswith(('.jpg', '.gif', '.tif', '.bmp', '.png', '.pcx')):
                image_path = os.path.join(root, file_name)
                image_data.append(image_info(image_path))
    
    return render_template('index.html', image_data=image_data)

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
