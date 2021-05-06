from nltk.probability import FreqDist
import matplotlib.pyplot as plt
__stop_words__ = ""

with open(__file__.replace("tools.py","stop_words.txt"), encoding='utf-8') as f:
    __stop_words__ = f.read().splitlines()




def get_frecuency(dataset):
    """provides a list with all the countries that currently have media outlets in Sun

    Returns:
        [string]: [country_name]
    """
    textos=dataset["text"]
    concatenado = ' '.join(textos)
    tokenizado = concatenado.split(" ")
    qty_elements = len(tokenizado)
    tokenized_no_stopwords= [token for token in tokenizado if token not in __stop_words__]
    freq_dictionary = FreqDist(tokenized_no_stopwords)
    return {"total_elements": qty_elements, "dictionary": freq_dictionary}

def get_n_most_freq(freq_struct, n, graph=False):
    """provides a list with all the countries that currently have media outlets in Sun

    Returns:
        [string]: [country_name]
    """
    dict_orders = sorted(freq_struct["dictionary"].items(), key=lambda x: x[1], reverse=True)
    if graph:
        
        x = [x[0] for x in dict_orders[:n]]
        y = [x[1]/freq_struct["total_elements"] for x in dict_orders[:n]]
        plt.bar(x,y)
        plt.title("term frecuency top %i words" %(n))
    return dict_orders[:n]

def add_stop_word(word):
    __stop_words__.append(word)

def graph_term_frecuency_bar(freq_struct, words):
    y = []
    for word in words:
        y.append(freq_struct["dictionary"][word]/freq_struct["total_elements"])
    plt.bar(words,y)
    ("term frecuency bar graph")

#def graph_fusionated_term_frecuency_bar(freq_struct, words):
