import seaborn as sns

def distploter(x):
    return sns.distplot(x, kde=False, rug=True)

def scatter(x,y,z):
    return sns.scatterplot(x, y, z)

def sumGroupby(x,y):
    return x.groupby(y).sum()

def meanGroupby(x,y):
    return x.groupby(y).mean()

def plotbar(x):
    return x.plot.bar()

def plotline(x):
    return x.plot.line()