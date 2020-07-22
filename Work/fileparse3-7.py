# fileparse.py
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):

    f = open(filename)
    rows = csv.reader(f)

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        headers = next(rows) if has_headers else []

        if select:
            indices = [ headers.index(colname) for colname in select ]
            headers = select

        records = []
        for row in rows:
            if not row:    
                continue

            if select:
                row = [ row[index] for index in indices]

            if types:
                row = [func(val) for func, val in zip(types, row)]

            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

        return records