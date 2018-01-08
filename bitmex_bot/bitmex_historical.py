import requests
import json
import settings as s


class Bitmex(object):

    def __init__(self):
        self.trade_currency = "XBT"
        self.ask_price = 0
        self.bid_price = 0
        self.order_id_prefix = "lee_bot"
        self.symbol = s.SYMBOL
        self.BASE_URL = "https://www.bitmex.com/api/v1/"

    def get_historical_data(self, tick='1m', count=400):
        # last one hour data with latest one in the end

        url = self.BASE_URL + "trade/bucketed?binSize={}&partial=false&symbol={}&count={}&reverse=true". \
            format(tick, self.trade_currency, count)
        r = json.loads(requests.get(url).text)

        lst = []
        # configure result into suitable data type
        try:
            dict_key = ["open", "close", "high", "low", "timestamp"]
            for item in r:
                d = {
                    dict_key[0]: item[dict_key[0]],
                    dict_key[1]: item[dict_key[1]],
                    dict_key[2]: item[dict_key[2]],
                    dict_key[3]: item[dict_key[3]],
                    dict_key[4]: item[dict_key[4]]
                }
                lst.append(d)
            return lst[::-1]
        except KeyError as e:
            pass
        except TypeError as e:
            pass
        except Exception as e:
            pass

# b = Bitmex()
# b.get_price()
# # print(b.ask_price, b.bid_price)
# b.place_order(price=b.bid_price, side='Buy', orderQty=100, type="Market")
# # b.cancel_all_order()
# print(b.get_historical_data())
