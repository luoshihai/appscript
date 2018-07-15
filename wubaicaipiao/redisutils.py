import redis

redis_config = {
    "host": "47.98.232.95",
    "port": 6379
}
# redis连接对象

redis_pool = redis.ConnectionPool(**redis_config)
r = redis.Redis(connection_pool=redis_pool)


# print(str(r.sadd("aa", "alpha")))

# 0 表示已经存在  1 表示不存在
def insert_str(name):
    if name == "" or name is None or len(name) == 0:
        return 1
    return r.sadd("name", name)


