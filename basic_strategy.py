### Quantiacs Trend Following Trading System Example
# import necessary Packages below:
import numpy as np

def myTradingSystem(DATE, OPEN, HIGH, LOW, CLOSE, VOL, exposure, equity, settings):
    ''' This system uses trend following techniques to allocate capital into the desired equities'''

    if str(DATE[0]) == '19900102':
         settings['reference_point'] = OPEN[0,-1]
         settings['allocation'] = np.asarray([0.9,0.1])

    reference_point = settings['reference_point']

    move = (CLOSE[0,-1] - reference_point)/reference_point
    sign = 1 if move >= 0 else -1

    num_thresholds = sign*((abs(move)*100)//1)

    if num_thresholds != 0:
        stock_exposure = settings['allocation'][0]
        factor = 0.15 if sign < 0 else 0.1
        new_stock_exposure = min(1, max(0, stock_exposure + factor*num_thresholds))
        settings['allocation'][0] = new_stock_exposure
        settings['allocation'][1] = 1-new_stock_exposure
        settings['reference_point'] = CLOSE[0, -1]


    return settings['allocation'], settings


def mySettings():
    ''' Define your trading system settings here '''

    settings= {}

    # S&P 100 stocks
    '''
    settings['markets']=['CASH','AAPL','ABBV','ABT','ACN','AEP','AIG','ALL',
     'AMGN','AMZN','APA','APC','AXP','BA','BAC','BAX','BK','BMY','BRKB','C',
     'CAT','CL','CMCSA','COF','COP','COST','CSCO','CVS','CVX','DD','DIS','DOW',
     'DVN','EBAY','EMC','EMR','EXC','F','FB','FCX','FDX','FOXA','GD','GE',
     'GILD','GM','GOOGL','GS','HAL','HD','HON','HPQ','IBM','INTC','JNJ','JPM',
     'KO','LLY','LMT','LOW','MA','MCD','MDLZ','MDT','MET','MMM','MO','MON',
     'MRK','MS','MSFT','NKE','NOV','NSC','ORCL','OXY','PEP','PFE','PG','PM',
     'QCOM','RTN','SBUX','SLB','SO','SPG','T','TGT','TWX','TXN','UNH','UNP',
     'UPS','USB','UTX','V','VZ','WAG','WFC','WMT','XOM']
    '''

    # Futures Contracts
    '''
    settings['markets']  = ['CASH','F_AD', 'F_BO', 'F_BP', 'F_C', 'F_CC', 'F_CD',
    'F_CL', 'F_CT', 'F_DX', 'F_EC', 'F_ED', 'F_ES', 'F_FC','F_FV', 'F_GC',
    'F_HG', 'F_HO', 'F_JY', 'F_KC', 'F_LB', 'F_LC', 'F_LN', 'F_MD', 'F_MP',
    'F_NG', 'F_NQ', 'F_NR', 'F_O', 'F_OJ', 'F_PA', 'F_PL', 'F_RB', 'F_RU',
    'F_S','F_SB', 'F_SF', 'F_SI', 'F_SM', 'F_TU', 'F_TY', 'F_US','F_W', 'F_XX',
    'F_YM']
    '''
    #settings['beginInSample'] = '20120506'
    #settings['endInSample'] = '20150506'
    settings['lookback']= 500
    settings['budget']= 10**6
    settings['slippage']= 0.05

    settings['markets'] = ['F_ES', 'F_ZQ']

    return settings

if __name__ == "__main__":
    import quantiacsToolbox
    results = quantiacsToolbox.runts(__file__)