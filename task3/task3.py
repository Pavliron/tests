import json
import sys

def load_json(json_file):
    with open(json_file, 'r') as file:
        return json.load(file)

def save_json(data, json_file):
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=2)

def fill_values(tests, values):
    for test in tests['tests']:
        test_id=test['id']
        for value in values['values']:
            if test_id==value['id']:
                test['value']=value['value']
                if 'values' in test:
                    test_values=test['values']
                    if isinstance(test_values,dict):
                        for t in test_values:
                            fill_values(test_values,values)
                            break
        
            
def main(values_path, tests_path, report_path):
    values = load_json(values_path)
    tests = load_json(tests_path)
    fill_values(tests, values)
    save_json(tests, report_path)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Неверное количество аргументов")
        sys.exit(1)
    
    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]
    
    main(values_path, tests_path, report_path)