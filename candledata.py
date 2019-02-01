
import os.path
import config, helpers

from requests import get

def pull(periodicity, instrument, year):
    taskname = '{}/{}/{}'.format(periodicity, instrument, year)
    basedir = os.path.join(config.data_dir, taskname)
    helpers.guarantee(basedir)
    
    for w in config.weeks:
        url = helpers.compose_url(periodicity, instrument, year, w)
        savepath = os.path.join(basedir, '{}.csv.gz'.format(w))
        print('Downloading {}'.format(url))

        tries = 0
        while tries < 5:
            r = get(url, allow_redirects=True)
            if r.status_code == 404:
                print('{} not found.'.format(url))
                break
            if r.status_code != 200:
                tries = tries + 1
                continue
            print('Saving to {}'.format(savepath))
            open(savepath, 'wb').write(r.content)
            break

        if tries == 5:
            print('Failed to download {}'.format(url))
