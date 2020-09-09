import functools
import csv


def decorator(func):
    @functools.wraps(func)
    def wrapped(*args):
        lst_d = func(*args)
        print(lst_d)
        with open('file.csv', 'w') as file:
            for j in range(len(lst_d)):
                writer = csv.DictWriter(file, fieldnames=list(lst_d[j][0].keys()))
                writer.writeheader()
                for i in lst_d[j]:
                    writer.writerow(i)

        return lst_d

    return wrapped
