# CSV to XLSX Converter

This project is a web application that allows users to upload a CSV file with a specified delimiter, convert it to an XLSX file, and download the converted file. The application uses Flask for the backend, and HTML, TailwindCSS, and jQuery for the frontend.

## Features

- Upload a CSV file with a specified delimiter
- Convert the CSV file to an XLSX file
- Download the converted XLSX file
- Display a loading spinner while the file is being converted
- Reset the form to perform another conversion

## Requirements

- Python 3.x
- Flask
- Pandas
- Openpyxl

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/imrkaofficial/convert_csv_to_xlsx.git
    cd convert_csv_to_xlsx


2. Create a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


3. Install the required packages:
    ```sh
    pip install -r requirements.txt


## Usage

1. Start the Flask server:
    ```sh
    python app.py

2. Open your web browser and navigate to http://127.0.0.1:7001.

3. Enter the delimiter and upload the CSV file.

4. Click the "Convert" button to convert the CSV file to an XLSX file.

5. Once the conversion is complete, download the converted file by clicking the download link.

6. To perform another conversion, click the "Try Again" button to reset the form.

 
# License
This project is licensed under the [MIT License](/LICENSE).