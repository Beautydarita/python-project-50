from gendiff import generate_diff
from os import path

def test_gendiff():
    path_dir = path.dirname(path.abspath(__file__))
    path1 = path.join(path_dir, 'fixtures', 'file1.json')
    path2 = path.join(path_dir, 'fixtures', 'file2.json')
    path_result = path.join(path_dir, 'fixtures', 'result_json.txt')
    actual = generate_diff(path1, path2)
    expected = open(path_result).read()
    assert actual == expected
    



