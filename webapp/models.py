from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

users_games = db.Table(
    'user_game',
    db.Column('user_email', db.String(), db.ForeignKey('user.email')),
    db.Column('game_id', db.Integer(), db.ForeignKey('game.id'))
)

class User(db.Model):
    email         = db.Column(db.String(100), primary_key=True)
    username      = db.Column(db.String(50))
    password      = db.Column(db.String(50))

    owner_games = db.relationship(
        'Game',
        backref='user',
        lazy='dynamic'
    )

    user_games    = db.relationship(
        'Game',
        secondary=users_games,
        backref=db.backref('User', lazy='dynamic')
    )

    votes         = db.relationship(
        'Vote',
        backref='user',
        lazy='dynamic'
    )

    stories       = db.relationship(
        'Story',
        backref='user',
        lazy='dynamic'
    )

    def __init__(self,  email, username):
        self.email = email
        self.username = username

    def __repr__(self):
        return '<user {}>'.format(self.username)

class Game(db.Model):
    id      = db.Column(db.Integer(), primary_key=True)
    title   = db.Column(db.String(100))
    owner   = db.Column(db.String(100), db.ForeignKey('user.email'))
    stories = db.relationship(
        'Story',
        backref='game',
        lazy='dynamic'
    )

    users = db.relationship(
        'User',
        secondary=users_games,
        backref=db.backref('game', lazy='dynamic')
    )

    def __init__(self, title, owner):
        self.title = title
        self.owner = owner

    def __repr__(self):
        return '<Game {}>'.format(self.title)


class Story(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(100))
    created_by  = db.Column(db.String(100), db.ForeignKey('user.email'))
    description = db.Column(db.Text)
    game_id     = db.Column(db.Integer(), db.ForeignKey('game.id'))
    user_votes  = db.relationship(
        'Vote',
        backref='story',
        lazy='dynamic'
    )

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Story {}>'.format(self.title)

class Vote(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    value      = db.Column(db.String(5))
    user_email = db.Column(db.String(100), db.ForeignKey('user.email'))
    story_id   = db.Column(db.Integer(), db.ForeignKey('story.id'))

    def __init__(self, user_email, value, story_id):
        self.user_email = user_email
        self.story_id = story_id
        self.value = value

    def __repr__(self):
        return '<Voted by {}>'.format(self.user_email)
