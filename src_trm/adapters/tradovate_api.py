"""
Created 13 september 2025
Author: Jean-Jacques BABIN-DAMANA
license: MIT
purpose : Tradovate API for futures
"""
class TradovateAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        # init connexion WebSocket + REST Tradovate

    def place_order(self, symbol, qty, side, order_type="market", price=None):
        # implémentation spécifique Tradovate
        pass

    def cancel_order(self, order_id):
        # implémentation spécifique Tradovate
        pass