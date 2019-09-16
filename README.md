# Frank's notes

I often find myself in one of the following situations:
* I need to solve a problem,
* I discover a new technology that looks interesting,
* I experiment with an application or a library that I do not know yet,
* I solve a maths or programming problem just for fun.

The things I learn when I read documentation, blog posts, or books in these
situations, and the findings of my experiments can be divided into three
categories:
* Some things are needed so frequently that I can memorize them very quickly.
* Other things turn out not to be so interesting after all and are needed only
  once, so I forget them.
* Then there are things which are useful once in a while, but which I cannot
  remember well, such that they need to be searched again and again.

This repository is an attempt to help me remember interesting and helpful stuff
that I find. I write down examples and explanations which help me most when I
re-read them, and I hope that the process of creating them also helps me to
 memorize what I want to keep in my mind.
 
I make these notes public to make it easy for me to find them whenever I need
them. And who knows - maybe some of this stuff will even turn out to be useful
for others :-) 

Most examples are organized as Jupyter notebooks.


# Python virtualenv setup

    virtualenv venv -p python3
    . venv/bin/activate
    pip install -r requirements.txt

    # Initialize bash kernel for Jupyter (see https://github.com/takluyver/bash_kernel)
    python -m bash_kernel.install

# Run Jupyter notebook server

    jupyter notebook
