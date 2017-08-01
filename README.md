triangles triangles triangles
=============================

My son sketched out a grid of points with a pattern of connections and asked the question, how many triangles are in here? Clearly there are a lot and I wanted to use it for an example of a programmatic approach to getting the answer.

I had him redo the sketch on graph paper and label the nodes, and I used networkx in python to represent it.

Here's the sketch
![[triangles sketch]](triangles.jpg "sketch of triangles")

And the answer is.....

Ha ha! That'd be too easy. You'll have to download this and run it yourself.

> python main.py dorset.txt

It's called dorset.txt because we were in Dorset, VT when my son came up with the puzzle. I made an extension of it called fullmesh.txt.

Note, this algorithm is not a general one. It makes assumptions about the structure and may give a misleading answer if you try to feed other random grids to it.
