from keycloak import KeycloakAdmin

admin = KeycloakAdmin(server_url="http://localhost:8000/auth/",
                               username='oadmin',
                               password='oadmin',
                               realm_name="Odonata",
                               verify=True)


user = admin.get_users({})
roles = admin.get_realm_roles()
clients = admin.get_clients()

ticket = next((x for x in clients if x['clientId'] == 'ticket-client'), None)
conf = next((x for x in user if x['username'] == 'config'),None)
userRoles = admin.get_client_roles_of_user(client_id=ticket['id'], user_id=conf['id']))


