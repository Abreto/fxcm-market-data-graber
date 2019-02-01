
import os.path
import config, helpers

def pull(periodicity, instrument, year):
    taskname = '{}/{}/{}'.format(periodicity, instrument, year)
    basedir = os.path.join(config.data_dir, taskname)
    helpers.guarantee(basedir)
    
    for w in config.weeks:
        print('Downloading /{}/{}.csv.gz'.format(taskname, w))
        pass
