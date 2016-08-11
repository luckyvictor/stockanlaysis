import urllib
import urllib2
import requests
import json

import pyexcel_xls
#https://automatetheboringstuff.com/chapter12/
import ystockquote 

'''
This is the "ystockquote" module.
This module provides a Python API for retrieving stock data from Yahoo Finance.
This module contains the following functions:
get_all(symbol)
get_dividend_yield(symbol)
get_dividend_per_share(symbol)
get_ask_realtime(symbol)
get_dividend_pay_date(symbol)
get_bid_realtime(symbol)
get_ex_dividend_date(symbol)
get_previous_close(symbol)
get_today_open(symbol)
get_change(symbol)
get_last_trade_date(symbol)
get_change_percent_change(symbol)
get_trade_date(symbol)
get_change_realtime(symbol)
get_last_trade_time(symbol)
get_change_percent_realtime(symbol)
get_change_percent(symbol)
get_after_hours_change(symbol)
get_change_200_sma(symbol)
get_commission(symbol)
get_percent_change_200_sma(symbol)
get_todays_low(symbol)
get_change_50_sma(symbol)
get_todays_high(symbol)
get_percent_change_50_sma(symbol)
get_last_trade_realtime_time(symbol)
get_50_sma(symbol)
get_last_trade_time_plus(symbol)
get_200_sma(symbol)
get_last_trade_price(symbol)
get_1_year_target(symbol)
get_todays_value_change(symbol)
get_holdings_gain_percent(symbol)
get_todays_value_change_realtime(symbol)
get_annualized_gain(symbol)
get_price_paid(symbol)
get_holdings_gain(symbol)
get_todays_range(symbol)
get_holdings_gain_percent_realtime(symbol)
get_todays_range_realtime(symbol)
get_holdings_gain_realtime(symbol)
get_52_week_high(symbol)
get_more_info(symbol)
get_52_week_low(symbol)
get_market_cap(symbol)
get_change_from_52_week_low(symbol)
get_market_cap_realtime(symbol)
get_change_from_52_week_high(symbol)
get_float_shares(symbol)
get_percent_change_from_52_week_low(symbol)
get_company_name(symbol)
get_percent_change_from_52_week_high(symbol)
get_notes(symbol)
get_52_week_range(symbol)
get_shares_owned(symbol)
get_stock_exchange(symbol)
get_shares_outstanding(symbol)
get_volume(symbol)
get_ask_size(symbol)
get_bid_size(symbol)
get_last_trade_size(symbol)
get_ticker_trend(symbol)
get_average_daily_volume(symbol)
get_trade_links(symbol)
get_order_book_realtime(symbol)
get_high_limit(symbol)
get_eps(symbol)
get_low_limit(symbol)
get_eps_estimate_current_year(symbol)
get_holdings_value(symbol)
get_eps_estimate_next_year(symbol)
get_holdings_value_realtime(symbol)
get_eps_estimate_next_quarter(symbol)
get_revenue(symbol)
get_book_value(symbol)
get_ebitda(symbol)
get_price_sales(symbol)
get_price_book(symbol)
get_pe(symbol)
get_pe_realtime(symbol)
get_peg(symbol)
get_price_eps_estimate_current_year(symbol)
get_price_eps_estimate_next_year(symbol)
get_short_ratio(symbol)
get_historical_prices(symbol, start_date, end_date)

sample usage:
>>> import ystockquote
>>> print ystockquote.get_price('GOOG')
529.46
'''

url = 'http://www.londonstockexchange.com/statistics/companies-and-issuers/list-of-all-companies.xls'

request = requests.get(url)
#with open("code3.zip", "wb") as code:
#    code.write(r.content)
with open('stocklist.xls") as stocktable:
  stocktable.write(request.content)
  
data = get_data("list-of-all-companies.xls")
print(json.dumps(data))
