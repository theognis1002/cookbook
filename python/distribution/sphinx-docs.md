Assuming you have Python already, install Sphinx:

`pip install sphinx`

Create a directory inside your project to hold your docs:

`cd /path/to/project`
`mkdir docs`

Run sphinx-quickstart in there:

`cd docs`
`sphinx-quickstart`

This quick start will walk you through creating the basic configuration; in most cases, you can just accept the defaults. When it’s done, you’ll have an index.rst, a conf.py and some other files. Add these to revision control.

Now, edit your index.rst and add some information about your project. Include as much detail as you like (refer to the reStructuredText syntax or this template if you need help). Build them to see how they look:

`make html`
