from db.mongo import *
import json 


class QueueLogic():

    def __init__(self, db):
        self.db = db

    def create(self, queue):
        self.db.create_queue(queue)

    def delete(self, queueId):
        self.db.delete_queue(queueId)

    def get(self):
        return self.db.get_queues()


class MappingLogic():

    def __init__(self, db):
        self.db = db

    def create(self, mapping):
        self.db.create_mapping(mapping)

    def delete(self, mappingId):
        self.db.delete_mapping(mappingId)

    def get(self):
        return self.db.get_mappings()


class UserLogic():

    def __init__(self,admin):
        self.__admin = admin


    def get_by_roles(self, roles):
        if type(roles) != list:
            roles = [roles]
        user = self.__admin.get_users({})
        clients = self.__admin.get_clients()
        conf_service = next((x for x in clients if x['clientId'] == 'config-service'), None)
        
        if not conf_service:
            raise Exception('Config service could not be found, either the connection or the configuration seems to be faulty')

        mail_user = []
        for u in user:
            userRoles = self.__admin.get_client_roles_of_user(client_id=conf_service['id'], user_id=u['id'])
            if any(x for x in userRoles if x['name'] in roles):
                print('iam in ' + u['username'])
                mail_user.append(u['email'])

        return mail_user

class MailLogic():

    def __init__(self,db):
        self.db = db

    def create(self, mapping):
        self.db.create_mail_mapping(mapping)

    def get(self):
        return self.db.get_mail_mappings()

    def delete(self, mailId):
        return self.db.delete_mail_mapping(mailId)
