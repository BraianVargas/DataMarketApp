from sqlalchemy import create_engine

from .mainController import *
from .etlController import *
from . import apraBP


@apraBP.route('/historical')
def getHistorical():
    return process_data("historicos")

@apraBP.route('/monthly')
def getMonthly():
    return process_data("mensuales")

@apraBP.route('/etl')
def loadEtl():
    engine = create_engine('mysql+mysqlconnector://root@localhost/datamarket', connect_args={'connect_timeout': 120})
    return loadDatabase(engine)
