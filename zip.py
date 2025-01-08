import os
import zipfile
import configparser
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
CONFIG_FILE = "config.ini"
R1_SUFFIX = "_R1.fastq"
R2_SUFFIX = "_R2.fastq"

def load_config():
    """Loads configuration from config.ini."""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return config

def zip_fastq_files(directory, output_zip, suffix):
    """
    Zips FASTQ files based on a suffix within the directory.

    Args:
        directory (str): Path to the directory containing the FASTQ files.
        output_zip (str): Path to save the generated ZIP archive.
        suffix (str): File suffix to identify files for zipping.
    """
    logging.info(f"Creating ZIP file: {output_zip} for suffix: {suffix}")
    try:
        with zipfile.ZipFile(output_zip, "w") as zipf:
            for file_name in os.listdir(directory):
                if file_name.endswith(suffix):
                    file_path = os.path.join(directory, file_name)
                    zipf.write(file_path, arcname=file_name)
        logging.info(f"Successfully created ZIP file: {output_zip}")
    except FileNotFoundError:
          logging.error(f"Error: Directory not found {directory}")
          exit(1)
    except Exception as e:
        logging.error(f"An error occurred while creating {output_zip}: {e}")
        exit(1)


if __name__ == "__main__":
    config = load_config()
    fastq_dir = config['Paths']['output_directory'] #output directory is where our split fastq files are
    r1_zip_path = "r1_fastq_files.zip"
    r2_zip_path = "r2_fastq_files.zip"
    
    zip_fastq_files(fastq_dir, r1_zip_path, R1_SUFFIX)
    zip_fastq_files(fastq_dir, r2_zip_path, R2_SUFFIX)