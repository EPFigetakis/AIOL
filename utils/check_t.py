import yfinance as yf
import mplfinance as mpf 
import pandas as pd


def check_tick(sym):
    tick = yf.Ticker(sym)
    hist = len(tick.history())
    if (hist == 0):
        status = "Not Found"
        return tick, status
    else:
        status = "Found"
        return tick, status



def create_fig(tick):
    period = '7d'
    hist = tick.history(period=period, interval='15m')
    mc = mpf.make_marketcolors(
            up='green',        
            down='red',          
            edge='inherit',      
            wick='inherit',      
            volume='in',         
            ohlc='i'           
        )
    
    STYLE_DICT = {"xtick.color": 'white',
              "ytick.color": 'white',
              "xtick.labelcolor": 'white',
              "ytick.labelcolor": 'white',
              "axes.spines.top": False,
              "axes.spines.right": False,
              "axes.labelcolor": 'white',
              'axes.edgecolor': 'gray'}

    s = mpf.make_mpf_style(
            base_mpf_style='yahoo', 
            marketcolors=mc,        
            figcolor="#0E1117", 
            facecolor="#000000",  
            gridcolor='lightgray',
            gridstyle=':', 
            rc=STYLE_DICT
        )
    
    fig,axlist = mpf.plot(
            hist,
            type='candle',
            mav=(20, 50),
            volume=True,
            style=s,
            ylabel='Price',
            ylabel_lower = 'Volume',
            figscale=.75,
            returnfig = True
        )
    axlist[0].set_title(f"{tick.info['shortName']} Stock Price and Volume ({period})",fontsize=12,color='white')
    return fig