from dataclasses import dataclass, field


@dataclass
class Tx:
    income: bool
    usd_value: float = field(default=0.0)
    btc_amount: float = field(default=0.0)

    def __post_init__(self):
        if self.usd_value < 0:
            raise ValueError("usd_value must be non-negative")
        if self.btc_amount < 0:
            raise ValueError("btc_amount must be non-negative")
