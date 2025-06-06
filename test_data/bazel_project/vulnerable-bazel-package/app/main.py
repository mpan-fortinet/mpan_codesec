import os

API_KEY = "NRAK-EXAMPLE-1234567890ABCDEF"

def handler():
    print("Leaking environment:")
    print(os.environ)
