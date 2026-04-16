from datetime import datetime

def transform_news(articles):
    # Initialze an empty list for the transfomred data
    transformed_data = []

    # Iterate through the articles list to append necessary fields
    for article in articles:
        transformed_data.append({
            "source": articles.get("source", {}).get("name"),
            "author": articles.get("author"),
            "title": articles.get("title"),
            "url": articles.get("url"),
            "date_published": articles.get("publishedAt"),
            "date_loaded": datetime.now()
            })

    return transformed_data
