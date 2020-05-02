import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')

def stdev_rate(bank_id):
    s = ("select stdev(rateoffr) from bank where bid='{}'").format(bank_id)
    return s

def stdev_quantity(c_name):
    s = ("select stdev(quantity) from crop where cname='{}'").format(c_name)
    return s
    
def barGraph(X, Y, xLabel, yLabel,name):
    # X, Y -> list, xLabel,yLabel -> string
    plt.bar(X, Y, align='center', alpha=0.5)
    plt.xticks(X)
    plt.ylabel(xLabel)
    plt.title(yLabel)
    plt.savefig('./app/static/'+name+"_bar.png")
    plt.close()

def pieChart(labels, sizes,name):
    # labels, sizes -> list
    patches, texts = plt.pie(sizes)
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('./app/static/'+name+"_pie.png")
    plt.close()