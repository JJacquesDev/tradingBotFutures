"""
Created 13 september 2025
Author: Jean-Jacques BABIN-DAMANA
license: MIT
purpose : Trade execution according to company adapter
"""
class ExecutionEngine:
    def __init__(self, adapter):
        self.adapter = adapter

    def send_order(self, symbol, qty, side, order_type="market", price=None):
        return self.adapter.place_order(symbol, qty, side, order_type, price)

    def cancel_order(self, order_id):
        return self.adapter.cancel_order(order_id)
