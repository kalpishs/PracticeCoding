import json
import os
import re
import requests
import logging

def send_message_to_channel_handler(message, response_log_filename):
    url = "https://l9e2z3w5wc.execute-api.us-east-1.amazonaws.com/PRE-DEV"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "x-api-key": "CugyutC2Bk5Q6ePG43hcH6u2e428MRt56YVKXtZg",
    }
    data = {
        "phone_number": "+12708354198",
        "guest_phone_number": "+13156364196",
        "message": message,
        "channel": "ivr",
        "channel_handler_version": "v2",
    }

    try:
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            logging.info("Request was successful: %s", response.json().get("message"))
            with open(response_log_filename, 'a') as response_log:
                response_log.write(response.json().get("message") + "\n")
            return response.json().get("message")
        else:
            logging.error("Request failed with status code: %s", response.status_code)
            return None
    except Exception as e:
        logging.exception("An error occurred during the request: %s", str(e))
        return None

def compare_strings(response, mock_response):
    response = re.sub(r"\s+", "", response)
    mock_response = re.sub(r"\s+", "", mock_response)
    return response == mock_response

def execute_test_cases(ids):
    for id in ids:
        json_file_path = f"{id}.json"
        if os.path.exists(json_file_path):
            with open(json_file_path, 'r') as json_file:
                data = json.load(json_file)

                if data.get("ACTION")== "TESTCASE EXECUTION":
                    test_data = data.get('Test', [])
                    response_log_filename = f"response_{id}.log"
                    for idx, item in enumerate(test_data, start=1):
                        message = item.get('MESSAGE', '')
                        response = send_message_to_channel_handler(message, response_log_filename)
                        print(response)

                        if compare_strings(response, item.get("response_text")):
                            continue
                        else:
                            logging.warning("Test case %d failed", idx)
                            break

if __name__ == "__main":
    logging.basicConfig(filename="test_log.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    ids = [1, 2, 3]  # Example list of IDs
    execute_test_cases(ids)
