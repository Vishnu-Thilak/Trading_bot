import logging

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "recvWindow": 5000
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        logging.info(f"Sending order: {params}")

        response = client.create_order(**params)

        if not response:
            raise RuntimeError("Empty response received from Binance API")

        logging.info(f"Response: {response}")
        return response

    except Exception as e:
        logging.error(f"Error placing order: {str(e)}")
        raise