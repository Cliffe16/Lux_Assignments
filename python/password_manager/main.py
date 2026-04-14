import csv

def store_creds():
    # Iterate over inputs
    while True:
        website = input("Enter website: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
    
        # Create credentials dictionary 
        credentials = {}

        # Define dictionary keys
        credentials['website'] = website
        credentials['username'] = username
        credentials['password'] = password

        # Confirm dictionary is populated
        print("\nCredentials stored: ", credentials)

        # Store credentials in a csv file
        with open("credentials.csv", "a", newline="") as file:
            write = csv.writer(file)
            for key, value in credentials.items():
                write.writerow([key, value])
        print("File 'credentials.csv' written successfully")

        try:
            # Get password by passing a website
            web_pass = input("\nEnter the website name to get password: ")
            if web_pass in credentials['website']:
                print (credentials['password'])

            # List all websites
            web_choice = input("\nWould you like to see all websites stored? (y/n): ")
            if web_choice == 'yes' or 'y':
                print(credentials['website'])

            # Program termination
            choice = input("\n\nDo you wish to continue? (y/n): ")
            if choice == 'no' or choice == 'n':
                print("Exiting password manager...")
                break
        except FileNotFoundError:
            print("File not found.")


if __name__ == "__main__":
    store_creds()
