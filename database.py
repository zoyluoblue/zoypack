import pymongo


class MongoCon:

    def __init__(self, host='localhost', port=27017, username='root', password='321', auth_db='admin', dbname='tmp', colname='tmp',
                 charset='utf8', db_config=None, use_uri=False, uri=None, **kwargs):
        self.auth_db = auth_db
        self.colname = colname
        self.dbname = dbname
        if isinstance(port, str):
            port = int(port)

        if uri:
            self.mongo_con = pymongo.MongoClient(uri)
        elif use_uri and not uri:
            self.mongo_con = pymongo.MongoClient(
                'mongodb://%(username)s:%(password)s@%(host)s:%(port)s/?authSource=%(dbname)s' % {'username': username,
                                                                                              'password': password,
                                                                                              'host': host,
                                                                                              'port': port,
                                                                                              'dbname': auth_db})
        else:
            self.mongo_con = pymongo.MongoClient(host=host, port=port, username=username, password=password,
                                                 authSource=auth_db)

    def db(self, dbname=None):
        dbname = dbname or self.dbname or 'tmp'
        print(dbname)
        return self.mongo_con[dbname]

    def col(self, colname=None, dbname=None):
        dbname = dbname or self.dbname or 'tmp'
        colname = colname or self.colname
        return self.db(dbname)[colname]
