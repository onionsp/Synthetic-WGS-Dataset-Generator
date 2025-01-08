# Whole Genome Sequencing Data Workflow

This repository contains scripts for simulating a basic genomic data workflow. **It is crucial to understand that all data used in this repository, including the FASTQ files and clinical data, are either artifically generated or modified for testing and educational purposes only.** They do not represent any real patient or biological data.

## Purpose

This repository demonstrates a simplified data workflow involving:

1.  **Preprocessing:** Splitting a set of FASTQ files based on simulated patient identifiers derived from a downsampled clinical data file.
2.  **Archiving:** Zipping the split FASTQ files for easy storage and transfer.

This workflow can serve as a template for developing and testing more complex bioinformatics pipelines.

├── config.ini
├── data/
│ ├── sampled_clinical_data.tsv
│ └── 2A1_CGATGT_L001_R1_001.fastq
│ └── 2A1_CGATGT_L001_R2_001.fastq
├── preprocess.py
├── zip.py
└── README.md
## Repository Structure
*   `config.ini`: Configuration file containing file paths, parameters, and other settings.
*   `data/`: A folder containing the **fake** clinical data (`sampled_clinical_data.tsv`) and **public** FASTQ files (`2A1_CGATGT_L001_R1_001.fastq`, `2A1_CGATGT_L001_R2_001.fastq`). These files are from [GenomeInABottle]([url](https://github.com/genome-in-a-bottle/giab_data_indexes)).
*   `preprocess.py`: Python script for preprocessing and splitting the FASTQ files based on patient IDs.
*   `zip.py`: Python script for zipping the split FASTQ files.
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
3.  **Run Preprocessing Script:**
    ```bash
    python preprocess.py
    ```
    This will create the split FASTQ files in the specified output directory.
4.  **Run Zipping Script:**
    ```bash
    python zip.py
    ```
    This will create two zip files, `r1_fastq_files.zip` and `r2_fastq_files.zip`, containing the split FASTQ files.

## Key Concepts

*   **Simulated Data:** This repository utilizes **artificial data** for all genomic and clinical files. This data is not real and serves as a demo of a data workflow. **No real patient data or biological sequences are used in this project.**
*   **Configuration:** The use of a configuration file (config.ini) allows for easy customization and portability.
*   **Modularity:** The code is structured into functions and modules, making it more readable, maintainable, and reusable.
*   **Error Handling:** Includes mechanisms for error handling to prevent unexpected program termination and provide useful feedback.
*   **Logging:** Uses logging to provide information during execution, aiding in debugging and workflow monitoring.

## Important Note on Data Privacy

**The data provided in this repository is synthetic and does not represent any actual biological or personal data. It is solely intended for educational purposes and software development. No sensitive information or personally identifiable data is involved in this project.**
