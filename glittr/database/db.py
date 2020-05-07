from glittr.models.db_models import Artist
from os import getenv

# from glittr.models.db_models import Artist, Parent, Child
from flask_sqlalchemy import SQLAlchemy
import json


def get_session(app):
    db = SQLAlchemy(app)
    session = db.session()
    return session


def add_artist(artist: dict, app):
    session = get_session(app)
    artist = Artist.from_dict(artist)
    session.add(artist)
    session.commit()
    return artist.artist_id


def get_artist(artist_id: int, app):
    artist = Artist.query.filter_by(artist_id=artist_id).first_or_404(
        description=f"Cannot find artist_id {artist_id}"
    )
    return json.loads(repr(artist))
