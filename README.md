# Image Metadata Reader

This project is a web-based application that allows users to upload a `.zip` file containing images and view key metadata, including the file name, size in pixels, resolution (DPI), color depth, and compression type.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Image Metadata Extraction**: Extracts metadata from supported image formats such as JPEG, PNG, BMP, and GIF.
- **User-friendly Interface**: Clean, responsive UI for easy navigation and data viewing.
- **File Management**: Automatically reads files from uploaded zip folders and displays metadata in a styled table.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/lesik248/Image-metadata-reader.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd Image-metadata-reader
    ```
3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the application**:
    ```bash
    python app.py
    ```
   The application should now be running at `http://127.0.0.1:5000`.

## Usage
1. Open the app in your browser.
2. Click on **Choose File** and upload a `.zip` folder containing images.
3. Click **Upload** to extract metadata for each image in the folder.
4. View the metadata in the table below the upload form.

## Contributing
Contributions are welcome! If you’d like to contribute, please fork the repository and create a pull request.

## License
This project is licensed under the MIT License.
