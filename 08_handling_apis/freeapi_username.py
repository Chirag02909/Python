import requests

def fetch_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        dob = user_data["dob"]["date"]
        country = user_data["location"]["country"]
        location = user_data["location"]["street"]["name"]
        phone = user_data["phone"]
        return username, dob, country, location, phone
    else:
        raise Exception("Failed to fetch user data")


def main():
    try:
        username, dob, country, location, phone = fetch_user()
        print(f"Username: {username}, \nDob: {dob}, \nCountry: {country}, \nLocation: {location}, \nPhone: {phone}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()