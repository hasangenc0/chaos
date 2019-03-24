c = python
fractals = src/fractals
init = __init__.py

mandelbrot:
	@$(c) $(fractals)/$(init) mandelbrot

.PHONY: mandelbrot