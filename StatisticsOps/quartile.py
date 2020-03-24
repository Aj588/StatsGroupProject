from numpy import quantile


class Quartile:
    @staticmethod
    def quartile(data,q,axis,kdims = False):
        return quantile(data,q,axis,kdims)