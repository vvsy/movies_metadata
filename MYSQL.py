import MySQLdb as mdb

db = mdb.connect('localhost', 'root', '13', 'movies_metadata')

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS movies_metadata")

sql = """CREATE TABLE movies_metadata (
        adult CHAR(255),
        belongs_to_collection VARCHAR(255),
        budget VARCHAR(255),
        genres TEXT,
        homepage VARCHAR(255),
        id VARCHAR(255),
        imdb_id VARCHAR(255),
        original_language VARCHAR(255),
        original_title VARCHAR(255),
        overview LONGTEXT,
        popularity TEXT,
        poster_path VARCHAR(255),
        production_companies TEXT,
        production_countries TEXT,
        release_date VARCHAR(255),
        revenue TEXT,
        runtime VARCHAR(255),
        spoken_languages TEXT,
        status VARCHAR(255),
        tagline TEXT,
        title VARCHAR(255),
        video VARCHAR(255),
        vote_average TEXT,
        vote_count TEXT )"""


cursor.execute(sql)


import pandas as pd

df = pd.read_csv('movies_metadata.csv')

for row in df.iterrows():
    a = row[1].values
    cursor.execute('INSERT INTO movies_metadata(adult,belongs_to_collection, budget,genres,homepage ,id ,imdb_id ,original_language ,original_title ,overview ,popularity ,poster_path ,production_companies ,production_countries ,release_date ,revenue,runtime ,spoken_languages ,status ,tagline ,title ,video ,vote_average ,vote_count)' 'VALUES("%s", "%s", "%s","%s", "%s", "%s","%s", "%s", "%s","%s", "%s", "%s","%s", "%s", "%s","%s", "%s", "%s","%s", "%s", "%s","%s", "%s", "%s")', tuple(a))

db.commit()
#sql = """INSERT INTO movies_metadata("""


db.close()
