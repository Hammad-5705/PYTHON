import asyncio  
import requests
import os

async def fx1():   
    url = 'https://cdn.analyticsvidhya.com/wp-content/uploads/2021/07/38787wallpaper.png'   
    directory = "C:/Users/Lenovo/Desktop" 
    response = requests.get(url)  
    if response.status_code == 200:  
        with open(os.path.join(directory, 'image.jpg'), 'wb') as file:  
            file.write(response.content)  
    else:  
        print("Failed to retrieve the image.")

async def fx2():  
    url = 'https://blog.eduonix.com/wp-content/uploads/2018/09/Scientific-Python-Scipy-696x500.jpg'   
    directory = "C:/Users/Lenovo/Desktop" 
    response = requests.get(url)  
    if response.status_code == 200:  
        with open(os.path.join(directory, 'image.jpeg'), 'wb') as file:  
            file.write(response.content)  
    else:  
        print("Failed to retrieve the image.")

async def main():  
    await asyncio.gather(  
        fx1(),  
        fx2(),  
    )  

if __name__ == "__main__":  
    asyncio.run(main())