import pandas as pd

if __name__ == '__main__':
    # omit ' ' and replace ' ' using T
    with open('/Users/thomas/Downloads/test.csv', "r+", encoding="utf-8") as csv_file:
        content = csv_file.read()
    with open('/Users/thomas/Downloads/test.csv', "w+", encoding="utf-8") as csv_file:
        csv_file.write(content.replace(' ', 'T'))
    with open('/Users/thomas/Downloads/test.csv', "r+", encoding="utf-8") as csv_file:
        content = csv_file.read()
    with open('/Users/thomas/Downloads/test.csv', "w+", encoding="utf-8") as csv_file:
        csv_file.write(content.replace('"', ''))

    # replace ' ' using 'Z'
    f = pd.read_csv('/Users/thomas/Downloads/test.csv', header=None)
    i = 0
    for row in f[1]:
        row = row + 'Z'
        f[1][i] = row
        i = i + 1
    f.to_csv('/Users/thomas/Downloads/test.csv', header=False, index=False)
