#!/usr/bin/python

import sys
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

nArg = len(sys.argv)

if nArg < 3 or nArg > 7:
	print "usage:", sys.argv[0], "[dist_name]", "[shapes]", "[loc]", "[scale]"

loc = float(sys.argv[-2])
dist = getattr(st, sys.argv[1])
scale = float(sys.argv[-1])
nShape = nArg-4

if nShape == 0:

	xMin = dist.ppf(0.01, loc=loc, scale=scale)
	xMax = dist.ppf(0.99, loc=loc, scale=scale)

	x = np.linspace(xMin, xMax, 100)

	ax.plot(x, dist.pdf(x, loc=loc, scale=scale), 'r-', lw=5, alpha=0.6, label='t pdf')

elif nShape == 1:

	xMin = dist.ppf(0.01, float(sys.argv[2]), loc=loc, scale=scale)
	xMax = dist.ppf(0.99, float(sys.argv[2]), loc=loc, scale=scale)

	x = np.linspace(xMin, xMax, 100)

	ax.plot(x, dist.pdf(x, float(sys.argv[2]), loc=loc, scale=scale), 'r-', lw=5, alpha=0.6, label='t pdf')

elif nShape == 2:

	xMin = dist.ppf(0.01, float(sys.argv[2]), float(sys.argv[3]), loc=loc, scale=scale)
	xMax = dist.ppf(0.99, float(sys.argv[2]), float(sys.argv[3]), loc=loc, scale=scale)

	x = np.linspace(xMin, xMax, 100)

	ax.plot(x, dist.pdf(x, float(sys.argv[2]), float(sys.argv[3]), loc=loc, scale=scale), 'r-', lw=5, alpha=0.6, label='t pdf')

else: #3

	xMin = dist.ppf(0.01, float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), loc=loc, scale=scale)
	xMax = dist.ppf(0.99, float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), loc=loc, scale=scale)

	x = np.linspace(xMin, xMax, 100)

	ax.plot(x, dist.pdf(x, float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), loc=loc, scale=scale), 'r-', lw=5, alpha=0.6, label='t pdf')


plt.show()
