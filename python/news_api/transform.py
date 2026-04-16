from datetime import datetime

def transform_news(articles):    
    # Initialze an empty list for the transfomred data
    transformed_data = []

    # Iterate through the articles list to append necessary fields
    for article in articles:
        transformed_data.append({
            "source": article.get("source", {}).get("name"),
            "author": article.get("author"),
            "title": article.get("title"),
            "url": article.get("url"),
            "date_published": article.get("publishedAt"),
            "date_loaded": datetime.now()
            })

    return transformed_data
