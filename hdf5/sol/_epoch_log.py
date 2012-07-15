import numpy as np
import tables as tb

def make_log():
    sec_per_year = 31556900
    secs = np.linspace(-12000.0*sec_per_year, 2301*sec_per_year, 5219500)
    arr = np.zeros(len(secs), dtype=np.dtype([('timestamp', float),
                                              ('crono', bool),
                                              ('marle', bool),
                                              ('lucca', bool),
                                              ('frog', bool),
                                              ('robo', bool),
                                              ('ayla', bool),
                                              ('magus', bool),
                                             ]))
    arr['timestamp'] = secs
    years_present = {'crono': [-12000, 1000, 600, 2300, 1999,],
                     'marle': [-12000, 1000, 600,],
                     'lucca': [1000, 2300, ],
                     'frog': [1000, 600,],
                     'robo': [1000, 2300,],
                     'ayla': [1000, 600],
                     'magus': [-12000, 600,],
                    }
    for hero, years in years_present.items():
        mask = arr[hero][:]
        for year in years:
            mask = mask | ((year*sec_per_year <= secs) & ((year+1)*sec_per_year >= secs))
        arr[hero] = mask

    f = tb.openFile('epoch_log.h5', 'w')
    f.createTable('/', 'log', arr)
    f.close()
