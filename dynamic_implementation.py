import json

def process_arguments(*args, **kwargs):
    for arg in args:
        print(f"Positional argument: {arg}")

    # Check if 'json_data' key is in kwargs
    if 'json_data' in kwargs:
        try:
            # Parse the JSON data from the 'json_data' key
            json_data = json.loads(kwargs['json_data'])
            print("Parsed JSON data:")
            print(json_data)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON data: {e}")
    else:
        print("No JSON data provided.")

# Example usage
process_arguments(1, 2, 'three', json_data='{"key": "value", "numbers": [4, 5, 6]}')
import json

def process_arguments(*args, **kwargs):
    
    print("_________________________\nargs and kwargs example\n_________________________")
    for arg in args:
        print(f"Positional argument: {arg}")

    # Check if 'json_data' key is in kwargs
    if 'json_data' in kwargs:
        try:
            # Parse the JSON data from the 'json_data' key
            json_data = json.loads(kwargs['json_data'])
            print("Parsed JSON data:")
            print(json_data)
            for json_key, json_value in json_data.items():
                print(f"Processing JSON value for key : {json_key} -> {json_value}")
                triple_ema_condition = False
                volume_condition = False

                if(json_key == 'volume'):
                    if(triple_ema_condition):
                        print("True")
                if(json_key == 'triple_ema'):
                    for element in json_value:
                        print(element)
                
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON data: {e}")
    else:
        print("No JSON data provided.")

# Example usage
process_arguments(1, 2, 'three', json_data='{"volume": "20", "triple_ema": [5, 13, 26]}')


# Code to parse the multiple json implementation
import json

def process_json_data(**kwargs):
    print("_________________________\nMultiple json parse\n_________________________")
    for key, value in kwargs.items():
        if key.endswith('_json'):
            try:
                # Attempt to parse JSON data
                json_data = json.loads(value)
                print(f"Key: {key}, Parsed JSON data:")
                print(json_data)

                for json_key, json_value in json_data.items():
                    print(f"Processing JSON value for key '{key}': {json_key} -> {json_value}")
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON data for key {key}: {e}")

# Example usage
process_json_data(data1_json='{"name": "John", "age": 30}', data2_json='{"city": "New York", "population": 8000000}')


# conditions = [condition1, condition2, condition3]

# # Check if all conditions are true using logical 'and'
# if all(conditions):
#     print("All conditions are satisfied.")
# else:
#     print("Not all conditions are satisfied.")