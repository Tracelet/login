import redis
import time

r = redis.StrictRedis(charset="utf-8", decode_responses=True)

# r.set('ip_address', '127.0.0.0')
# r.set('timestamp', int(time.time()))
# r.set('user_agent', 'Opera')
# r.set('last_page_visited', 'home')

print(r.mget("ip_address", "timestamp", "user_agent", "last_page_visited"))
