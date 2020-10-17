from ipywidgets import interact
import numpy as np
import matplotlib.pyplot as plt
import matplotlib 


def outer(figs):
    '''
    Визуализурует эволюцию распространения вируса и статистику 
    о количестве здоровых, заболевших, иммуных и погибших людях.
    
    Input: figs кортеж, состоящий из трех элементов:
        1) Список (массив) из матриц состояний системы в единичный момент времени
        2) Статистика: массив размера (4, number_of_estimations) 
            Индексы:
            0 - число погибнувших
            1 - число здоровых (неболевших)
            2 - число зараженных
            3 - число, получивших иммунитет
        3) xlim - число (сколько итераций из всех строить)
    Input Example: 
            figs = (boards, stats, xlim)
            outer(figs)
    Return:
        Анимация распространения вируса
    '''
    evolution, stats, xlim = figs
    
    def show(num=(0,xlim - 1)):
    
        
        norm = matplotlib.colors.Normalize(0, 3)
        cmap = plt.cm.jet
        status_labels = ['dead', 'fine', 'sick', 'immunity']
        colors = ['blue', 'deepskyblue', 'gold', 'firebrick']
        markers = ['x', 'o', 's', 'D']
        
    
        fig = plt.figure(figsize=(12, 4))
        ax0 = fig.add_axes([0, 1.0, 0.3, 0.85])
        ax1 = fig.add_axes([0.35, 1.0, 0.65, 0.85])
        ax2 = fig.add_axes([0.0, 0.85, 0.3, 0.05])
        
        
        # Evolution graph
        ax0.set_title(f'Evolution #{num+1} step')
        ax0.set_xticks([])
        ax0.set_yticks([])
        ax0.pcolor(evolution[num][::-1], norm=norm, cmap=cmap, 
                   lw=0.25, edgecolor='black'
                  )
        # Stats graphs
        ax1.set_title('Statictics')
        ax1.grid()
        #ax1.set_xlim(0, 5 * stats.shape[1])
        ax1.set_xlim(0, xlim)
        for n, i in enumerate(stats):
            ax1.plot(i[:num], color=colors[n], marker=markers[n], markersize=10, lw=1.5)
        
#         ax1.set_xticks(np.arange(0, 100 * stats.shape[1] + 1, 500))
        ax1.legend(status_labels, bbox_to_anchor=(1.3, 1))
        cbar = matplotlib.colorbar.ColorbarBase(ax2, 
                                                cmap=cmap, 
                                                norm=norm, 
                                                orientation='horizontal',
                                               )
        cbar.set_ticks([0, 1, 2, 3])
        cbar.set_ticklabels(status_labels)
    return interact(show)
