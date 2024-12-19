# orion.py

import requests

orion_url = 'http://localhost:1026/v2/entities'

def clean_value(value, attribute_type):
    """
    Cleans the data to be able to work with it easily
    """
    if attribute_type == 'Number':
        try:
            return float(value)
        except ValueError:
            print(f"Value {value} is not valid")
            return 0  
    elif attribute_type == 'Text':
        return value.strip().replace('"', '').replace(',', '')
    return value

def get_entity(entity_id, entity_type):
    """
    Retrieves data of an entity from Orion
    """
    url = f"{orion_url}/{entity_id}?type={entity_type}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"Entity {entity_id} retrived")
        print("Data:")
        print(response.json())  
    else:
        print(f"Error trying to retrive {entity_id}: {response.status_code}, {response.text}")

def delete_entity(entity_id, entity_type):
    """
    Deletes an entity in Orion
    """
    url = f"{orion_url}/{entity_id}?type={entity_type}"
    
    response = requests.delete(url)
    
    if response.status_code == 204:
        print(f"Entyty {entity_id} has been deleted")
    else:
        print(f"Error tryong to delete {entity_id}: {response.status_code}, {response.text}")

def publish_entity(entity_id, entity_type, attributes):
    """
    Publish an entity in Orion
    """

    entity = {
        "id": entity_id,
        "type": entity_type,
    }


    for attr_name, attr_data in attributes.items():
        cleaned_value = clean_value(attr_data['value'], attr_data['type'])
        entity[attr_name] = {
            "type": attr_data['type'],
            "value": cleaned_value
        }

    response = requests.post(orion_url, json=entity, headers={'Content-Type': 'application/json'})

    if response.status_code == 201:
        print(f"Entity {entity_id} has been published")
    else:
        print(f"Error trying to publish {entity_id}: {response.status_code}, {response.text}")

def publish_entities_from_list(entities):
    """
    Iterates on the dict list and publish all entities
    """
    for entity_data in entities:
        entity_id = entity_data['entityID']['value']  
        entity_type = entity_data['entityType']['value']  
        attributes = {key: value for key, value in entity_data.items() if key not in ['entityID', 'entityType']}
        publish_entity(entity_id, entity_type, attributes)
