from glittr.api import app
from os import getenv
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy


def initialize_db():
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    manager = Manager(app)
    manager.add_command("db", MigrateCommand)

    return db


if __name__ == "__main__":
    """main function for deploy
    """
    db = initialize_db()
    app.run(debug=False)
