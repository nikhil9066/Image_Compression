# Image Compression and Decompression

This Python script provides image compression and decompression using QR factorization and Singular Value Decomposition (SVD). It supports both QR and SVD methods for compression and decompression.

## Features

- Image compression and decompression using QR factorization and SVD.
- Visualization of cumulative energy graphs and singular values.
- Evaluation of accuracy through Mean Squared Error (MSE) and accuracy percentage.

## Table of Contents

- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Sample Output](#sample-output)

## Dependencies

- Python 3.x
- NumPy
- Matplotlib
- Pillow (PIL)

Install dependencies using:

```bash
pip install numpy matplotlib Pillow
```

## Installation

### Prerequisites

Before you begin, ensure you have Python 3.x installed on your system. If not, you can download and install it from [python.org](https://www.python.org/downloads/).

### Clone the Repository

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/image-compression.git
    cd image-compression
    ```

### Install Dependencies

2. Install the required dependencies using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

This will install NumPy, Matplotlib, and Pillow (PIL), which are necessary for the image compression and decompression script.

Now you're ready to use the image compression and decompression script.

## Usage

This script provides two methods for image compression and decompression: QR Factorization and Singular Value Decomposition (SVD). Follow the instructions below to use the script:

### Compression and Decompression using QR Factorization

To compress and decompress an image using QR Factorization, use the following command:

```bash
python main.py --method qr --k 50 --image_path path/to/your/image.jpg
```

## Examples

### Example using QR Compression and Decompression

#### Command:

```bash
python main.py --method qr --k 50 --image_path examples/sample_image.jpg
```
## Sample Output

### QR Compression and Decompression

<p align="center">
  <img src="https://github.com/nikhil9066/Image_Compression/assets/36182930/132dac3f-fb84-4f5a-973b-70b06393b96d" alt="Original Image" width="200"/>
  <img src="https://github.com/nikhil9066/Image_Compression/assets/36182930/0fd68dc9-5416-43ae-ba6c-87b9b6a6c63e" alt="Compressed Image (QR)" width="200"/>
  <img src="https://github.com/nikhil9066/Image_Compression/assets/36182930/c9013a1a-e0e8-4750-934d-975a81d95171" alt="Reconstructed Image (QR)" width="200"/>
</p>

### SVD Compression and Decompression

<p align="center">
  <img src="https://github.com/nikhil9066/Image_Compression/assets/36182930/62c1cbb8-e63a-4b31-af1b-0f1e41dc289a" alt="Original Image" width="200"/>
  <img src="https://github.com/nikhil9066/Image_Compression/assets/36182930/0ea9ddca-22f7-40b3-977b-6d8fff314fa1" alt="Compressed Image (SVD)" width="200"/>
  <img src="https://github.com/nikhil9066/Image_Compression/assets/36182930/9e59a532-7d09-45a3-95df-e4cc763a31b1" alt="Reconstructed Image (SVD)" width="200"/>
</p>

### Cumulative Energy Graphs

<p align="center">
  <img src="https://github.com/nikhil9066/Image_Compression/assets/36182930/b68044a2-3a70-460e-9d5d-5e9c08d10129" alt="Cumulative Energy Graph (QR)" width="200"/>
  <img src="https://github.com/nikhil9066/Image_Compression/assets/36182930/ccd26d11-3938-4c2c-8d40-16aeba718981" alt="Cumulative Energy Graph (QR)" width="200"/>
  <img src="https://github.com/nikhil9066/Image_Compression/assets/36182930/6094f5ae-9c34-4d7d-9940-07580ee5e282" alt="Cumulative Energy Graph (QR)" width="200"/>
</p>
