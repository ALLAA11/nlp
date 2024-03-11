import csv
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

def read_csv(file_path):
    dataset = []
    with open(file_path, 'r', newline='', encoding='ISO-8859-1') as file:
        reader = csv.reader(file)
        for row in reader:
            dataset.append(row)
    return dataset

def tokenize_and_stem(text):
    tokens = word_tokenize(text)
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return stemmed_tokens

def process_dataset(dataset):
    processed_dataset = []
    for row in dataset:
        processed_row = []
        for column in row:
            processed_column = tokenize_and_stem(column)
            processed_row.append(processed_column)
        processed_dataset.append(processed_row)
    return processed_dataset

def main():
    file_path = 'C:\\Users\\DELL\\Desktop\\task 2\\alldata_1_for_kaggle.csv'  
    dataset = read_csv(file_path)
    processed_dataset = process_dataset(dataset)
    for row in processed_dataset:
        print(row)

if __name__ == "__main__":
    main()
