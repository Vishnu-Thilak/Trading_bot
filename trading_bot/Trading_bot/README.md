# Binance Futures Testnet Trading Bot

## Setup

1. Create Binance Futures Testnet account
2. Generate API keys
3. Set environment variables:

export BINANCE_API_KEY=your_key
export BINANCE_API_SECRET=your_secret

4. Install dependencies:
pip install -r requirements.txt

## Run Examples

Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit Order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

## Assumptions

The user has an active Binance Futures Testnet (USDT-M) account.

API credentials are generated from Binance Futures Testnet and stored securely as environment variables:

BINANCE_API_KEY

BINANCE_API_SECRET

The trading symbol provided (e.g., BTCUSDT) is valid and available on the Futures Testnet.

The account has sufficient balance and margin to place the requested order.

Quantity and price values provided by the user follow the symbol’s precision rules.

This application supports only MARKET and LIMIT order types.

The project is intended for demonstration and evaluation purposes, not for live or production trading.