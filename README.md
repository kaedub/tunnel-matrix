## Pygame Virtual LED matrix

Currently uses Python 2 and Pygame to display a matrix.  

Each file is a slightly different tunnel pattern.

#### To run the tunnel.py program:

`python2 tunnel.py`



#### Press _space bar_ to start or stop movement, _V_ to change direction, and _X_ to add the 'X' to xfold pattern.

This was a program I wrote in my early days of learning programming. It was extremely difficult for me  
to devise an algorithm for the pattern and even today I'm having trouble understanding exactly how I got  
this all to work. My plan is to refactor this over time as the design choices I made and my variable  
naming are pretty cringeworthy.  

I had one major problem that I learned a lot from when making this. 

1) First problem was that time and space complexity was a mysteriousconcept to me at the time of writing  
this. My initial strategy was building a matrix of RGB color tuples then using Pygame to render squares of  
these colors. At each frame I would change each value in the matrix and render again. I tried scaling  
to a 256 x 256 square it did not like that. Went from 30 FPS to about 0.2 FPS. 

_Back to the drawing board..._  

I realized I didn't need to store a matrix in memory at all. I could simply come up with a way to  
calculate the index of the colors list using the row and column index. After that is was just a matter of  
applying something from back in Pre-Calculus class, _graph reflections_!  
