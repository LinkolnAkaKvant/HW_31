import csv
import json


def csv_to_json(csv_file, json_file, model):
    json_array = []
    with open(csv_file, encoding='utf-8') as csv_f:
        for row in csv.DictReader(csv_f):
            record = {'model': model, 'pk': row["id"]}
            del row['id']

            if "price" in row:
                row["price"] = int(row['price'])

            if "is_published" in row:
                if row["is_published"] == "True":
                    row["is_published"] = True
                else:
                    row["is_published"] = False

            record['fields'] = row
            json_array.append(record)

    with open(json_file, 'w', encoding='utf-8') as json_f:
        json_f.write(json.dumps(json_array, ensure_ascii=False))


csv_to_json('ads.csv', 'ads.json', 'ads.ad')
csv_to_json('categories.csv', 'categories.json', 'ads.category')
