---
parent: notes 
grand_parent: random notes 
title: - Building a website with Jekyll and Jupyter Notebooks 
nav_order: Website 
---

#### The goal
I have lots of markdown snippets (little bits of code), loosely organised in a folder. In addition I also have some Jupyter notebooks with useful bits of code. I would like to store them in one central place, organised and easily accessible, with a nice overview/web interface, like the people below.


#### How other people do it
Out of the box solutions: build a website from a mix of Jupyter notebooks and markdown files. Something along the lines of these sites:
- Chris Ablon's website: [website](https://chrisalbon.com/), [code](https://github.com/chrisalbon/notes)
- Jake van der Plas' website: [website](), [code]()
- "Just the docs" Jekyll theme: [website](https://github.com/pmarsceill/just-the-docs)


#### How to do it:
Jekyll (and Hugo) generate a website from markdown files.
So all these approaches take a mix of markdown and Jupyter files as inputs, and then generate a website out of it (with some special treatment for the Jupyter notebooks). 
- The first step is to have all the files organised into one folder (potentially with subfolders). 
- The second step is to then build a website from it. This is ususally done using two scripts:
	- the first converts the Jupyter notebooks into markdown and adds the required header (so Jekyll/Hugo knows what to do with them); 
	- the second one is the Jekyll/Hugo script that takes all the files (which are now all markdown) and builds the website from it. (when using Github pages, this step is not required)

#### Step 1: have all the files in order
The script would just take these files as an input then and generate a website from it.

Steps on the way:
- have an ordered overview of 


#### Step 2: run the script to convert the Jupyter files into markdown
The general process is laid out [here](https://cduvallet.github.io/posts/2018/03/ipython-notebooks-jekyll): save your Jupyter notebooks in a folder (with structure), run a script which creates markdown files from them (using [nbconvert](https://nbconvert.readthedocs.io/en/latest/)), and then adds headers for Jekyll in the markdown files, and fixes links and images, and places them where they should be.

Some scripts to automate this process are:
- Chris Albon's [script](https://github.com/chrisalbon/notes/blob/master/make.ipynb). This is specific to Hugo though, so the code might be a little different for Jekyll.
- [here](https://github.com/mobeets/jekyll-ipython-markdown), [here](https://gist.github.com/tgarc/7d6901858ef708030c19), [here](https://jaketae.github.io/blog/jupyter-automation/)


#### Step 3: build the Jekyll page (from all the markdown files)
Using the standard Jekyll procedure


#### On a sidenote...
Jake van der Plas actually uses a different approach (not using Jekyll or anything alike). His [book](https://jakevdp.github.io/PythonDataScienceHandbook/index.html) is built from a collection of Jupyter notebooks (they are ordered, each notebook is a section of a specific chapter), and then runs a script to generate an overview/table of contents page. The code for how he does it is in [his repo](https://github.com/jakevdp/PythonDataScienceHandbook/tree/master/tools).

A different - but much more serious approach - is to use something like [Jupyter Book](https://jupyterbook.org/intro.html) to build an entire book from Jupyter notebooks.

[Jupytext](https://github.com/mwouts/jupytext) transforms Jupyter notebooks into textfiles, which facilitates version control and collaboration. Only tangentially related, but might also be interesting.


#### And another sidenote: Jekyll themes for a personal website
- [Academic Pages](https://academicpages.github.io/) seems to be a decent go-to for using Jekyll. The pages still look a little ugly though... :/
	- It's probably worth looking for a better Jekyll theme


Tangentially related things:





This needs to be done only once, the very first time:
- install Ruby and Jekyll (steps 1-4 [here](https://jekyllrb.com/docs/installation/windows/))

To generate a main (user) page on Github pages, 
- create repository for the site [Github tutorial](https://jekyllrb.com/docs/installation/windows/)


this might be interesting to host the site more 'privately'
