from ldap3 import Server, Connection, AUTO_BIND_NO_TLS

LDAP_URL = '192.168.100.4'

# Check user authentication in the LDAP and return his information
def get_LDAP_user(username, password):
    try:
        server = Server(LDAP_URL, use_ssl=False)
        connection = Connection(server,
                                'PBRUSSELS\\{username}'.format(
                                    username=username),
                                password=password, auto_bind=AUTO_BIND_NO_TLS)

        connection.search('dc=pbrussels,dc=lan', '({attr}={login})'.format(
            attr='uid', login=username), attributes=['cn'])
        print(connection.response)
        if len(connection.response) == 0:

            return None

        return connection.response[0]
    except Exception as err:

        return None