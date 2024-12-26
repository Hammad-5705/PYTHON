import concurrent.futures  
import requests  
import os  

def download_file(url, name):  
    try:  
        print(f"Started Downloading {name}")  
        response = requests.get(url)  
        response.raise_for_status()  # Check for HTTP request errors  
        os.makedirs('files', exist_ok=True)  # Ensure the directory exists  
        with open(f"files/file{name}.jpg", "wb") as file:  
            file.write(response.content)  
        print(f"Finished Downloading {name}")  
        return f"Downloaded: {name}"  # Return a success message  
    except Exception as e:  
        print(f"Failed to download {name}: {e}")  
        return f"Failed: {name}"  # Return a failure message  

url = "https://picsum.photos/2000/3000"  

# Use ThreadPoolExecutor for I/O-bound tasks  
with concurrent.futures.ThreadPoolExecutor() as executor:  
    l1 = [url for _ in range(60)]  # List of URLs (same URL repeated)  
    l2 = [i for i in range(60)]  # List of names (0 to 59)  
    results = executor.map(download_file, l1, l2)  

    for result in results:  
        print(result)  # Print the result of each download