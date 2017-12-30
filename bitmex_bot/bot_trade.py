class BOT_TRADE(object):
    def __init__(self, **kwargs):
        self.orderType = kwargs['orderType']
        self.quantity = kwargs['quantity']
        if not self.orderType == "Market":
            self.price = kwargs['price']
            if kwargs['orderType'] in ['StopLimit', 'LimitIfTouched']:
                self.stopPx = kwargs['stopPx']
        self.api_obj = kwargs['obj']
        # sell or buy
        self.side = kwargs['side']
        self.place_trade(**kwargs)

    def place_trade(self, **kwargs):
        # delete dict item obj not needed more
        kwargs.pop('obj')

        return self.api_obj.place_order(**kwargs)