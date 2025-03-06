import requests

def test_newsapi(newsapi):
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")  # Check HTTP status code

    if response.status_code == 200:
        data = response.json()
        print("Full API Response:", data)  # Print full response for debugging
    else:
        print("Error fetching data. Check API key or internet connection.")

# Replace "your_newsapi_key" with your actual key
test_newsapi("4d82558b5448424d81ff0391e4f9d522")
