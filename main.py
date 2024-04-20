from btc_portfolio import BtcPortfolio
from models import Tx


txs = [
    Tx(income=True, usd_value=100, btc_amount=2),
    Tx(income=False, usd_value=70, btc_amount=1),
]

portfolio = BtcPortfolio()

for tx in txs:
    if tx.income:
        portfolio.buy_btc(tx.btc_amount, tx.usd_value)
        print(f"Bought {tx.btc_amount} btc at {tx.usd_value} usd")
    else:
        pnl_usd, pnl_percent = portfolio.selling_pnl(tx.btc_amount, tx.usd_value)
        print(f"Sold {tx.btc_amount} btc, got {pnl_usd:.1f} usd ({pnl_percent*100:.1f}%) PnL")
        portfolio.sell_btc(tx.btc_amount)

print()
price = float(input("Enter current btc price: "))
pnl_usd, pnl_percent = portfolio.holdings_pnl(price)
print(f"Current holdings PnL: {pnl_usd:.1f} usd ({pnl_percent*100:.1f}%) PnL")