import pandas as pd
import matplotlib.pyplot as plt


def prepare(dataset):
    
    """Prepares the dataset columns for analysis.
    
    Parameters
    ----------
    dataset : Dataframe
        Dataframe for analysis.
        
    Returns
    -------
    dataset : Dataframe
        Dataset with more apropriate column structure.
    """ 
    # split the column 'ships_from_to' into 2 columns
    dataset[['ships_from','ships_to']] = dataset.ships_from_to.str.split('to',expand=True) 

    #splits the column 'ships_to' into 2 columns
    dataset[['ships_to_1','ships_to_2']] = dataset.ships_to.str.split(',',expand=True) 


    return dataset




def ships_most(dataset):
    
    """Returns the info where vendors ship product from
    and amount of succesful transactions.
    
    Parameters
    ----------
    dataset : Dataframe
        Dataframe for analysis.
        
    Returns
    -------
    sort : Dataframe
        The 2 columns of the dataframe with sorted values."""
    
    #groups 2 columns from a dataset
    count = dataset.groupby('ships_from').count()[['successful_transactions']]

    #sorts valuesin descending order
    sort = count.sort_values(by=['successful_transactions'], ascending = False)
    
    return sort






def price(dataset):
    
    """Calculates the price based on the user's input.
    
    Parameters
    ----------
    dataset : Dataframe
        Dataframe for analysis.
        
    Returns
    -------
    result : string
        The string containing the price per amount of grams.
    """ 
    #calculates the average cost per gram
    #BTC price $2480.44 as of July 18
    mean_btc = dataset['cost_per_gram'].mean()
    gram = mean_btc * 2480.44
    
    #creates input function for the user
    inp = int(input("what's the price for the cocaine? type  the number of grams here:  "))
    cost = inp * gram
    cost = round(cost, 2)
    
    #adjusts the inflexion according to the input
    if inp != 1:
        result = '$' + str(cost) + ' per ' + str(inp) + ' grams'
    else:
        result = '$' + str(cost) + ' per ' + str(inp) + ' gram'
    
    return result
    
    
    
    


def plot(dataset):
    
    """Plots quality-rating correlation.
    
    Parameters
    ----------
    dataset : Dataframe
        Dataframe for analysis.
        
    Returns
    -------
    graph : plot
        The plot with the correlation.
    """ 
    
    graph = dataset.plot.hist(x="quality",y="rating",alpha=1)
    plt.ylabel('quality')
    plt.xlabel('rating')
    plt.ylim(0, 100)
    
    
    return graph



def receives_most(dataset):
    
    """Returns the info where vendors ship product to 
    and amount of succesful transactions .
    
    Parameters
    ----------
    dataset : Dataframe
        Dataframe for analysis.
        
    Returns
    -------
    result : sort
        The 2 sorted columns of the dataframe.
    """ 
     
    #merging 2 columns    
    dataset['ships_to_final'] = dataset.pop('ships_to_1').fillna(dataset.pop('ships_to_2')).astype(str)
    
    #groups 2 colums from a dataset
    count = dataset.groupby('ships_to_final').count()[['successful_transactions']]
    
    #sorts values in descending order
    sort = count.sort_values(by=['successful_transactions'], ascending = False)
    
    return sort