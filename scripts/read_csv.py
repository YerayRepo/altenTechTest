# read_csv.py

import csv

def clean_header(header):
    """ Removes the sufixes like <Number>, <Text>, etc. """
    attribute_name = header.split('<')[0]
    attribute_type = header.split('<')[1].split('>')[0] if '<' in header else None
    return attribute_name, attribute_type

def read_csv(file_path):
    """
    Reads csv file and returns a dict with the data
    """
    entities = []
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            headers = reader.fieldnames
            cleaned_headers = [
                clean_header(header) for header in headers
            ]
            for row in reader:
                entity = {}
                for header, (clean_name, attribute_type) in zip(headers, cleaned_headers):
                    entity[clean_name] = {
                        'type': attribute_type if attribute_type else 'Text', 
                        'value': row[header]
                    }
                entities.append(entity)
        return entities
    except Exception as e:
        print(f"Error trying to read the csv file: {e}")
        return None
