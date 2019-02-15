from sunckSql import SunckSql

s = SunckSql("192.168.1.106","root","zhaozelei110","leige")

res = s.get_all("select * from bandcard where money>400")
for row in res:
    print("%d--%d" % (row[0], row[1]))

