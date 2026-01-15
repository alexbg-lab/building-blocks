import requests, os

if __name__ == "__main__":
    url: str | None = os.getenv("INPUT_URL")

    print("Status Code:", requests.get(url).status_code)
