# Spelling Bee Solver Web Scraper

**Author:** [Z. A. Caddick](https://zacharycaddick.com/)

## Description

This repository contains a two-script data pipeline designed to scrape, retrieve, and process game data from `sbsolver.com`.
- `sbsolver_webscrape.py`: Pulls historical game data from The New York Times Spelling Bee hosted on 'SBSolver.com'.
- `sbsolver_data_cleanup.py`: Processes the fetched data into structured columns.

## Features

- Extract game date.
- Identify the puzzle's center and outer letters.
- Parse word lists, word count, scores, and pangrams.
- Enumerate unique letters within pangrams.
- Categorize by word length and corresponding count.

## SBSolver Data Pipeline

### 1. sbsolver_webscrape.py

#### Overview
A web scraper developed in Python to fetch game data from `sbsolver.com`.

#### Features
- Retrieve content in sequence.
- Configurable scraping range.
- Built-in delay between requests for server-friendliness.
- Handle HTTP errors.
- Save fetched data to `sbsolver_data.csv`.

#### Usage
1. Install the necessary modules:
    ```bash
    pip install requests beautifulsoup4 pandas
    ```
2. Execute the script:
    ```bash
    python sbsolver_webscrape.py
    ```
3. Output saved to `sbsolver_data.csv`.

### 2. sbsolver_data_cleanup.py

#### Overview
Processes the raw data fetched by the web scraper, refining it into structured form.

#### Features
- Extract game specifics: date, letters, pangrams, word count, etc.
- Determine the common letter across all game words.
- Save refined data to `sb_solver_filtered_data.csv`.

#### Usage
1. Ensure you have the dependencies:
    ```bash
    pip install pandas
    ```
2. Run the script:
    ```bash
    python sbsolver_data_cleanup.py
    ```

## Good Practices
- **Web Scraping**: Adhere to the website's `robots.txt` rules and obtain necessary permissions.
- **Pipeline Flow**: Start with the web scraping script, followed by the cleanup script.

## Output DataFrame Structure

The polished `df_processed` DataFrame includes:
1. **date**: Game's date.
2. **center_letter**: Center Letter which appears in every game word.
3. **letters**: Unique pangram letters, separated by commas.
4. **pangrams**: Count of pangrams.
5. **perfect**: Count of perfect pangrams.
6. **words**: Total word count.
7. **score**: Overall score.
8. **pangram_list**: List of pangrams.
9. **word_list**: Word list for each game.
10. **letters_word_count**: Count of words for specific letters.
11. **column_word_count**: Count of words by length.
