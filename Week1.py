import numpy as np

class OrderQuantity(object):
    """
    Q: current quantity being used
    stock: current stock
    Hc: Holding Cost - the cost of holding stock between periods
    Sc: Stockout Cost - the cost of being short inventory between periods
    method: The method used to pick the order quantity
    N: The current period
    reward: The total reward/cost so far
    quantities: tracks the sample mean and the total amount of times a quantity has been used
    """
    def __init__(self, Q, Hc, Sc, update_method):
        self.Q = Q
        self.stock = Q
        self.Hc = Hc
        self.Sc = Sc
        self.method = update_method
        self.N = 0
        self.reward = 0

        if update_method == 'epsilon-greedy':
            sample_mean = 0

        self.quantities = {15: (sample_mean,0),
                           20: (sample_mean,0),
                           25, (sample_mean,0),
                           30, (sample_mean,0),
                           35, (sample_mean,0)}

    def pull(self, Q):
        '''
        Performs a random "pull" and returns the reward
        Returns: The cost incurred through one iteration of the newsvendor game
        '''
        # iteration counter
        self.N +=1

        # Satisfy the random demand and update the sample mean
        random_demand = np.random.normal(loc=20, scale=4)
        self.stock -= random_demand

        self.update(random_demand)

        # Determine the holding cost or stockout cost
        if self.stock < 0:
            self.reward += abs(self.stock) * self.Sc
        elif self.stock > 0:
            self.reward += self.stock * self.Hc
        else:
            self.reward += 0

        # Pick which Q we will use
        lowest_reward = 0
        for key, value in self.quantity.items():
            average = value[0]

        # Replenish the stock
        self.stock = self.stock + self.Q

        return reward


    def update(self, new_demand):
        '''Updates the estimate of the mean reward'''
        if self.update_method == 'epsilon-greedy':
            self.reward = ( 1 - (1/self.N) ) * self.reward + (1/self.N) * new_demand


    def play_newsvendor(self, iterations):
        '''
        Plays the newsvendor game a set number of times
        Returns: the average cost
        '''
        running_reward = 0
        for _ in range(0, iterations):
            current_reward = self.pull()
            running_reward = running_reward + current_reward

        return (running_reward / self.N)


def main():

    newsvendor_instance = OrderQuantity(Q=15,Hc=1,Sc=20,update_method='epsilon-greedy')

    print(newsvendor_instance.play_newsvendor(1000))


if __name__ == "__main__":
    main()
