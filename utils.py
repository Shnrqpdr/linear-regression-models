import matplotlib.pyplot as plt
import numpy as np

def histogram(type_hist, data, varname, legendLocation, numberBins, title):
    
    media = float(data.mean())
    desvioPadrao = float(data.std())
    
    mu = media
    sigma = desvioPadrao
    
    # figname = 'hist_%s.png' %place

    fig1 = plt.figure(figsize=(10,8))
    axes = fig1.add_axes([0.1,0.1,0.8,0.8])
    
    n_bins = numberBins
        
    n, bins, patches = axes.hist(data, bins=n_bins, density=True, color='#1f77b4', label=title)
    
    y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))

    axes.plot(bins, y, ls='--', color='#ff7f0e', label='Melhor fit da distribuição')
    
    axes.axvline(media, color='r', label='Média geral dos dados')
    
    axes.set_xlabel(varname)

    axes.set_title(title)

    plt.grid(axis='y', linestyle='-', linewidth=0.5)
    ax = plt.gca() 
    axes.legend(loc=legendLocation)
    plt.show()