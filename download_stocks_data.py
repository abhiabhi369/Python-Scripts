from datetime import datetime, timedelta, date
from jugaad_data.nse import stock_df

today = datetime.now()
today_date = today.day
today_month = today.month
today_year = today.year

one_year_ago = today - timedelta(days=365)
one_year_ago_date = one_year_ago.day
one_year_ago_month = one_year_ago.month
one_year_ago_year = one_year_ago.year

df = stock_df(symbol="SBIN", from_date=date(one_year_ago_year, one_year_ago_month, one_year_ago_date),
            to_date=date(today_year, today_month, today_date), series="EQ")
print(df.head())
df.to_excel('test.xlsx')

