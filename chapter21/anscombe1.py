import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="ticks")

if __name__ == "__main__":
    
    df = sns.load_dataset("anscombe")
    df_grouped = df.groupby('dataset').agg({'x': ['mean', 'std'], 'y': ['mean', 'std']})
    print(df_grouped)
    print("-"*20)

    sns.lmplot(
        data=df, 
        x="x", 
        y="y", 
        col="dataset", 
        hue="dataset",
        col_wrap=2, 
        palette="muted", 
        ci=None,
        height=4, 
        scatter_kws={"s": 50, "alpha": 1}
    )
    plt.show()