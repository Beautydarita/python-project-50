import json

def generate_diff(file_path1, file_path2):
    result = ''
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))
    unique_keys = sorted(set(data1.keys()) | set(data2.keys()))

    for key in unique_keys:
        if key not in data1:
            result += f'+ {key}: {data2[key]}\n'
        elif key not in data2:
            result += f'- {key}: {data1[key]}\n'
        elif data1[key] == data2[key]:
            result += f'  {key}: {data1[key]}\n'
        elif data1[key] != data2[key]:
            result += f'- {key}: {data1[key]}\n'
            result += f'+ {key}: {data2[key]}\n'

    return '{\n' + result + '}'

    
    



