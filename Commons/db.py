import mysql.connector

import click
from flask import current_app, g
from flask.cli import with_appcontext

from Commons.schema import instructions

def getDB():
    if 'db' not in g:
        g.db=mysql.connector.connect( 
            host=current_app.config['DATABASE_HOST'],
            user=current_app.config['DATABASE_USER'],
            password=current_app.config['DATABASE_PASSWORD'],
            database=current_app.config['DATABASE']
        )
        
        g.c = g.db.cursor(dictionary=True)
    return g.db, g.c

def init_db():
    db, c = getDB()
    
    for i in instructions:
        c.execute(i)
    db.commit()

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')

def closeDB(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(closeDB)
    app.cli.add_command(init_db_command)
    