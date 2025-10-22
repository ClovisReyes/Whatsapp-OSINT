#BY: ClovisReyes

import os
import requests
import json
from dotenv import load_dotenv
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# Load environment variables from the .env file
load_dotenv()

# API key and host from the .env file
api_key = os.getenv('RAPIDAPI_KEY')
api_host = os.getenv('RAPIDAPI_HOST')

# Function to print the JSON with formatting and colors
def print_colored_json(data, level=0):
    indent = "    " * level
    if isinstance(data, dict):
        for key, value in data.items():
            print(f"{indent}{Fore.CYAN}{key}{Style.RESET_ALL}: ", end="")
            print_colored_json(value, level + 1)
    elif isinstance(data, list):
        for item in data:
            print_colored_json(item, level)
    else:
        print(f"{Fore.YELLOW}{data}{Style.RESET_ALL}")

# Function to query WhatsApp data
def query_whatsapp_number(phone_number):
    url = f"https://{api_host}/number/{phone_number}"
    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": api_host
    }
    
    try:
        # Make the GET request to the API
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Get the response in JSON format
        data_response = response.json()
        
        # Print the formatted and colored JSON
        print_colored_json(data_response)
    
    except requests.exceptions.HTTPError as http_err:
        print(f"{Fore.RED}HTTP Error: {http_err}{Style.RESET_ALL}")
    except requests.exceptions.RequestException as req_err:
        print(f"{Fore.RED}Request Error: {req_err}{Style.RESET_ALL}")
    except json.JSONDecodeError:
        print(f"{Fore.RED}Error processing the JSON response.{Style.RESET_ALL}")
    except Exception as err:
        print(f"{Fore.RED}An error occurred: {err}{Style.RESET_ALL}")

def main():
    # Green banner
    print(Fore.GREEN + """
     __i
    |---|    
    |[_]|    
    |:::|    
    |:::|    
    `\\   \\   
      \\_=_\\ 
    WhatsApp Number Data Query
    """ + Style.RESET_ALL)

    number_input = input("Enter the phone number (with country code): ")
    
    # Validate if a number was entered
    if not number_input.strip():
        print("You must enter a valid phone number.")
        return
    
    # Query number data
    query_whatsapp_number(number_input)

if __name__ == "__main__":
    main()
