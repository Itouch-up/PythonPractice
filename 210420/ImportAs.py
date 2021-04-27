# 긴 모듈의 이름을 간략히 부르는 별명을 붙여주는 방법
import datetime as dt
today = dt.date.today()
print('오늘은 {}년 {}월 {}일입니다.'.format(today.year, today.month, today.day))
xMas = dt.datetime(2021, 12, 25)
time_gap = xMas-dt.datetime.now()
print('다음 크리스마스 까지는 {}일 {}시간 남았습니다.'.format(
    time_gap.days, time_gap.seconed//3600))
