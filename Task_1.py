import os
import shutil
import sys

def main():
    # Parse command line arguments
    if len(sys.argv) < 2:
        
        sys.exit(1)
    
    source_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else 'dist'
    
    # Ensure the destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # Process the source directory
    process_directory(source_dir, dest_dir)

def process_directory(path, dest_path):
    try:
        # List all items in the directory
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            # If the item is a directory, process it recursively
            if os.path.isdir(item_path):
                process_directory(item_path, dest_path)
            # If the item is a file, process it for copying
            elif os.path.isfile(item_path):
                process_file(item_path, dest_path)
    except Exception as e:
        print(f"Error processing directory {path}: {e}")

def process_file(file_path, dest_path):
    try:
        # Get the file extension
        _, ext = os.path.splitext(file_path)
        ext = ext.lstrip('.').lower()  # Remove leading dot and convert to lowercase
        # Create a new directory based on the file extension
        new_dir = os.path.join(dest_path, ext)
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        # Copy the file to the new directory
        shutil.copy(file_path, new_dir)
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

if __name__ == "__main__":
    main()
