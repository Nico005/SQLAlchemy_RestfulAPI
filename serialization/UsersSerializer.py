from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from app.models.UsersModel import Users
from app.models.LogsModel import Logs
from config.database.connection import Connector
from sqlalchemy.orm import sessionmaker



connect = Connector()

from sqlalchemy.orm.scoping import scoped_session
Session = scoped_session(sessionmaker(bind=connect.ConnectorMySql()))





class LogsSchema(ModelSchema):

    class Meta:
        model = Logs
        #sqla_session = Session

class UsersSchema(ModelSchema):

    logs = fields.Nested(LogsSchema,many=True,exclude=('log', ))
    class Meta:
        model = Users
        #sqla_session = Session

