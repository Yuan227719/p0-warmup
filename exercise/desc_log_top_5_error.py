log = """2026-09-11 21:00:01 INFO [gateway] request served in 32ms
2026-09-11 21:00:04 ERROR [auth] E5001 token expired
2026-09-11 21:00:09 ERROR [payment] E5001 gateway timeout
2026-09-11 21:00:15 WARN [cache] miss ratio high
2026-09-11 21:00:22 ERROR [auth] E4002 invalid signature
2026-09-11 21:00:30 ERROR [order] E5001 downstream timeout
2026-09-11 21:00:41 INFO [gateway] request served in 41ms
2026-09-11 21:00:45 ERROR [db] E1004 connection reset
2026-09-11 21:00:52 ERROR [payment] E5001 gateway timeout
2026-09-11 21:01:03 ERROR [db] E3010 slow query 4200ms
2026-09-11 21:01:10 ERROR [auth] E4002 invalid signature
2026-09-11 21:01:18 ERROR [order] E5001 downstream timeout
2026-09-11 21:01:25 WARN [cache] eviction latency high
2026-09-11 21:01:31 ERROR [notify] E8003 sms quota exceeded
2026-09-11 21:01:38 ERROR [notify] E8003 sms provider error
2026-09-11 21:01:40 ERROR [db] E1004 too many connections
2026-09-11 21:01:47 ERROR [payment] E5003 risk control rejected
2026-09-11 21:01:55 ERROR [db] E3010 slow query 5100ms
2026-09-11 21:02:02 ERROR [auth] E5001 token expired
2026-09-11 21:02:10 ERROR [order] E5001 inventory lock timeout
2026-09-11 21:02:19 ERROR [db] E1004 deadlock detected
2026-09-11 21:02:25 ERROR [auth] E4002 invalid signature"""


str = log.splitlines()

error_dict = {}

for line in str:
    value=line.split(' ')
    if 'ERROR' in value:
        error_dict[value[4]] = error_dict.get(value[4], 0) + 1



top5 = sorted(error_dict.items(), key=lambda item: item[1], reverse=True)[:5]


for i in top5: 
    print(f'{i[0]} 出现 {i[1]} 次')



