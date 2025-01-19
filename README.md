# Whole Genome Sequencing Data Workflow

This repository contains scripts for simulating a basic genomic data workflow. **It is crucial to understand that all data used in this repository, including the FASTQ files and clinical data, are either artificially generated or modified for testing and educational purposes only.** They do not represent any real patient or biological data.

## Purpose

This repository demonstrates a simplified data workflow involving:

1.  **Preprocessing:** Splitting a set of FASTQ files based on simulated patient identifiers derived from a downsampled clinical data file. The splitting is now based on a target file size, using randomly sampled sequences.
2.  **Archiving:** Zipping the split FASTQ files for easy storage and transfer.

This workflow serves as a template for developing and testing more complex bioinformatics pipelines.

## Repository Structure

*   `config.ini`: Configuration file containing file paths, parameters, and other settings.
*   `data/`: A folder containing the **fake** clinical data (`sampled_clinical_data.tsv`) and **public** FASTQ files (`2A1_CGATGT_L001_R1_001.fastq`, `2A1_CGATGT_L001_R2_001.fastq`). These files are from [GenomeInABottle](https://github.com/genome-in-a-bottle/giab_data_indexes).
*   `preprocess.py`: Python script for preprocessing and splitting the FASTQ files based on patient IDs. The splitting is now done by target file size in gigabytes using random sampling.
*   `zip.py`: Python script for zipping the split FASTQ files.
*   `main.py`: Python script that executes both `preprocess.py` and `zip.py` with one call.
*   `README.md`: This file, providing documentation for the repository.

## Usage

1.  **Clone the Repository:**
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```
2.  **Configuration:** Adjust the `config.ini` file according to your desired paths and parameters of your own .fastq and .tsv files.
    *   `clinical_data_path`: Path to the clinical data TSV file.
    *   `fastq_r1_path`: Path to the R1 FASTQ file.
    *   `fastq_r2_path`: Path to the R2 FASTQ file.
    *   `output_directory`: Directory where split FASTQ files will be created.
    *   `clinical_sample_size`: Number of samples from clinical data to downsample to.
    *   `target_file_size_gb`: Target size of the split FASTQ files in gigabytes.
3.  **Run the Workflow Using Main Class:**
    ```bash
    python main.py
    ```
    This will create the split FASTQ files in the specified output directory, with each file approximately the specified size. The sequences are randomly sampled from the original fastq file.  The split FASTQ files are then zipped into `r1_fastq_files.zip` and `r2_fastq_files.zip`.

## Important Note on Data Privacy

**The data provided in this repository is synthetic and does not represent any actual biological or personal data. It is solely intended for educational purposes and software development. No sensitive information or personally identifiable data is involved in this project.**
