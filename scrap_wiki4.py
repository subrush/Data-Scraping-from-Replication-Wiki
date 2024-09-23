import requests
from bs4 import BeautifulSoup
import pandas as pd

# Load the Excel file
file_path = 'ReplicationWiki_scraped_test.xlsx'
df = pd.read_excel(file_path)

# Function to fetch and display the entire table with class 'wikitable sortable zebra jquery-tablesorter'
def display_table(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        #print(soup)

        # Find the table with the specified classes
        table = soup.find('table', {'class': 'wikitable sortable zebra'})
        if table:
            print("Table found. Here is the content:")
            
            # Print the entire table HTML
            return table.prettify()
        else:
            return "Table not found"
    except Exception as e:
        return f"Error: {e}"

# Test with one URL from your dataset
#example_url = df['paper'].iloc[3]  # Use the first URL from the dataset for demonstration
#table_content = display_table(example_url)

# Show the table content
#print(table_content)


# Function to scrape the "Replication type" from the table's 9th column
def scrape_replication_type_from_ninth_column(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the table with the classes "wikitable sortable zebra jquery-tablesorter"
        table = soup.find('table', {'class': 'wikitable sortable zebra'})
        
        if table:
            # Loop through each row in the table
            for row in table.find_all('tr'):
                # Get all cells in the row
                cells = row.find_all('td')
                
                # If there are at least 9 cells, extract the value from the 9th column
                if len(cells) >= 9:
                    replication_type = cells[8].text.strip()  # 9th column is index 8
                    return replication_type
            return "Replication type not found"
        else:
            return "Table not found"
    except Exception as e:
        return f"Error: {e}"

# Apply the updated scraping function to each URL in the "paper" column
df['Replication type'] = df['paper'].apply(scrape_replication_type_from_ninth_column)

# Save the updated dataframe to a new Excel file
output_file_v6 = 'ReplicationWiki_scraped_output_v6.xlsx'
df.to_excel(output_file_v6, index=False)

output_file_v6

