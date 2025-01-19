import subprocess
import logging
import os
import configparser

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
CONFIG_FILE = "config.ini"

def load_config():
    """Loads configuration from config.ini."""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return config

class Workflow:
    def __init__(self):
        self.config = load_config()
        self.preprocess_script = "preprocess.py"
        self.zip_script = "zip.py"

    def run_preprocess(self):
        """Runs the preprocess.py script."""
        logging.info("Starting preprocess step...")
        try:
            subprocess.run(["python", self.preprocess_script], check=True)
            logging.info("Preprocess step completed successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error running preprocess.py: {e}")
            exit(1)

    def run_zip(self):
        """Runs the zip.py script."""
        logging.info("Starting zip step...")
        try:
            subprocess.run(["python", self.zip_script], check=True)
            logging.info("Zip step completed successfully.")
        except subprocess.CalledProcessError as e:
             logging.error(f"Error running zip.py: {e}")
             exit(1)
    def run_all(self):
        """Runs the entire workflow."""
        self.run_preprocess()
        self.run_zip()
        logging.info("Workflow completed successfully!")


if __name__ == "__main__":
    workflow = Workflow()
    workflow.run_all()