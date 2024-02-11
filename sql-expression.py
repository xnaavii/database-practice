from sqlalchemy import (
    create_engine,
    Table,
    Column,
    Float,
    ForeignKey,
    Integer,
    String,
    MetaData,
)

# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData()

# create variable for "artist" table
artist_table = Table(
    "artist",
    meta,
    Column("artist_id", Integer, primary_key=True),
    Column("name", String),
)

# create variable for "artist" table
album_table = Table(
    "album",
    meta,
    Column("album_id", Integer, primary_key=True),
    Column("title", String),
    Column("artist_id", Integer, ForeignKey("artist_table.artist_id")),
)

track_id = Table(
    "track",
    meta,
    Column("track_id", Integer, primary_key=True),
    Column("name", String),
    Column("album_id", Integer, ForeignKey("album_table.album_id")),
    Column("media_type_id", Integer, primary_key=False),
    Column("genre_id", Integer, primary_key=False),
    Column("composer", String),
    Column("milliseconds", Integer),
    Column("bytes", Integer),
    Column("unit_price", Float),
)

# making the solution
with db.connect() as connection:

    # Query 1 - select all records from the "Artist" table
    # select_query = artist_table.select()

    # Query 2 - select only the "Name" column from the "Artist" table
    # select_query = artist_table.select().with_only_columns(artist_table.c.name)

    # Query 3 - Select only 'Queen' from the 'Artist' table
    # select_query = artist_table.select().where(artist_table.c.name == 'Queen')

    # Query 4 - Select only by 'artist_id' #51 from the 'Artist' table
    # select_query = artist_table.select().where(artist_table.c.artist_id == 51)

    # Query 4 - Select only the albums with 'artist_id' #51 on the 'album' table
    # select_query = album_table.select().where(album_table.c.artist_id == 51)

    # Query 5 - Select only the     tracks where 'composer' is 'Queen;
    select_query = track_id.select().where(track_id.c.composer == 'Queen')
    

    results = connection.execute(select_query)
    for result in results:
        print(result)
