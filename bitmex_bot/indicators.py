import numpy as np


def ema(values, period=20):
    values = np.asarray(values)
    weights = np.exp(np.linspace(-1., 0., period))

    weights /= weights.sum()

    a = np.convolve(values, weights, mode='full')[:len(values)]
    a[:period] = a[period]
    return a


def macd(l):
    if len(l) > 26:
        ema_26 = ema(l, 26)
        ema_12 = ema(l, 12)

        macd_value = ema_12 - ema_26

        signal_line = ema(macd_value, 9)

        macd_hist = macd_value - signal_line

        return macd_hist

    return


def HEIKIN(O, H, L, C, oldO, oldC):
    HA_Close = (O + H + L + C)/4
    HA_Open = (oldO + oldC)/2
    elements = np.array([H, L, HA_Open, HA_Close])
    HA_High = elements.max(0)
    HA_Low = elements.min(0)
    out = np.array([HA_Close, HA_Open, HA_High, HA_Low])
    return out
