import os
from dotenv import load_dotenv

load_dotenv()


class Headers:
    basic = {
        "Content-Type": f"application/json",
    }

    update = {
        "Content-Type": f"application/json",
        "Accept": f"application/json",
        "Cookie": f"token={os.getenv('SESSION_TOKEN')}",
    }

    delete = {
        "Content-Type": f"application/json",
        "Cookie": f"token={os.getenv('SESSION_TOKEN')}",
    }

    empty_headers = {

    }
