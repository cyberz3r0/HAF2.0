def analyze_photo(photo_path):
    import json
    import requests
    from decouple import config

    url = "https://api.mindee.net/v1/products/mindee/expense_receipts/v5/predict"

    with open(photo_path, "rb") as myfile:
        files = {"document": myfile}
        headers = {"Authorization": config('api_key')}
        response = requests.post(url, files=files, headers=headers)
        response_dict = json.loads(response.text)
        response_data = response_dict['document']['inference']['pages'][0]['prediction']
    return response_data
    # print(response_data['line_items']) #line_items
    # print(response_data['total_net']) #subtotal
    # print(response_data['taxes']) #taxes
    # print(response_data['total_amount']) #total_amount
    # print(response_data['tip']) #tip