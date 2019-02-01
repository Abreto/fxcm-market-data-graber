
import os
import config

def guarantee(path):
    os.system('mkdir -p "{}"'.format(path))
    # try:
    #     os.mkdir(path)
        
    # except FileExistsError:
    #     pass
    # except:
    #     print('Unexpected error.')
    #     raise

def compose_url(periodicity, instrument, year, week):
    return config.url_pattern.format(
        periodicity=periodicity,
        instrument=instrument,
        year=year,
        week=week
    )
