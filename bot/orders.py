from binance.exceptions import BinanceAPIException
from .logging_config import logger


class OrderManager:
    def __init__(self, client):
        self.client = client

    def place_order(
        self,
        symbol,
        side,
        order_type,
        quantity,
        price=None,
    ):
        try:
            logger.info(
                f"REQUEST | Symbol={symbol}, Side={side}, "
                f"Type={order_type}, Qty={quantity}, Price={price}"
            )

            if order_type == "MARKET":
                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity,
                )
            else:
                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity,
                    price=price,
                    timeInForce="GTC",
                )

            logger.info(f"RESPONSE | {response}")
            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            raise

        except Exception as e:
            logger.exception(f"Unexpected Error: {e}")
            raise