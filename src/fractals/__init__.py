import sys
import mandelbrot as mb

params = sys.argv

if len(params) > 1 and params[1] == "mandelbrot":
  # visualize mandelbrot set
  mb.plot()