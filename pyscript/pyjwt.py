import jwt
import datetime
import time

payload = {
    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=10),
    'name': 'Le Quang Sang',
    'age': 21,
    'adress': 'Can Tho'
}
encoded = jwt.encode(payload, 'secret', algorithm='HS256')
count = 0
while(1):
    try:
        decoded = jwt.decode(encoded, 'secret', algorithms=['HS256'])
        print(decoded)
        print(count)
        count += 1
    except:
        print("An exception occurred")
        break
    time.sleep(1)

