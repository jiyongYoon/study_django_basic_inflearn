from redis import Redis


def getConn():

    REDIS_HOST = 'localhost'
    # REDIS_HOST = '172.25.110.76'
    REDIS_PORT = 6379
    REDIS_PASSWORD = None

    return Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)


conn = getConn()
print(conn)
