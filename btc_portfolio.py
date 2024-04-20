class BtcPortfolio:
    _usd_value: float
    _btc_amount: float

    def __init__(self, holdings_usd_value: float = 0, holdings_btc_amount: float = 0) -> None:
        self._usd_value = holdings_usd_value
        self._btc_amount = holdings_btc_amount

    # Transact
    
    def buy_btc(self, btc_amount: float, usd_value: float):
        self._usd_value += usd_value
        self._btc_amount += btc_amount
    
    def sell_btc(self, btc_amount: float):
        self._usd_value -= self.local_usd_value_estimate(btc_amount)
        self._btc_amount -= btc_amount
    
    # Explore
    
    def selling_pnl(self, btc_amount: float, usd_value: float):
        pnl = usd_value - self.local_usd_value_estimate(btc_amount)
        return pnl, pnl/self._usd_value # usd, %
    
    def local_usd_value_estimate(self, btc_amount: float):
        return self.holdings_price * btc_amount

    @property
    def holdings_usd_value(self):
        return self._usd_value
    
    @property
    def holdings_btc_amount(self):
        return self._btc_amount
    
    @property
    def holdings_price(self):
        return self._usd_value / self._btc_amount

    def holdings_pnl(self, price: float):
        # price - usd/btc
        # returns pnl if all the current holding will be sold right now
        return self.selling_pnl(self._btc_amount, price*self._btc_amount)