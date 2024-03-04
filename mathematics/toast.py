import time
import yfinance as yf

def main(rate):
    for _ in range(rate):
        time.sleep(1)
        apple = yf.Ticker("AAPL")
        vanguard_bonds_etf = yf.Ticker("BND")
        
        apple_history = apple.history(period="1mo")

        vanguard_bonds_etf_history = vanguard_bonds_etf.history(period="id")

        print(apple_history['Close'].iloc[-1], vanguard_bonds_etf_history['Close'].iloc[-1])
        #print(vanguard_bonds_etf.info.keys())
        #print(apple.info['exchange'])
        apple_price = apple.info['currentPrice']
        vanguard_bonds_etf_price = vanguard_bonds_etf.info['dayHigh']

        print(apple_price, vanguard_bonds_etf_price)

main(300)
