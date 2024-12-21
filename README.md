# README for S3 File Downloader Script

## Overview

This script downloads files from an S3-compatible storage service based on file names provided in an Excel sheet. The script connects to the specified S3 bucket and downloads the listed files to a designated local directory.

## Features

- Reads file names from an Excel file.
- Connects to an S3 bucket using user-provided credentials and endpoint.
- Downloads files from the S3 bucket to a specified local directory.
- Error handling to capture and display any issues during the file download process.

## Requirements

- Python 3.x
- Required libraries:
  - `pandas`
  - `boto3`

You can install the required libraries using `pip`:
```bash
pip install pandas boto3 openpyxl
```

## Configuration

1. **Excel File**  
   Replace `/path/to/excel/file/consisting/file/names` with the path to the Excel file containing the file names.

2. **Local Download Destination**  
   Replace `/path/to/download/destination/` with the path to the directory where the files should be downloaded.

3. **S3 Configuration**  
   You will be prompted to enter:
   - **Access Key**
   - **Secret Key**
   - **Bucket Name**
   - **Endpoint URL** (for S3-compatible services like MinIO)

## Usage

1. Run the script:
   ```bash
   python s3_file_downloader.py
   ```

2. Follow the prompts to input your S3 credentials, bucket name, and endpoint URL.

3. The script will:
   - Read the file names from the specified Excel file.
   - Attempt to download each file from the bucket to the local destination.

## Error Handling

- If an error occurs during the file download process, the error message will be displayed in the console for debugging purposes.

## Example Usage

### Input Prompt:
```plaintext
please enter s3 Access Key: <your-access-key>
please enter s3 Secret Key: <your-secret-key>
Please enter s3 Bucket name: my-bucket
Please enter s3 Endpoint URL: https://s3.amazonaws.com
```

### Output:
```plaintext
File example_file.txt downloaded successfully to /path/to/download/destination/
```

### On Error:
```plaintext
[Errno 2] No such file or directory: 'nonexistent_file.txt'
```

## Notes

- Ensure the Excel file is formatted correctly, with file names listed in a single column.
- Verify that the specified S3 bucket and endpoint URL are accessible using the provided credentials.
- Ensure the local download directory exists and is writable.

This script provides a basic solution for batch file downloads from S3-compatible storage. It can be enhanced with features like logging, file validation, and multi-threading for improved performance.
