import os

def parse_env():
    with open(".env", "r") as f:
        data = f.read()

    for line in data.split('\n'):
        # skip syntax errors
        if '=' not in line:
            continue
        
        # skip empty lines
        if not line:
            continue

        # skip comments
        if line[0] == '#':
            continue

        idx = line.find('=')
        key, value = line[:idx], line[idx+1:]

        os.environ[key] = value
