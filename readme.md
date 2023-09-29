
# Spelling Bee Solver Web Scraper
Authors: [Caddick, Z. A.](https://zacharycaddick.com/), 

## Description
This script extracts past game data from 'SBSolver.com' for The New York Times Spelling Bee. With an input DataFrame containing unstructured text, the script processes and extracts various game metrics, including word counts, scores, pangrams, and more, returning a structured DataFrame.

## Features
- **Extracts game date.**
- **Identifies the letters for each game** – the center letters and the outer letters for each puzzle.
- **Parses out** the word list, total word count, scores, and pangrams.
- **Retrieves a list** of unique letters used in the pangrams.
- **Categorizes the word length** and its respective count.
  
## How to Use
1. Ensure you have `pandas` and `re` modules installed.
2. Import the `extract_data_from_text` function from the script.
3. Prepare a pandas DataFrame (`df`) with a column named "Text" containing unstructured data.
4. Call the function and pass your DataFrame: 
    ```python
    df_processed = extract_data_from_text(df)
    ```
5. The `df_processed` DataFrame will now contain structured game data.

## Output DataFrame Structure
The output DataFrame (`df_processed`) contains the following columns:
1. **date**: The date of the Spelling Bee game.
2. **center_letter**: The letter(s) that appear in every word for the game.
3. **letters**: A comma-separated list of unique letters found in the pangram list.
4. **pangrams**: The number of pangrams found.
5. **perfect**: The number of perfect pangrams.
6. **words**: Total number of words.
7. **score**: Total score.
8. **pangram_list**: List of pangrams.
9. **word_list**: List of words for the game.
10. **letters_word_count**: Word count based on specific letters.
11. **column_word_count**: Word count based on word length.
