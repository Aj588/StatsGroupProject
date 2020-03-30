from scipy.stats import stats


class Skew:
    @staticmethod
    def skew(data, axis=0, bias=True):
        return stats.skew(data, axis, bias)