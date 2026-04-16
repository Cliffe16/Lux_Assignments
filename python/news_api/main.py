from extract import extract_news
from transform import transform_news
from load import load_news

def main():
    articles = extract_news()
    transformed_data = transform_news(articles)

    print("Extracting articles...")
    extract_news()
    print("Data Extracted successfully:\n", articles)
    print("--------------------------------------")
    
    print("Transforming data")
    transform_news(articles)
    print("Data transformed successfully\n", transformed_data)

    print("Loading Data...")
    load_news(transformed_data)

if __name__ == "__main__":
    main()
