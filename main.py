station = []
out = []
x = 0
i = 0
#รับข้อมูลเข้า
while i!=1:
    a = str(input())
    i = len(a)
    if i > 10:
        station.append(a)
    else:
        search = str(a)
        break
#ค้นหาสถานีที่ติดกับสถานีปัจจุบัน
while x <= len(station) - 1:
    if search in station[x]:
        out.append(station[x].replace(search,'').replace(" ",''))
        station[x] = ""
    x+=1
#ค้นหา2สถานีถัดจากสถานีปัจจุบัน
S = len(station)
O = len(out)
a = 0
for y in out:
    i = 0
    if a > O-1:
        break
    for x in station:
        i+=1
        if y in x:
            out.append(x.replace(y,''))
            break
        if i > S:
            break
    a+=1
#จัดเรียงข้อมูล
out.append(search)
out = sorted(out)
print(out)
