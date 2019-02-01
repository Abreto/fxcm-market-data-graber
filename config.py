
import os

app_dir = os.getcwd()
data_dir = app_dir + '/data'

url_pattern = ('https://candledata.fxcorporate.com'
    '/{periodicity}/{instrument}/{year}/{week}.csv.gz')

periodicity = ['m1']

instruments = [
    'AUDCAD', 'AUDCHF', 'AUDJPY', 'AUDNZD', 'CADCHF', 'EURAUD',
    'EURCHF', 'EURGBP', 'EURJPY', 'EURUSD', 'GBPCHF', 'GBPJPY',
    'GBPNZD', 'GBPUSD', 'NZDCAD', 'NZDCHF', 'NZDJPY', 'NZDUSD',
    'USDCAD', 'USDCHF', 'USDJPY'
]

years = ['2012', '2013', '2014', '2015', '2016', '2017', '2018']

weeks = list(range(1, 54))
