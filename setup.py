
from setuptools import setup, find_packages

# Read the requirements.txt file and store the dependencies in a list
with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()


setup(
    #this will be the package name you will see, e.g. the output of 'conda list' in anaconda prompt
    name = 'noisedive_flask', 
    #some version number you may wish to add - increment this after every update
    version='1.1.27', 
    include_package_data=True,
    # package_data=? (MANIFEST.in)
    install_requires=requirements,

    #this approach automatically finds out all directories (packages) - those must contain a file named __init__.py (can be empty)
    packages=find_packages(), #include/exclude arguments take * as wildcard, . for any sub-package names
)

# TODO: 
# TODO: 
# TODO: 
# TODO: 
# TODO: NEXT UP:
# 0) make deployment.yaml auto build and install most recent package version. DONE
# 1) either abandon the base repo or finish porting all the query code to be non-awful and use one DB, and close conns!
# 2) make it so the databases aren't cleared each time (no github)
# 3) document just-once and every-time steps in README or google doc
# TODO: 
# TODO: 
# TODO: 
# TODO: 
# TODO: 
# TODO: 

#### LOCALLY, RUN:
# ~/noisedive_flask % FLASK_APP=noisedive_flask flask run

# In production:
# ### EACH TIME:
# source venv/bin/activate
# python setup.py bdist_wheel
# pip install dist/noisedive_flask-1.1.8-py3-none-any.whl
# venv/bin/waitress-serve --call 'noisedive_flask:create_app'

#### NOTES: works great locally. Seems to run remotely, but I can't find it online. Might need to use nginx or something, or it's something else.


# I think all you do is:
# ### ON REMOTE MACHINE:
# python3.10 -m venv venv
# source venv/bin/activate
# pip install --upgrade pip
# pip install -r requirements.txt

# python setup.py bdist_wheel

# ### NOTE: updates seem to not go through unless version is increased??
# ### potentially on new machine or different directory, using the version (here 1.1 listed in setup.py)
# pip install dist/noisedive_flask-1.1.9-py3-none-any.whl --force-reinstall

# ## WSGI server:
# pip install waitress
# venv/bin/waitress-serve --call 'noisedive_flask:create_app'


######
# added sh file:
# # touch /home/protected/run-noisedive.sh
# #!/bin/sh
# # then:
# chmod a+x run-noisedive.sh
# # you can test with:
# cd noisedive
# ../run-noisedive.sh

# changed proxy port to flask default 5000
# changed server type to fancy daemon friendly one and plan to production site
# made sure protected virtualenv includes all the packages and the new wheel (TODO create automatically)
# wrote daemon to run /home/protected/noisedive/venv/bin/waitress-serve --call 'noisedive_flask:create_app'
# kicked it off in nearlyfreespeech
# logs of daemon are in: /home/logs/daemon_noisedive.log
# changed setup.py to have include_package_data=True so non-py files are included in package.
# and then added a MANIFEST.in file to specify what to include.
# also changed permissions on database files, they weren't working: chmod 664 db/*.db
# exec venv/bin/waitress-serve --call 'noisedive_flask:create_app'