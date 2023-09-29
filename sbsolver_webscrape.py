import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

BASE_URL = "https://www.sbsolver.com/s/"

def get_content_from_div(url):
    r = requests.get(url)
    r.raise_for_status()

    soup = BeautifulSoup(r.content, 'lxml')
    div_content = soup.find('div', id='alpha-inner')
    return div_content.text if div_content else ''

if __name__ == "__main__":
    # Initialize an empty DataFrame with the desired columns
    df = pd.DataFrame(columns=["Sequence", "URL", "Text"])
    
    for i in range(1, 5):  # test batch of first 5 cases 
    # for i in range(1, 1970):  # first entry through Sept. 29th 2023 (note: this will take several hours to complete)
        url = BASE_URL + str(i)
        print(f"Fetching data from {url} ...")
        try:
            extracted_content = get_content_from_div(url)
            
            # Append the data to the DataFrame using loc
            df.loc[len(df)] = [i, url, extracted_content]
            
            time.sleep(2)  # Respectful delay between requests
        except requests.HTTPError:
            print(f"Failed to fetch from {url}")

    # Print the DataFrame to verify the data
    print(df)

    # If you want to save the DataFrame to a CSV file
    df.to_csv("sbsolver_data.csv", index=False)
