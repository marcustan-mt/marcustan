# Use Case: Illustrating Matplotlib through a Simple Gambling Simulator
# Objective of this code: Building a Simple Gambling Simulator to simulate 1000 successive bets on the outcomes (i.e., spins) of the American roulette wheel.
# Each series of 1000 successive bets are called an “episode.” You should test for the results of the betting events by making successive calls to the get_spin_result(win_prob) function. 
# The strategy that we follow can be summarized as :
#   1. Doubling the amount if we don't win
#   2. Setting a cap on the maximum amount that we can win


def get_spin_result(win_prob):  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    :param win_prob: The probability of winning  		  	   		  		 		  		  		    	 		 		   		 		  
    :type win_prob: float  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: The result of the spin.  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: bool  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    result = False  		  	   		  		 		  		  		    	 		 		   		 		  
    if np.random.random() <= win_prob:  		  	   		  		 		  		  		    	 		 		   		 		  
        result = True  		  	   		  		 		  		  		    	 		 		   		 		  
    return result  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def test_code():
    """
    Method to test your code
    """
    win_prob = 0.474  # set appropriately to the probability of a win
    np.random.seed(gtid())  # do this only once
    print(get_spin_result(win_prob))  # test the roulette spin
    # add your code here to implement the experiments

    # Added an additional library to ensure graphs can be plotted smoothly
    import matplotlib.pyplot as plt

    # # [Experiment 1] Initializing plots per assignment requirement
    plt.title('Episode Winnings; 10 Episodes')
    plt.xlabel("No. of Bets")
    plt.ylabel("Winnings")
    plt.xlim(0, 300)
    plt.locator_params(axis='x')
    plt.ylim(-256, 100)
    plt.locator_params(axis='y')

    # Experiment 1; Figure 1 results
    for i in range(0,10):
        # print(i)

        # Initializing lists for plotting purposes
        list_x = np.zeros((1000),dtype = np.int_)
        list_y = np.zeros((1000),dtype = np.int_)
        episode_winnings = 0
        counter = 0

        # Pseudo code per provided
        while episode_winnings < 80:
            won = False
            bet_amount = 1
            while won == False:
                won = get_spin_result(win_prob)
                if won == True:
                    episode_winnings = episode_winnings + bet_amount
                else:
                    episode_winnings = episode_winnings - bet_amount
                    bet_amount = bet_amount * 2
                list_x[counter] = counter
                if episode_winnings >= 80:
                    list_y[counter] = 80
                else:
                    list_y[counter] = episode_winnings
                counter = counter + 1
                # Breaking any further running of the episode if 1000 bets has been placed, or if episode winning has reached $80
                if counter == 1000 or episode_winnings > 80:
                    break

            # Breaking any further while loop if 1000 bets has been placed.
            if counter == 1000:
                break

        # Appending $80 as episode winning if 1000 loops has not been completed, but episode winning has reached $80.
        if counter != 1000:
            for x in range(counter,1000):
                list_x[x] = x
                list_y[x] = 80
        # Plotting for Figure 1
        plt.plot(list_x,list_y, label=f'Episode {i+1}')
        plt.legend(loc="upper left")
        plt.savefig('images/figure-1.png',bbox_inches='tight')

    # # Experiment 1; Figure 2 results
    dict_mean_sd = {}
    for i in range(0, 1000):
        dict_mean_sd[i] = np.zeros((1000),dtype = np.int_)
    list_mean = np.zeros((1000),dtype = np.float32)
    list_sd_add_mean = np.zeros((1000),dtype = np.float32)
    list_sd_minus_mean = np.zeros((1000),dtype = np.float32)
    for i in range(0, 1000):
        # print('episode number: ', i)

        # Initializing variables for plotting purposes
        list_x = np.zeros((1000),dtype = np.int_)
        list_y = np.zeros((1000),dtype = np.int_)

        episode_winnings = 0
        counter = 0

        # Pseudo code per provided
        while episode_winnings < 80:
            won = False
            bet_amount = 1

            while won == False:
                won = get_spin_result(win_prob)
                if won == True:
                    episode_winnings = episode_winnings + bet_amount
                else:
                    episode_winnings = episode_winnings - bet_amount
                    bet_amount = bet_amount * 2
                list_x[counter] = counter
                if episode_winnings >= 80:
                    list_y[counter] = 80
                    dict_mean_sd[counter][i] = 80
                else:
                    list_y[counter] = episode_winnings
                    dict_mean_sd[counter][i] = episode_winnings
                counter = counter + 1

                # Breaking any further running of the episode if 1000 bets has been placed, or if episode winning has reached $80
                if counter == 1000 or episode_winnings > 80:
                    break

            # Breaking any further while loop if 1000 bets has been placed.
            if counter == 1000:
                break

        # Appending $80 as episode winning if 1000 loops has not been completed, but episode winning has reached $80.
        if counter != 1000:
            for x in range(counter, 1000):
                list_x[x] = x
                list_y[x] = 80
                dict_mean_sd[x][i] = 80

    # Calculating Mean for each try
    for i in dict_mean_sd.keys():
        sd = np.std(dict_mean_sd[i])
        avg = np.mean(dict_mean_sd[i])

        list_mean[i] = avg
        list_sd_add_mean[i] = avg + sd
        list_sd_minus_mean[i] = avg - sd

    plt.clf()
    plt.title('Mean Episode Winnings; 1000 Episodes')
    plt.xlabel("No. of Bets")
    plt.ylabel("Mean Winnings")
    plt.xlim(0, 300)
    plt.locator_params(axis='x')
    plt.ylim(-256, 100)
    plt.locator_params(axis='y')
    plt.plot(list_x, list_mean, label='Mean')
    plt.plot(list_x, list_sd_add_mean, label='Mean + SD')
    plt.plot(list_x, list_sd_minus_mean, label='Mean - SD')
    plt.legend(loc="upper left")
    plt.savefig('images/figure-2.png',
                bbox_inches='tight')

    # Experiment 1; Figure 3 results
    # Calculating median for each try
    list_med = np.zeros((1000),dtype = np.float32)
    list_sd_add_med = np.zeros((1000),dtype = np.float32)
    list_sd_minus_med = np.zeros((1000),dtype = np.float32)

    for i in dict_mean_sd.keys():
        sd = np.std(dict_mean_sd[i])
        med = np.median(dict_mean_sd[i])

        list_med[i] = med
        list_sd_add_med[i] = med + sd
        list_sd_minus_med[i] = med - sd

    plt.clf()
    plt.title('Median Episode Winnings; 1000 Episodes')
    plt.xlabel("No. of Bets")
    plt.ylabel("Median Winnings")
    plt.xlim(0, 300)
    plt.locator_params(axis='x')
    plt.ylim(-256, 100)
    plt.locator_params(axis='y')
    plt.plot(list_x, list_med, label='Median')
    plt.plot(list_x, list_sd_add_med, label='Median + SD')
    plt.plot(list_x, list_sd_minus_med, label='Median - SD')
    plt.legend(loc="upper left")
    plt.savefig('images/figure-3.png',
                bbox_inches='tight')

    # Experiment 2; Figure 4 results
    dict_mean_sd = {}
    for i in range(0, 1000):
        dict_mean_sd[i] = np.zeros((1000),dtype = np.int_)
    list_mean = np.zeros((1000),dtype = np.float32)
    list_sd_add_mean = np.zeros((1000),dtype = np.float32)
    list_sd_minus_mean = np.zeros((1000),dtype = np.float32)
    for i in range(0, 1000):
        # print('episode number: ', i)

        # Initializing variables for plotting purposes
        list_x = np.zeros((1000), dtype=np.int_)
        list_y = np.zeros((1000), dtype=np.int_)

        episode_winnings = 0
        counter = 0

        # Pseudo code per provided
        while episode_winnings < 80 and episode_winnings > -256:
            won = False
            bet_amount = 1

            while won == False:
                won = get_spin_result(win_prob)
                if won == True:
                    episode_winnings = episode_winnings + bet_amount
                else:
                    episode_winnings = episode_winnings - bet_amount
                    bet_amount = bet_amount * 2
                    if bet_amount > (episode_winnings + 256):
                        bet_amount = min(episode_winnings + 256, bet_amount)
                list_x[counter] = counter
                if episode_winnings >= 80:
                    list_y[counter] = 80
                    dict_mean_sd[counter][i] = 80
                elif episode_winnings <= -256:
                    list_y[counter] = -256
                    dict_mean_sd[counter][i] = -256
                else:
                    list_y[counter] = episode_winnings
                    dict_mean_sd[counter][i] = episode_winnings
                counter = counter + 1

                # Breaking any further running of the episode if 1000 bets has been placed, or if episode winning has reached $80
                if counter == 1000 or episode_winnings > 80 or episode_winnings <= -256:
                    break

            # Breaking any further while loop if 1000 bets has been placed.
            if counter == 1000:
                break

        # Appending $80 as episode winning if 1000 loops has not been completed, but episode winning has reached $80.
        if counter != 1000:
            for x in range(counter, 1000):
                if episode_winnings >= 80:
                    list_x[x] = x
                    list_y[x] = 80
                    dict_mean_sd[x][i] = 80
                else:
                    list_x[x] = x
                    list_y[x] = -256
                    dict_mean_sd[x][i] = -256

    # Calculating Mean for each try
    for i in dict_mean_sd.keys():
        sd = np.std(dict_mean_sd[i])
        avg = np.mean(dict_mean_sd[i])

        list_mean[i] = avg
        list_sd_add_mean[i] = avg + sd
        list_sd_minus_mean[i] = avg - sd

    plt.clf()
    plt.title('Mean Episode Winnings; 1000 episodes of more realistic method')
    plt.xlabel("No. of Bets")
    plt.ylabel("Mean Winnings")
    plt.xlim(0, 300)
    plt.locator_params(axis='x')
    plt.ylim(-256, 100)
    plt.locator_params(axis='y')
    plt.plot(list_x, list_mean, label='Mean')
    plt.plot(list_x, list_sd_add_mean, label='Mean + SD')
    plt.plot(list_x, list_sd_minus_mean, label='Mean - SD')
    plt.legend(loc="upper left")
    plt.savefig('images/figure-4.png',
                bbox_inches='tight')

    # Experiment 2; Figure 5 results
    # Calculating median for each try
    list_med = np.zeros((1000), dtype=np.float32)
    list_sd_add_med = np.zeros((1000), dtype=np.float32)
    list_sd_minus_med = np.zeros((1000), dtype=np.float32)

    for i in dict_mean_sd.keys():
        sd = np.std(dict_mean_sd[i])
        med = np.median(dict_mean_sd[i])

        list_med[i] = med
        list_sd_add_med[i] = med + sd
        list_sd_minus_med[i] = med - sd

    plt.clf()
    plt.title('Median Episode Winnings; 1000 episodes of more realistic method')
    plt.xlabel("No. of Bets")
    plt.ylabel("Median Winnings")
    plt.xlim(0, 300)
    plt.locator_params(axis='x')
    plt.ylim(-256, 100)
    plt.locator_params(axis='y')
    plt.plot(list_x, list_med, label='Median')
    plt.plot(list_x, list_sd_add_med, label='Median + SD')
    plt.plot(list_x, list_sd_minus_med, label='Median - SD')
    plt.legend(loc="upper left")
    plt.savefig('images/figure-5.png',
                bbox_inches='tight')


if __name__ == "__main__":  		  	   		  		 		  		  		    	 		 		   		 		  
    test_code()  		  	   		  		 		  		  		    	 		 		   		 		  
