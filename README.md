# Whole Genome Sequencing Data Workflow

This repository contains scripts for simulating a basic genomic data workflow. **It is crucial to understand that all data used in this repository, including the FASTQ files and clinical data, are either artificially generated or modified for testing and educational purposes only.** They do not represent any real patient or biological data.

## Purpose

This repository demonstrates a simplified data workflow involving:

1.  **Preprocessing:** Splitting a set of FASTQ files based on simulated patient identifiers derived from a downsampled clinical data file. The splitting is now based on a target file size, using randomly sampled sequences.
2.  **Archiving:** Zipping the split FASTQ files for easy storage and transfer.

This workflow serves as a template for developing and testing more complex bioinformatics pipelines.

## Repository Structure

*   `config.ini`: Configuration file containing file paths, parameters, and other settings.
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
2.  **Configuration:** Adjust the `config.ini` file according to your desired paths and parameters of your own .fastq and .tsv files. **Clinical data and fastq files will need to be downloaded from public sources.**
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

## Data Transfer Agreement

1. **Purpose of the Agreement** (Please select one):  

    A. Research purposes 

    B. Others: **[Specify]** 

2. **Description of the Data:**  

    The dataset utilized in this project is **synthetically** generated, with individual data points retrieved programmatically using Python scripts. Including the patientID and the sampleID that is in the clinical dataset. 

    The clinical dataset, comprising patient-related information which includes; Mutation Count, Diagnosis Age, Sex, Ethnicity Category, Sample Type, country, Days to Last Followup, Location, Neoplasm Disease Stage American Joint Committee on Cancer Code, Sample Class, 
    Smoker status, TMB (nonsynonymous), Tumor Grade, Tumor Other Histologic Subtype, has been sourced from CBioPortal. Aside from these data, which includes; patientid and sampleid has been synthetically generated using Python scripts. 

    The FASTQ files included in the dataset are derived from a single FASTQ file obtained from the Genome in a Bottle project (NCBI). This original file has been partitioned into 100 smaller segments for processing purposes. 

3. **References of data:** 

    CBioPortal, the code randomly picks 100 data from this dataset. The code then proceeds to add PatientID and SampleID  - https://www.cbioportal.org/study/clinicalData?id=paad_qcmg_uq_2016  

    Genome in a bottle (NCBI) - https://ftp.ncbi.nlm.nih.gov/ReferenceSamples/giab/data_indexes/AshkenazimTrio/sequence.index.AJtrio_Illumina300X_wgs_07292015_updated  

    Code to generate final dataset- https://github.com/onionsp/Synthetic-WGS-Dataset-Generator  

 

4. **Terms and conditions:** 

    **Usage Restrictions:** Data Recipient agrees to not Use or Disclose the Data Set (or components) for any purpose other than as described for the Research Project or as Required by Law. 

    **Confidentiality:** Data Recipient agrees to ensure that any agent, including a subcontractor, to whom it provides the Data Set, agrees to the same restrictions and conditions that apply through this Agreement to the Data Recipient with respect to such information. 

    **Compliance:** Data Recipient agrees not to contact any individuals from or about whom the data apply, and for Limited Data Sets, agrees not to attempt to identify the information contained in the Data Set. 

    **Return or Destruction:** Data Recipient will indemnify, defend and hold harmless the University’s and any University affiliates’ trustees, officers, directors, employees and agents from and against any claim, cause of action, liability, damage, cost or expense
    (including without limitation, reasonable attorney’s fees and court costs) arising out of or in connection with any unauthorized or prohibited Use or Disclosure of the Data Set or any other breach of this Agreement by Data Recipient or any subcontractor, agent 
    or person under Data Recipient’s control. 
