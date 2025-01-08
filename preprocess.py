import os
import pandas as pd
import configparser
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants (moved from global scope)
CONFIG_FILE = "config.ini"

def load_config():
    """Load configuration from config.ini file."""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return config


def get_patient_ids(config):
    """
    Reads patient IDs from a clinical data file specified in the config.
    
    Returns:
        list: A list of patient IDs.
    """
    try:
        clinical_data_path = config['Paths']['clinical_data_path']
        clinical_sample_size = int(config['Parameters']['clinical_sample_size'])

        logging.info(f"Loading clinical data from: {clinical_data_path}")

        df = pd.read_csv(clinical_data_path, sep='\t')
    
        if clinical_sample_size > len(df):
            logging.warning(f"Requested sample size {clinical_sample_size} is larger than dataset ({len(df)}). Using entire dataset.")
            sample_df = df
        else:
            sample_df = df.sample(n=clinical_sample_size, random_state=42) #set the random_state for reproducibility

        patient_ids = sample_df['Patient ID'].tolist()
        logging.info(f"Extracted patient IDs successfully.")
        return patient_ids
    except FileNotFoundError:
        logging.error(f"Error: Clinical data file not found at {clinical_data_path}")
        exit(1)  
    except KeyError as e:
        logging.error(f"Key error: {e}. Ensure config.ini has required keys")
        exit(1)
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        exit(1)

def split_fastq(fastq_file, output_dir, patient_ids):
    """
    Splits a FASTQ file into smaller files, one for each patient ID.

    Args:
        fastq_file (str): Path to the input FASTQ file.
        output_dir (str): Directory to save the split FASTQ files.
        patient_ids (list): List of patient IDs.
    """
    try:
      logging.info(f"Splitting FASTQ file: {fastq_file}")
      with open(fastq_file, "r") as file:
          total_sequences = sum(1 for _ in file) // 4  # Each sequence is 4 lines

      sequences_per_patient = total_sequences // len(patient_ids)
      remaining_sequences = total_sequences % len(patient_ids)

      # The splitting of the FASTQ is simulated for demonstration. Not based on real patient sequences.
      # Reset file pointer
      with open(fastq_file, "r") as file:
          for i, patient_id in enumerate(patient_ids):
                output_file = os.path.join(output_dir, f"{patient_id}_{'R1' if 'R1' in fastq_file else 'R2'}.fastq")
                with open(output_file, "w") as out:
                    # Allocate additional sequence if there are remainders
                    num_sequences = sequences_per_patient + (1 if i < remaining_sequences else 0)
                    for _ in range(num_sequences):
                        for _ in range(4):  # Each sequence has 4 lines
                            out.write(next(file))

      logging.info(f"Successfully split {fastq_file} into per-patient files.")
    except FileNotFoundError:
          logging.error(f"Error: FASTQ file not found at {fastq_file}")
          exit(1)
    except Exception as e:
        logging.error(f"An error occurred while splitting {fastq_file}: {e}")
        exit(1)

if __name__ == "__main__":
    config = load_config()
    patient_ids = get_patient_ids(config)
    
    fastq_r1 = config['Paths']['fastq_r1_path']
    fastq_r2 = config['Paths']['fastq_r2_path']
    output_dir = config['Paths']['output_directory']
    
    # Create output directory if it does not exist
    os.makedirs(output_dir, exist_ok=True)

    split_fastq(fastq_r1, output_dir, patient_ids)
    split_fastq(fastq_r2, output_dir, patient_ids)
    logging.info("FASTQ files have been successfully split and saved!")