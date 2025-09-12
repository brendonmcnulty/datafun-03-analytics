# datafun-03-analytics
Data Analytics – Module 3

This project demonstrates an end-to-end pattern for fetching and processing multiple data types (Excel, Text, CSV, JSON) with Python.
All scripts log progress via utils_logger.py and save inputs/outputs in consistent folders.

⚙️ Setup & Run
Requirements

Python 3.10+

Virtual environment recommended

Packages: requests, pandas, openpyxl (others are from Python’s standard library)

1) Create & activate a virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

2) Install dependencies
pip install -r requirements.txt

3) Run scripts

Use the commands listed below for each fetcher/processor.

📥 Fetch Scripts
brendon_get_excel.py

Purpose: Fetches the Tableau Superstore Subset Excel dataset.

Output: brendon_data/superstore_subset.xlsx

Run:

python brendon_get_excel.py

brendon_get_text.py

Purpose: Fetches a plain-text sample (W3C ISO 8859-1 character list).

Output: brendon_data/w3c_iso_8859-1.txt

Run:

python brendon_get_text.py

brendon_get_csv.py

Purpose: Fetches the Iris dataset (classic ML dataset).

Source: https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

Output: brendon_data/iris.csv

Run:

python brendon_get_csv.py

brendon_get_json.py

Purpose: Fetches dog breed data from the Dog CEO API.

Source: https://dog.ceo/api/breeds/list/all

Output: brendon_data/dog_breeds.json

Run:

python brendon_get_json.py

🛠 Process Scripts
brendon_process_excel.py

Purpose: Processes the Superstore Excel file.

Steps: Loads Excel; standardizes columns; coerces types; derives fields (profit_margin, order_year, etc.); summarizes; saves a text summary.

Output: brendon_processed/superstore_subset_summary.txt

Run:

python brendon_process_excel.py

brendon_process_text.py

Purpose: Processes the W3C text file.

Steps: Counts case-insensitive occurrences of the word LATIN.

Output: brendon_processed/text_w3c_word_count.txt

Run:

python brendon_process_text.py

brendon_process_csv.py

Purpose: Processes the Iris CSV file.

Steps: Reads the sepal_length column, computes min, max, mean, and stdev, and writes results to a summary file.

Output: brendon_processed/iris_sepal_length_stats.txt

Run:

python brendon_process_csv.py

brendon_process_json.py

Purpose: Processes the Dog CEO breeds JSON.

Steps: Counts total breeds, total sub-breeds, and lists a sample of breed names.

Output: brendon_processed/dog_breeds_summary.txt

Run:

python brendon_process_json.py

🗂 Project Structure
.
├── brendon_data/                     # Raw fetched data
│   ├── superstore_subset.xlsx
│   ├── w3c_iso_8859-1.txt
│   ├── iris.csv
│   └── dog_breeds.json
├── brendon_processed/                # Processed outputs
│   ├── superstore_subset_summary.txt
│   ├── text_w3c_word_count.txt
│   ├── iris_sepal_length_stats.txt
│   └── dog_breeds_summary.txt
├── brendon_get_excel.py
├── brendon_process_excel.py
├── brendon_get_text.py
├── brendon_process_text.py
├── brendon_get_csv.py
├── brendon_process_csv.py
├── brendon_get_json.py
├── brendon_process_json.py
├── utils_logger.py
└── README.md

🔎 Notes

All scripts assume utils_logger.py is in the same folder for logging.

Inputs go in brendon_data/; processed outputs go in brendon_processed/.

If you don’t want to track generated outputs, add brendon_processed/ to .gitignore.