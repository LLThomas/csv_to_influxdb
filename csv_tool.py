import pandas as pd

if __name__ == '__main__':
    # omit ' ' and replace ' ' using T
    with open('/home/thomas/Downloads/data.csv', "r+", encoding="utf-8") as csv_file:
        content = csv_file.read()
    with open('/home/thomas/Downloads/data.csv', "w+", encoding="utf-8") as csv_file:
        csv_file.write(content.replace(' ', 'T'))
    with open('/home/thomas/Downloads/data.csv', "r+", encoding="utf-8") as csv_file:
        content = csv_file.read()
    with open('/home/thomas/Downloads/data.csv', "w+", encoding="utf-8") as csv_file:
        csv_file.write(content.replace('"', ''))

    # replace ' ' using 'Z'
    f = pd.read_csv('/home/thomas/Downloads/data.csv', low_memory=False)
    f['time'] = f.apply(lambda x: x['time']+'Z', axis=1)
    f.to_csv('/home/thomas/Downloads/data.csv', index=False)
