class Solution:
    def reformatdate(self, date: str) -> str:
        # 解包
        day, mon, year = date.split()
        mon_lst = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        # sequence使用enumerate
        mon_map = {mon: idx for idx, mon in enumerate(mon_lst, 1)}
        # 格式化输出
        return "%s-%02d-%02d" % (year, mon_map[mon], int(day[:-2]))
