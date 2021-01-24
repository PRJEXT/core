from dotenv import load_dotenv
from service.ListenerService import ListenerService


def main():
    load_dotenv()

    print("Waiting for reviews")
    ListenerService()

if __name__ == "__main__":
    main()
