#!/usr/bin/env python
import numpy as np
import matplotlib.colors as colors
import matplotlib.pyplot as plt

"""
Hasan Genc 2019

The Mandelbrot set is the set obtained from the quadratic recurrence equation
z_(n+1)=z_n^2+C http://mathworld.wolfram.com/MandelbrotSet.html
"""

def mandelbrot(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon = 2.0):
  x = np.linspace(xmin, xmax, xn)
  y = np.linspace(ymin, ymax, yn)
  c = x + y[:, None]*1j

  z = np.zeros(c.shape, np.complex64)
  n = np.zeros(c.shape, dtype = int)

  for r in range(maxiter):
    i = np.less(abs(z), horizon)
    n[i] = r
    z[i] = z[i]**2 + c[i]

  n[n == maxiter - 1] = 0
  return z, n

def plot():
  xmin, xmax, xn = -2.25, 0.75, 1500
  ymin, ymax, yn = -1.25, 1.25, 1250
  maxiter, horizon = 200, 2**40
  log_horizon = np.log(np.log(horizon))/np.log(2)

  z, n = mandelbrot(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon)

  with np.errstate(invalid='ignore'):
    m = np.nan_to_num(n + 1 - np.log(np.log(abs(z)))/np.log(2) + log_horizon)

  dpi = 72
  width = 10
  height = 10*yn/xn
  fig = plt.figure(figsize=(width, height), dpi = dpi)
  ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False, aspect=1)

  # Shaded rendering
  light = colors.LightSource(azdeg=315, altdeg=10)
  m = light.shade(m, cmap=plt.cm.hot, vert_exag=1.5, norm=colors.PowerNorm(0.3), blend_mode='hsv')
  plt.imshow(m, extent=[xmin, xmax, ymin, ymax], interpolation="bicubic")
  ax.set_xticks([])
  ax.set_yticks([])

  text = ("The Mandelbrot fractal set\n")
  ax.text(xmin+.025, ymin+.025, text, color="white", fontsize=12, alpha=0.5)

  plt.show()

if __name__ == "__main__":
  plot()

if __name__ == "fractals.mandelbrot":
  plot()
