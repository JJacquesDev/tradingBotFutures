"""
Docstring for dev_dom_analyzer.source_dom_analyzer.classes.real_time_data_signalr
    purpose : Retrieve user and market data in real time from  topstep/projectx api thanks to signal R framework
    author : Jean-Jacques BABIN-DAMANA
    Created : 20/01/2026
    licence : jeanjacquesBD@
"""
# import requests
import asyncio
# Not appropriate python version 3.11 (should be 3.10 but -> signalr not maintened = risk)
# from signalr_aio import HubConnectionBuilder

class Real_time_data:
    """
    Docstring for Real_time_data
    Pick up real time market data
    pick up real time user data

    markethub_url = (
            "https://rtc.topstepx.com/hubs/market"
        )
    """
    def __init__(self, token, markethub_url, contract_identifier):
        self.jwt_token = token
        self.contract_identifier = contract_identifier

        self.marketHubUrl = markethub_url

        self.asyncio.run(the_main())

        async def the_main(self):
            print("Trying to connect to the markethub url....")
            connection = (
                HubConnectionBuilder()
                .with_url(
                    self.marketHubUrl,
                    options={
                        "access_token_factory": lambda: self.jwt_token,
                        "skip_negotiation": True,
                        "transport": "websockets"
                    }
                )
                .with_automatic_reconnect()
                .build()
            )

            # ---- Handlers ----
            connection.on(
                "GatewayQuote",
                lambda contract_id, data: print("Quote:", data)
            )

            connection.on(
                "GatewayTrade",
                lambda contract_id, data: print("Trade:", data)
            )

            connection.on(
                "GatewayDepth",
                lambda contract_id, data: print("Depth:", data)
            )

            await connection.start()

            # ---- Subscriptions ----
            await connection.invoke("SubscribeContractQuotes", self.contract_identifier)
            await connection.invoke("SubscribeContractTrades", self.contract_identifier)
            await connection.invoke("SubscribeContractMarketDepth", self.contract_identifier)

            print("Connected and subscribed")

            # Keep alive
            while True:
                await asyncio.sleep(1)

   
