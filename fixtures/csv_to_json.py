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

            if 'author_id' in row:
                row['author_id'] = int(row['author_id'])

            if 'category_id' in row:
                row['category_id'] = int(row['category_id'])

            if "is_published" in row:
                if row["is_published"] == "True":
                    row["is_published"] = True
                else:
                    row["is_published"] = False

            if 'lat' in row:
                row['lat'] = float(row['lat'])

            if 'lng' in row:
                row['lng'] = float(row['lng'])

            if 'age' in row:
                row['age'] = int(row['age'])

            if 'location_id' in row:
                row['location_id'] = int(row['location_id'])

            record['fields'] = row
            json_array.append(record)

    with open(json_file, 'w', encoding='utf-8') as json_f:
        json_f.write(json.dumps(json_array, ensure_ascii=False))


csv_to_json('location.csv', 'location.json', 'users.location')
csv_to_json('user.csv', 'user.json', 'users.user')
csv_to_json('category.csv', 'category.json', 'ads.category')
csv_to_json('ad.csv', 'ads.json', 'ads.ad')
