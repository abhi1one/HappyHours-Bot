import sqlite3
from pybotframework.botframework import BotFramework
from pybotframework.regex_connector import RegexConnector
from pybotframework.luis_connector import LUISConnector
from pybotframework.result_formatter import ResultFormatter
from pybotframework.db_utils import  DBUtils

#regex_conn = RegexConnector(intent_file='regex.json', response_file='responses.json')
luis_conn = LUISConnector(None)
rformatter=ResultFormatter()
DATABASE = "/Users/tskumar/Downloads/hh.db"
my_app = BotFramework(connectors=[luis_conn],formatter=rformatter)
db_utils = DBUtils()

if __name__ == '__main__':
    # Connect to database
    try:
        print('connect to database')
        connection = sqlite3.connect(DATABASE)
        print('Calling create_tables')
        ret = db_utils.create_tables(connection)
        print("Calling list_data ")
        db_utils.list_data(connection,None)
    except Exception as ex:
        print('Unable to complete DB activities')
        print(ex.with_traceback(None))
    finally:
        connection.close()
    print('Starting flask')
    # Run flask app on port specified here
    my_app.run_server(host='localhost', port=3978, debug=True)
