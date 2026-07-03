# Binance Futures Testnet Trading Bot

## Overview

This project is a Python-based command-line trading bot that interacts with the Binance USDT-M Futures Testnet. It allows users to place both Market and Limit orders through a simple CLI while maintaining a clean project structure, input validation, logging, and exception handling.

This project was developed as part of a technical assessment.

---

## Features

* Place **Market Orders**
* Place **Limit Orders**
* Supports both **BUY** and **SELL**
* Command-line interface using Click
* Input validation
* Structured project architecture
* API request and response logging
* Exception handling for API and network errors
* Uses Binance USDT-M Futures Testnet

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── config.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
├── logs/
│   └── trading.log
│
├── .env
├── .gitignore
├── cli.py
├── requirements.txt
└── README.md
```

---

## Requirements

* Python 3.10 or later
* Binance Futures Testnet account
* Binance Futures Testnet API Key
* Binance Futures Testnet Secret Key

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd trading_bot
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Configure API Credentials

Create a `.env` file in the project root.

```text
BINANCE_API_KEY=YOUR_API_KEY
BINANCE_API_SECRET=YOUR_API_SECRET
```

Replace the placeholders with your Binance Futures Testnet API credentials.

---

## Running the Application

### Market Buy

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Market Sell

```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

### Limit Buy

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 90000
```

### Limit Sell

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

---

## Example Output

```text
==================================================
ORDER REQUEST SUMMARY
==================================================
Symbol      : BTCUSDT
Side        : BUY
Order Type  : MARKET
Quantity    : 0.001

==================================================
ORDER RESPONSE
==================================================
Order ID      : 123456789
Status        : FILLED
Executed Qty  : 0.001
Average Price : 104235.50

Order placed successfully!
```

---

## Logging

The application automatically creates a log file:

```text
logs/trading.log
```

The log contains:

* API request details
* API response details
* Errors and exceptions
* Timestamp for each operation

---

## Error Handling

The application handles:

* Invalid user input
* Invalid order types
* Missing price for Limit orders
* Binance API errors
* Network and unexpected exceptions

---

## Assumptions

* The application uses the Binance USDT-M Futures Testnet.
* Users have a valid Testnet account and API credentials.
* API credentials are stored securely in a `.env` file.
* Internet connectivity is available while placing orders.

---

## Future Improvements

* Support for additional order types (Stop Market / Stop Limit)
* Interactive CLI menu
* Position monitoring
* Order cancellation
* Trade history
* Unit tests
* Docker support

---

## Author

Developed as part of a Python backend technical assessment demonstrating clean code structure, reusable components, input validation, logging, and Binance Futures Testnet integration.
