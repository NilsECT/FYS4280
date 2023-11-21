import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Vd on 5 um at 2 V
vd_5um_2V = pd.read_csv('data/W3_Vd_2V_5um', delimiter = "\t")

vd_5um_2V.rename(columns={'absmean(A)' : 'Current (A)', 'bias(V)' : 'Bias (V)'}, inplace=True)
vd_5um_2V["Drain voltage"] = ['2 V' for i in range(len(vd_5um_2V))]

figure = sns.relplot(data=vd_5um_2V,
            x="Bias (V)",
            y="Current (A)",
            hue="Drain voltage",
            kind="line", # the kind of plot
            legend="auto")

for ax in figure.axes.flatten():
    ax.ticklabel_format(style='sci', scilimits=(0,0), axis='y')

plt.savefig("vd_2V_5um.pdf")
plt.close()

# Vg

dataframe_list = []

for gate_voltage in range(1, 6, 1):
    for gate_distance in ['2_5', '5', '10', '20']:
        temp = pd.read_csv('data/W3_Vg_' + str(gate_voltage) + 'V_' + gate_distance + 'um', delimiter="\t")

        # remove the unused columns
        # add a column for gate voltage
        temp.drop(columns=['mean(A)', 'range/2(A)', 'relerror'], inplace=True)

        label = [gate_voltage]*len(temp)

        temp["Gate voltage"] = [str(i) + ' V' for i in label]
        temp["Gate distance"] = [gate_distance + ' um' for i in label]

        dataframe_list.append(temp)

df_vg = pd.concat(dataframe_list, ignore_index=True)

df_vg.rename(columns={'absmean(A)' : 'Current (A)', 'bias(V)' : 'Bias (V)'}, inplace=True)

figure = sns.relplot(data=df_vg, # from your Dataframe
                   col="Gate distance", # Make a subplot in columns for each variable in "animal"
                   col_wrap=2, # Maximum number of columns per row 
                   x="Bias (V)",
                   y="Current (A)",
                   hue="Gate voltage",
                   kind="line", # the kind of plot
                   legend="auto"
                   )

for ax in figure.axes.flatten():
    ax.ticklabel_format(style='sci', scilimits=(0,0), axis='y')

plt.savefig("vg_all.pdf")
plt.close()