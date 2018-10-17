import numpy as np

class OrderQuantity(object):
    """docstring for OrderQuantity."""
    def __init__(self, Q, Hc, Sc):
        self.Q = Q
        self.Hc = Hc
        self.Sc = Sc

    def pull(self):
        '''
        Performs a random "pull" and returns the reward
        Returns: The cost incurred through one iteration of the newsvendor game
        '''
        self.Q = self.Q - np.random.normal(loc=20, scale=4)

        pass

    def update(self):
        '''Updates the estimate of the mean reward'''
        pass


def main():

    newsvendor_instance = OrderQuantity(Q=15,Hc=1,Sc=20)

    pass


if __name__ == "main":
    main()
