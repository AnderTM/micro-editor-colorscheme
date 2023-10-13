import os
import json


def find_schemes_files():
    schemes_dir_name = 'colorschemes'
    schemes_dir = os.path.join(os.getcwd(), schemes_dir_name)

    schemeFiles = []
    for file_name in os.listdir(schemes_dir):
        schemeFiles.append(file_name)  
    
    with open('scheme_files.json', 'w') as json_file:
        json.dump(schemeFiles, json_file, indent=2)


def main():
    find_schemes_files()


if __name__ == '__main__': 
    main()
