import numpy as np
from Config.Constants import CORRELATION_COEFFICIENT_BENCHMARK as C


def is_correlation_strong(lat_list_x, lon_list_x, lat_list_y, lon_list_y):
    corr = np.corrcoef([lat_list_x, lon_list_x, lat_list_y, lon_list_y])
    # print np.mean([corr[0, 2], corr[1, 3]])
    if np.mean([corr[0, 2], corr[1, 3]]) >= C:
        return True
    return False

# print is_correlation_strong([19.126104, 19.124847, 19.123772], [72.927831, 72.92782, 72.927895],
#                             [19.126104, 19.124847, 19.123772], [72.927831, 72.92782, 72.927895])
