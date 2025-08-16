import requests

def fetch_upcoming_launches():
    url = "https://api.spacexdata.com/v4/launches/upcoming"
    response = requests.get(url)
    data = response.json()

    if isinstance(data, list) and len(data) > 0:
        for launch in data:
            name = launch["name"]
            date = launch["date_utc"]
            rocket_id = launch["rocket"]
            launchpad_id = launch["launchpad"]
            webcast = launch["links"]["webcast"] if launch["links"]["webcast"] else "No webcast available"

            print(f"Mission Name: {name}")
            print(f"Launch Date (UTC): {date}")
            print(f"Rocket ID: {rocket_id}")
            print(f"Launchpad ID: {launchpad_id}")
            print(f"Webcast: {webcast}")
            print("-" * 50)
    else:
        raise Exception("No upcoming launches found or invalid response.")

def main():
    try:
        fetch_upcoming_launches()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
