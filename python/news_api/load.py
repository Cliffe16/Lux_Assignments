import pandas as pd
from sqlalachemy import create_engine
from config import DB_USER, DB_PASS, DB

#Initialize db conncetion engine
engine = create_engine("postgresql+psycopg2://{DB_USER}:{DB_PASS}@localhost:5432/{DB}
    ")

def load_news(transformed_data):
    # Skip if no data is returned
    if not transformed_data:
        print("No data to load")

    # Convert articles to dataframe
    df = pd.DataFrame(transformed_data)

    # Load data to database
    df.to_sql("articles", 
                con=engine, 
                if_exists="append",
                index = False
            )

    # Confirm Load
    print("Rows:", len(df), "loaded")
    
