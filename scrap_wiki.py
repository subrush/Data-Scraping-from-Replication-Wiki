import requests
from bs4 import BeautifulSoup
import pandas as pd

# Load the Excel file
file_path = 'Updated_ReplicationWiki_with_URLs.xlsx'
df = pd.read_excel(file_path)

# Function to scrape replication type
def get_replication_type(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Locate the table under "This article is a replication of"
        table = soup.find('table', text="This article is a replication of")
        if table:
            # Find the "Replication type" column in the table
            replication_type = table.find('td', text="Replication type").find_next('td').text.strip()
            return replication_type
        return None
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

# Iterate over the rows and scrape data
for index, row in df.iterrows():
    url = row['paper']  # Assuming 'paper' column has the URLs
    if pd.notnull(url):
        replication_type = get_replication_type(url)
        df.at[index, 'Replication type'] = replication_type

# Save the updated DataFrame back to Excel
output_file_path = 'Updated_ReplicationWiki.xlsx'
df.to_excel(output_file_path, index=False)

print(f"Scraping complete. Updated file saved to {output_file_path}")
