import numpy as np

class OrderQuantity(object):
    """docstring for OrderQuantity."""
    def __init__(self, Q, Hc, Sc, update_method):
        self.Q = Q
        self.stock = Q
        self.Hc = Hc
        self.Sc = Sc
        self.update_method = update_method
        self.N = 0

        if self.update_method == 'epsilon-greedy':
            self.sample_mean = 0


    def pull(self):
        '''
        Performs a random "pull" and returns the reward
        Returns: The cost incurred through one iteration of the newsvendor game
        '''
        # iteration counter
        self.N = self.N + 1

        # Satisfy the random demand and update the sample mean
        random_demand = np.random.normal(loc=20, scale=4)
        self.stock = self.stock - random_demand

        self.update(random_demand)

        # Determine the holding cost or stockout cost
        if self.stock < 0:
            reward = self.stock * self.Sc
        elif self.stock > 0:
            reward = self.stock * self.Hc
        else:
            reward = 0

        # Replenish the stock
        self.stock = self.stock + self.Q


        return reward

    def update(self, new_demand):
        '''Updates the estimate of the mean reward'''
        if self.update_method == 'epsilon-greedy':
            self.sample_mean = ( 1 - (1/self.N) ) * sample_mean + (1/self.N) * new_demand


def main():

    newsvendor_instance = OrderQuantity(Q=15,Hc=1,Sc=20)

    for i in range(0,20):
        newsvendor_instance.pull()
        print(newsvendor_instance.stock)
        print(i)


if __name__ == "main":
    main()
