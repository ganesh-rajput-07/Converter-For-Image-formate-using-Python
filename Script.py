pip install pillow

from PIL import Image

def image_converter():
    # Ask the user for the input file
    input_file = input("Enter the path of the image file you want to convert: ")

    try:
        # Open the input image
        img = Image.open(input_file)

        # Display available formats
        print("\nAvailable formats: JPG, PNG, WEBP, ICO, BMP, TIFF")
        output_format = input("Enter the format you want to convert to (e.g., JPG, PNG): ").upper()

        # Validate output format
        valid_formats = {"JPG", "JPEG", "PNG", "WEBP", "ICO", "BMP", "TIFF"}
        if output_format not in valid_formats:
            print(f"Invalid format '{output_format}'. Please choose from {valid_formats}.")
            return

        # Set the output file name
        output_file = input("Enter the output file name (without extension): ") + f".{output_format.lower()}"

        # Convert to RGB for formats that don't support transparency (e.g., JPG)
        if output_format in {"JPG", "JPEG"}:
            img = img.convert("RGB")

        # Save the file in the specified format
        img.save(output_file, format=output_format)
        print(f"Conversion successful! The image has been saved as '{output_file}'.")
    except FileNotFoundError:
        print("The specified file was not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the converter
if __name__ == "__main__":
    image_converter()
