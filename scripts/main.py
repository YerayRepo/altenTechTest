# main.py

import os
from read_csv import read_csv
from orion import publish_entities_from_list as publishOrion

def main():

    filePath = '../data/entities.csv'

    if not os.path.exists(filePath):
        print(f"The file {filePath} does not exist")
        return

    entities = read_csv(filePath)

    if entities is not None:
        publishOrion(entities) 

if __name__ == '__main__':
    main()
