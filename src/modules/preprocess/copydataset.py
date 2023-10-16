import shutil
import os


def copy_files(src_dir, dest_dir):
    """
    This Function copies all contents of src_dir to dest_dir. Useful for preprocessing of raw dataset such that original data files are retained.
    """
    try:
        if not os.path.exists(src_dir):
            raise FileNotFoundError(
                f"error: Source directory '{src_dir}' not found.")

        if os.path.exists(dest_dir):
            print(f"copydataset.py: Source directory '{dest_dir}' already exists")
            return

        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        files = [f for f in os.listdir(src_dir) if os.path.isfile(
            os.path.join(src_dir, f)) and f.endswith('.csv')]

        for file in files:
            src_path = os.path.join(src_dir, file)
            dest_path = os.path.join(dest_dir, file)
            shutil.copy2(src_path, dest_path)  # Use copy2 to preserve metadata

        print(
            f"Successfully copied {len(files)} files from '{src_dir}' to '{dest_dir}'")

    except Exception as e:
        print(f"An error occurred in copydataset.py: {str(e)}")
