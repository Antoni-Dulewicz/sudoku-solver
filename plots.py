import matplotlib.pyplot as plt
import os

def clear_output_folder(output_folder):
    if os.path.exists(output_folder):
        for file_name in os.listdir(output_folder):
            os.remove(os.path.join(output_folder,file_name))
    else:
        os.mkdir(output_folder)

def plot_energies(energies,output_folder):
    plt.plot(energies,color = 'goldenrod')
    plt.title('Energy characteristics function')
    plt.xlabel('iteration')
    plt.ylabel('energy')
    plt.savefig(os.path.join(output_folder,'energy_plot.png'))
    plt.close()

def plot_temparatures(temparatures,output_folder):
    plt.plot(temparatures,color ='orangered')
    plt.title('Temp. function')
    plt.xlabel('iteration')
    plt.ylabel('temparature')
    plt.savefig(os.path.join(output_folder,'temp_plot.png'))
    plt.close