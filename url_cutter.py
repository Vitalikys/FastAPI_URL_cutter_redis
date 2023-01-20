# https://pythontic.com/database/redis/introduction

import redis
import json

redis_client = redis.StrictRedis(host='localhost', port=63791, db=2)
my_data = {
    'target_url': 'google.com',
    'short_url': 'GKI3DTE23',
    'created_at': '12.34.2022',
    'clicks': 0
}
if redis_client.exists('url_1'):
    raise FileExistsError
else:
    redis_client.hset('url_1', 'target_url', 'google.com 2 ')
    redis_client.hset('url_1', 'short_url', 'GKI3DTE23 2')

print('hkeys', redis_client.hkeys('url_1'))  # KEYS
print('hvals', redis_client.hvals('url_1'))  # VAlUES
print('hgetall', redis_client.hgetall("url_1"))

# Retrieve the value for a specific key
print("\n Value for the key 'target_url' is:")
print(redis_client.hget("url_1", "target_url"))


# redis_client.execute_command('JSON.SET', 'url_1', '.', json.dumps(my_data))
# reply = json.loads(redis_client.execute_command('JSON.GET', 'object'))
# redis_client.json().get()
redis_client.close()
