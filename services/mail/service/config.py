 

class Config(object):

    JWT_OIDC_WELL_KNOWN_CONFIG = 'https://KEYCLOAK-SERVICE/auth/realms/odonata/.well-known/openid-configuration'
    JWT_OIDC_AUDIENCE = 'ticket-client'
