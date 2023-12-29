def analyze_photo(photo_path):
    import requests
    from decouple import config

    url = "https://api.mindee.net/v1/products/mindee/expense_receipts/v5/predict"

    with open(photo_path, "rb") as myfile:
        files = {"document": myfile}
        headers = {"Authorization": config('api_key')}
        response = requests.post(url, files=files, headers=headers)
        print(response.text)
        