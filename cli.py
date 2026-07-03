import click

from bot.client import BinanceClient
from bot.orders import OrderManager
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)


@click.command()
@click.option("--symbol", required=True, help="Trading symbol (e.g. BTCUSDT)")
@click.option("--side", required=True, help="BUY or SELL")
@click.option("--type", "order_type", required=True, help="MARKET or LIMIT")
@click.option("--quantity", required=True, type=float, help="Order quantity")
@click.option("--price", type=float, help="Price (required for LIMIT orders)")
def main(symbol, side, order_type, quantity, price):
    """Binance Futures Testnet Trading Bot"""

    try:
        # Validate inputs
        symbol = validate_symbol(symbol)
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)
        price = validate_price(price, order_type)

        # Initialize client
        client = BinanceClient().get_client()

        # Place order
        order_manager = OrderManager(client)

        response = order_manager.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
        )

        # Print request summary
        print("\n" + "=" * 50)
        print("ORDER REQUEST SUMMARY")
        print("=" * 50)
        print(f"Symbol      : {symbol}")
        print(f"Side        : {side}")
        print(f"Order Type  : {order_type}")
        print(f"Quantity    : {quantity}")

        if order_type == "LIMIT":
            print(f"Price       : {price}")

        # Print response
        print("\n" + "=" * 50)
        print("ORDER RESPONSE")
        print("=" * 50)
        print(f"Order ID      : {response.get('orderId')}")
        print(f"Status        : {response.get('status')}")
        print(f"Executed Qty  : {response.get('executedQty')}")
        print(f"Average Price : {response.get('avgPrice', 'N/A')}")

        print("\n✅ Order placed successfully!")

    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()