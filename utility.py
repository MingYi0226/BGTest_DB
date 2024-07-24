import re
import math
import pandas as pd
from openai import OpenAI
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def extract_event(description):
    if str(description) == 'nan':
        return ''
    history = [
        {"role": "system", "content": "You are an assistant who extracts keywords."},
        {"role": "user", "content": "Extract event industry seperated by comma from the following description."},
        {"role": "user", "content": description},
    ]
    completion = client.chat.completions.create(
        model="PrunaAI/defog-llama-3-sqlcoder-8b-GGUF-smashed",
        messages=history,
        temperature=0.7,
        stream=True,
        max_tokens=20,
    )
    response = ''
    for chunk in completion:
        if chunk.choices[0].delta.content:
            response += chunk.choices[0].delta.content
    response = response.lower().replace('event industry:', '')
    return response

def name2email(strPattern, first, last):
    if len(strPattern) == 0:
        return ''
    if first == 'nan':
        first = ''
    if last == 'nan':
        last = ''
    parts = re.split(r'\[|\]', strPattern)
    for i, part in enumerate(parts):
        if part == 'first':
            parts[i] = first
        elif part == 'first_initial':
            parts[i] = first[0] if len(first) > 0 else ''
        elif part == 'last':
            parts[i] = last
        elif part == 'last_initial':
            parts[i] = last[0] if len(last) > 0 else ''
    return ''.join(parts)

def extract_keyword(fileName:str):
    try:
        # Read the CSV file
        df = pd.read_csv(f'..\events-data\{fileName}')
        
        for index, row in df.iterrows():
            # Process the 'event_description' column
            industry = extract_event(row['event_description'])
            df.at[index, 'event_industry'] = industry
            print(f'{index}: {industry}')

        # Save the modified DataFrame back to a CSV file
        df.to_csv(f'..\events-data\{fileName}_', index=False)

    except Exception as e:
        print(f"Error occured :{e}")
    
def generate_email(fileName:str):
    try:
        # Read the CSV file
        df = pd.read_csv(f'..\events-data\{fileName}')
        
        for index, row in df.iterrows():
            x = str(row['email_pattern'])
            if x == 'nan':
                continue
            email = name2email(
                str(row['email_pattern']).strip(), 
                str(row['first_name']).strip(), 
                str(row['last_name']).strip())
            df.at[index, 'email'] = email
            print(f'{index}: {email}')

        # Save the modified DataFrame back to a CSV file
        df.to_csv(f'..\events-data\{fileName}_', index=False)

    except Exception as e:
        print(f"Error occured :{e}")

if __name__ == '__main__':
    extract_keyword('event_info.csv')
    generate_email('people_info.csv')