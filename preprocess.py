import os
import pandas as pd
import configparser
import logging
import random

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

def split_fastq(fastq_file, output_dir, patient_ids, target_file_size_gb):
    """
    Splits a FASTQ file into smaller files, one for each patient ID, with target file size using random sampling.
    
    Args:
        fastq_file (str): Path to the input FASTQ file.
        output_dir (str): Directory to save the split FASTQ files.
        patient_ids (list): List of patient IDs.
        target_file_size_gb (float): Target size for each output file in gigabytes.
    """
    try:
        logging.info(f"Splitting FASTQ file: {fastq_file}")
        target_file_size_bytes = target_file_size_gb * 1024 * 1024 * 1024  # Convert GB to bytes

        sequences = []
        with open(fastq_file, "r") as file:
            while True:
                try:
                    sequence = [next(file) for _ in range(4)]
                    sequences.append(sequence)
                except StopIteration:
                   break  #stop reading from file

        total_sequences = len(sequences)

        for patient_id in patient_ids:
            output_file = os.path.join(output_dir, f"{patient_id}_{'R1' if 'R1' in fastq_file else 'R2'}.fastq")
            
            current_file_size = 0
            with open(output_file, "w") as out:
              while current_file_size < target_file_size_bytes and sequences:
                  random_index = random.randint(0, len(sequences) - 1)
                  sampled_sequence = sequences[random_index]

                  # Write the sequence to the output file and update the current file size
                  for line in sampled_sequence:
                      out.write(line)
                      current_file_size += len(line.encode('utf-8'))

        logging.info(f"Successfully split {fastq_file} into per-patient files using random sampling.")

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
    target_size = float(config['Parameters']['target_file_size_gb']) # get target file size
    
    # Create output directory if it does not exist
    os.makedirs(output_dir, exist_ok=True)

    split_fastq(fastq_r1, output_dir, patient_ids, target_size)
    split_fastq(fastq_r2, output_dir, patient_ids, target_size)
    logging.info("FASTQ files have been successfully split and saved!")