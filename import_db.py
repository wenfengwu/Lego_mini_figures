from miniFig_app import db
import os, json, pprint
from miniFig_app.models.figure import Figure

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# an Engine, which the Session will use for connection
# resources
engine = create_engine('mysql+pymysql://root:rootroot@localhost:3306/minifigs')

counter = 0
# create session and add objects
with Session(engine) as session:
    dataset_path = os.getenv('DATASET_PATH', '/Users/wuwenfeng/Documents/GitHub/lego-set/datasets/minifigure')
    for filename in os.listdir(dataset_path):
        file_path = os.path.join(dataset_path, filename)
        with open(file_path) as f:
            items = json.load(f)
            for i, item in enumerate(items):
                f = Figure()
                f.id = item['id']
                f.img_url = item['img']
                f.name = item['name']
                year = '0'
                category = 'NA'
                for k, v in item['tags'].items():
                    if 'year-' in v:
                        year = k
                    elif '/category-' in v:
                        category = k
                f.year = int(year)
                f.theme = category
                session.merge(f)
                session.commit()

