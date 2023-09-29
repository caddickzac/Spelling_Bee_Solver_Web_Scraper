import pandas as pd

# Replace 'sbsolver_data.csv' with the path to your CSV file
df = pd.read_csv('sbsolver_data.csv')

# Display the first few rows of the DataFrame to confirm it loaded correctly
df.head()

import pandas as pd
import re

def extract_data_from_text(df):
    def extract_info(text):
        date_match = re.search(r'Spelling Bee for (\w+ \d+, \d+)', text)
        words_match = re.search(r'words: (\d+)', text)
        pangrams_match = re.search(r'pangrams: (\d+)', text)
        perfect_match = re.search(r'perfect: (\d+)', text)
        score_match = re.search(r'score: (\d+)', text)
        letters_matches = re.findall(r'([A-Z]) x (\d+)', text)
        word_list_matches = re.findall(r'([A-Z]+\n\n\d+)', text)
        pangram_list_matches = re.findall(r'([A-Z]+)\n\n\d+\n\n(perfect pangram|pangram)', text)
        column_word_count_matches = re.findall(r'(\d+L) x (\d+)', text)
        
        date = date_match.group(1) if date_match else None
        words = int(words_match.group(1)) if words_match else None
        pangrams = int(pangrams_match.group(1)) if pangrams_match else None
        perfect = int(perfect_match.group(1)) if perfect_match else None
        score = int(score_match.group(1)) if score_match else None
        letters_word_count = {match[0]: int(match[1]) for match in letters_matches} if letters_matches else {}
        
        word_list = [word.split('\n\n')[0] for word in word_list_matches] if word_list_matches else []
        pangram_list = [match[0] for match in pangram_list_matches] if pangram_list_matches else []
        
        # Determine the unique, sorted letters from the pangram list
        unique_letters = sorted(set(''.join(pangram_list)))
        letters = ', '.join(unique_letters)
        
        column_word_count = {match[0]: int(match[1]) for match in column_word_count_matches} if column_word_count_matches else {}

        return pd.Series([date, letters, pangrams, perfect, words, score, pangram_list, word_list, letters_word_count, column_word_count], 
                         index=['date', 'letters', 'pangrams', 'perfect', 'words', 'score', 'pangram_list', 'word_list', 'letters_word_count', 'column_word_count'])

    df_extracted = df['Text'].apply(extract_info)
    
    # Rearrange letters so the common letter is at index 0 and extract center letter
    def get_center_and_rearrange_letters(row):
        letters_list = row['letters'].split(', ')
        center_letter = [letter for letter in letters_list if all(letter in word for word in row['word_list'])]
        
        if center_letter:  # If a center letter is found
            letters_list.remove(center_letter[0])
            letters_list.insert(0, center_letter[0])
            return pd.Series([center_letter[0], ', '.join(letters_list)], index=['center_letter', 'letters'])
        else:
            return pd.Series([None, row['letters']], index=['center_letter', 'letters'])

    df_center_and_reordered = df_extracted.apply(get_center_and_rearrange_letters, axis=1)
    df_extracted['center_letter'] = df_center_and_reordered['center_letter']
    df_extracted['letters'] = df_center_and_reordered['letters']

    # Reorder columns
    final_columns_order = ['date', 'center_letter', 'letters', 'pangrams', 'perfect', 'words', 'score', 'pangram_list', 'word_list', 'letters_word_count', 'column_word_count']
    df_processed = df_extracted[final_columns_order]

    return pd.concat([df, df_processed], axis=1)

df_processed = extract_data_from_text(df)
print(df_processed)

# save cleaned data
df_processed.to_csv('sb_solver_filtered_data.csv', index=False)

