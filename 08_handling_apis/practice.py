import requests

def fetch_user():
    url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        quote_data = data["data"]
        author = quote_data["author"]
        content = quote_data["content"]
        length = quote_data["length"]
        tags = quote_data["tags"]
        message = data["message"]
        return author, content, length, tags, message
    else:
        raise Exception("Failed to fetch quote data")

def main():
    try:
        author, content, length, tags, message = fetch_user()
        print(f"Author: {author}\nQuote: {content}\nLength: {length}\nTags: {', '.join(tags)}\nMessage: {message}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
