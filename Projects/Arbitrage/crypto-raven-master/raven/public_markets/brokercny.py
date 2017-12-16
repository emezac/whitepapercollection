# Copyright (C) 2016, Philsong <songbohr@gmail.com>

import urllib.request
import urllib.error
import urllib.parse
import json
from .market import Market
import lib.broker_api as exchange_api

class BrokerCNY(Market):
    def __init__(self, base_currency, market_currency, pair_code):
        super().__init__(base_currency, market_currency, pair_code)

        exchange_api.init_broker()

    def update_depth(self):
        depth = {}
        try:
            ticker = exchange_api.exchange_get_ticker()
            depth['asks'] = [[ticker.ask, 30]]
            depth['bids'] = [[ticker.bid, 30]]
        except Exception as e:
            exchange_api.init_broker()
            return

        self.depth = self.format_depth(depth)
