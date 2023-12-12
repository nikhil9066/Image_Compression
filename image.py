import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Function to calculate Mean Squared Error (MSE)
def calculate_mse(original, reconstructed):
    mse = np.mean((original - reconstructed)**2)
    return mse

# Function to calculate accuracy percentage
def calculate_accuracy_percentage(mse, max_possible_mse):
    accuracy_percentage = 100 * (1 - mse / max_possible_mse)
    return accuracy_percentage

# Function to normalize image values between 0 and 1
def normalize_image(image):
    return image / np.max(image)

# SVD Compression function
def svd_compress(image, k):
    U, S, Vt = np.linalg.svd(image, full_matrices=False)
    singular_values_squared = S**2
    cumulative_energy = np.cumsum(singular_values_squared) / np.sum(singular_values_squared)

    # Plotting the cumulative energy graph for compression
    plt.plot(cumulative_energy, marker='o')
    plt.title('Cumulative Energy of Singular Values (Compression)')
    plt.xlabel('Number of Singular Values')
    plt.ylabel('Cumulative Energy')
    plt.show()

    compressed_U = U[:, :k]
    compressed_S = np.diag(S[:k])
    compressed_Vt = Vt[:k, :]
    compressed_image = np.dot(compressed_U, np.dot(compressed_S, compressed_Vt))

    # Plotting the singular values for compression
    plt.plot(S, marker='o')
    plt.title('Singular Values (Compression)')
    plt.xlabel('Index')
    plt.ylabel('Singular Value')
    plt.show()

    accuracy_before = calculate_mse(image, compressed_image)
    max_possible_mse = np.max(image)**2  # Maximum possible MSE when all pixel values are different
    accuracy_percentage_before = calculate_accuracy_percentage(accuracy_before, max_possible_mse)

    print(f'MSE Before Compression (SVD): {accuracy_before}')
    print(f'Accuracy Before Compression (SVD): {accuracy_percentage_before}%\n')

    print('U matrix (Left Singular Vectors):')
    print(compressed_U)
    print('\nS matrix (Diagonal Singular Values):')
    print(compressed_S)
    print('\nVt matrix (Right Singular Vectors):')
    print(compressed_Vt)
    
    return compressed_image, compressed_U, compressed_S, compressed_Vt

# SVD Decompression function
def svd_decompress(compressed_U, compressed_S, compressed_Vt):
    reconstructed_image = np.dot(compressed_U, np.dot(compressed_S, compressed_Vt))

    # Plotting the singular values for decompression
    singular_values = np.diag(compressed_S)
    plt.plot(singular_values, marker='o')
    plt.title('Singular Values (Decompression)')
    plt.xlabel('Index')
    plt.ylabel('Singular Value')
    plt.show()

    accuracy_after = calculate_mse(original_image, reconstructed_image)
    max_possible_mse = np.max(original_image)**2  # Maximum possible MSE for the original image
    accuracy_percentage_after = calculate_accuracy_percentage(accuracy_after, max_possible_mse)

    print(f'MSE After Decompression (SVD): {accuracy_after}')
    print(f'Accuracy After Decompression (SVD): {accuracy_percentage_after}%\n')

    print('U matrix (Left Singular Vectors):')
    print(compressed_U)
    print('\nS matrix (Diagonal Singular Values):')
    print(compressed_S)
    print('\nVt matrix (Right Singular Vectors):')
    print(compressed_Vt)

    return reconstructed_image, accuracy_after, accuracy_percentage_after

# Function to evaluate accuracy
def evaluate_accuracy(original, reconstructed, method):
    mse = calculate_mse(original, reconstructed)
    max_possible_mse = np.max(original)**2
    accuracy_percentage = calculate_accuracy_percentage(mse, max_possible_mse)
    
    print(f'MSE After Decompression ({method}): {mse}')
    print(f'Accuracy After Decompression ({method}): {accuracy_percentage}%\n')

# Load the image
image_path = "1800.jpeg"

image = np.array(Image.open(image_path))

# Find the range of pixel values
min_pixel_value = np.min(image)
max_pixel_value = np.max(image)

print(f"Min Pixel Value: {min_pixel_value}")
print(f"Max Pixel Value: {max_pixel_value}")


original_image = np.array(Image.open(image_path).convert("L"))  # Convert to grayscale

# Display the original image
plt.imshow(original_image, cmap='gray')
plt.title('Original Image')
plt.show()


# Compression and Decompression using SVD
print("Compression and Decompression using SVD")
k_svd = 50  # Adjust this value based on the desired compression level for SVD
compressed_image_svd, compressed_U_svd, compressed_S_svd, compressed_Vt_svd = svd_compress(original_image, k_svd)
reconstructed_image_svd, _, _ = svd_decompress(compressed_U_svd, compressed_S_svd, compressed_Vt_svd)

# Evaluate accuracy for SVD
evaluate_accuracy(original_image, reconstructed_image_svd, 'SVD')

# Visualization for SVD
plt.imshow(compressed_image_svd, cmap='gray')
plt.title('Compressed Image (SVD)')
plt.show()
plt.imshow(reconstructed_image_svd, cmap='gray')
plt.title('Reconstructed Image (SVD)')
plt.show()