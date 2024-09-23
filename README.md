# Data-Scraping-from-Replication-Wiki
Data Scraping from Replication Wiki
# Replication Type Scraper

This project is a Python-based web scraper that extracts the "Replication type" information from academic paper links. The scraper works by visiting the provided URLs, locating a table with the class `wikitable sortable zebra jquery-tablesorter`, and retrieving the information from the 9th column in the table, which corresponds to the "Replication type".

## Features

- Scrapes academic papers from URLs and extracts "Replication type" from a specific table.
- Outputs the results into an Excel file with the scraped data in the appropriate column.
- Handles errors such as missing tables or unexpected page structures.

## Requirements

- Python 3.x
- The following Python libraries:
  - `requests`
  - `beautifulsoup4`
  - `pandas`
  - `openpyxl`

You can install the required libraries using pip:

```bash
pip install requests beautifulsoup4 pandas openpyxl
```

## How It Works

1. **Input**: The script reads an Excel file that contains URLs to academic papers in column B. The goal is to scrape the "Replication type" for each URL and store it in column A of the same Excel sheet.
  
2. **Process**:
   - For each URL in column B, the script sends an HTTP request to fetch the HTML page.
   - It parses the HTML using `BeautifulSoup` and locates the table with the class `wikitable sortable zebra jquery-tablesorter`.
   - It then finds the 9th column, which contains the "Replication type", and extracts the relevant data.

3. **Output**: The scraped data is written back into an Excel file with the "Replication type" placed in column A for each corresponding paper.

## Files

- **`scraper.py`**: The main script that performs the web scraping and saves the results to Excel.
- **`ReplicationWiki_scraped_output.xlsx`**: The Excel file that contains the output with the scraped "Replication type" data.

## Usage

1. Ensure you have the necessary Python environment and dependencies installed.
2. Place the Excel file with the academic paper URLs in column B.
3. Run the script `scraper.py` to start the scraping process.

```bash
python scraper.py
```

4. Once the process is complete, check the output Excel file for the scraped "Replication type" values in column A.

## Error Handling

- If the script encounters a page without the expected table structure, it will log a "Table not found" or "Replication type not found" message for that URL.
- Any unexpected errors during the scraping process will be captured and printed for debugging purposes.

## Example

For an input Excel file that looks like this:

| Replication type | Paper URL                                      |
|------------------|------------------------------------------------|
|                  | https://example.com/paper1                     |
|                  | https://example.com/paper2                     |

After running the script, it will output an Excel file with the "Replication type" data populated, like this:

| Replication type | Paper URL                                      |
|------------------|------------------------------------------------|
| Type 1           | https://example.com/paper1                     |
| Type 2           | https://example.com/paper2                     |

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
