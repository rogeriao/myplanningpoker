from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from webapp import create_app
from webapp.models import db, User, Vote, Story, Game

app = create_app('webapp.config.DevConfig')

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('server', Server())
manager.add_command('db', MigrateCommand)

@manager.shell
def shell_context():
    return dict(
        app=app,
        db=db,
        User=User,
        Vote=Vote,
        Story=Story,
        Game=Game
    )

if __name__ == "__main__":
    manager.run()
