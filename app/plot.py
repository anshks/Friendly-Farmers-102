import matplotlib.pyplot as plt
import numpy as np

def barGraph(X, Y, xLabel, yLabel):
	# X, Y -> list, xLabel,yLabel -> string
	plt.bar(X, Y, align='center', alpha=0.5)
	plt.xticks(X)
	plt.ylabel(xLabel)
	plt.title(yLabel)
	plt.savefig("testBar.png")

def pieChart(labels, sizes):
	# labels, sizes -> list
	patches, texts = plt.pie(sizes)
	plt.legend(patches, labels, loc="best")
	plt.axis('equal')
	plt.tight_layout()
	plt.savefig("testPie.png")