import requests  
import json

# def get_news(query):  
#     url = 'https://newsapi.org/v2/everything'  
    
#     params = {  
#         'q': query, 
#         'language' : 'en',
#         'apiKey':"11c1fddcce5e4b858d06e1a68a300300"
#     }  
      
#     response = requests.get(url, params=params)  
    
#     if response.status_code == 200:  
#         return response.json()
#     else:  
#         return {'error': response.status_code, 'message': response.text}  



# news_query = input("Enter Query to search news : ")  
# news_data = get_news(news_query)  

 
# if 'error' not in news_data:  
#     for article in news_data['articles']:  
#         print(f"Title: {article['title']}")  
#         print(f"Source: {article['source']['name']}")  
#         print(f"Published at: {article['publishedAt']}")  
#         print(f"Description: {article['description']}")
#         print(f"Contect: {article["content"]}")
#         print(f"URL: {article['url']}\n\n\n")  
# else:  
#     print(f"Error: {news_data['message']}")



# def getn(query):
#     url="https://newsapi.org/v2/everything"

#     params={
#         "q":query,
#         "language":"en",
#         "apiKey":"11c1fddcce5e4b858d06e1a68a300300",

#     }

#     response= requests.get(url,params=params)
#     return response.json()

# news_query = input("Enter Query to search news : ")  
# news_data = getn(news_query)

# for article in news_data['articles']:
#     print(f"Title: {article['title']}") 


query=input("What type of news are you intrested in? : ")
url=f"https://newsapi.org/v2/everything?q={query}&from=2024-11-25&sortBy=publishedAt&apiKey=11c1fddcce5e4b858d06e1a68a300300"
r=requests.get(url)
news=json.loads(r.text)
for article in news['articles']:  
    print(f"Title: {article['title']}")  
    print(f"Source: {article['source']['name']}")  
    print(f"Published at: {article['publishedAt']}")  
    print(f"Description: {article['description']}")
    print(f"Contect: {article["content"]}")
    print(f"URL: {article['url']}\n\n\n")