# Run the scripts
The scripts retrieve data from Standard and Poor's website, computes a datapackage augmented with yahoo webservices and ***published back the datapackage to github***.

In order to run the scripts, you'll need a valid on github with write access on the repository.

## Fork the repository into your github account...
Because you don't have write access to mine.

## Allow ssh access to your repository
If you don't have a public/private ssh key pair, follow this  [github tutorial](https://help.github.com/articles/generating-ssh-keys/)

Then you must configure your local ssh access to github with a ``~/.ssh/config`` file. Mine looks like :

    Host github.com
        HostName github.com
        User git
        IdentityFile ~/.ssh/lexman_github_rsa

## Checkout the project... With ssh !

    git clone git@github.com:lexman/s-and-p-500-companies.git
    git checkout tuttle	

## Install the dependencies
The scripts work with some python code and are glued together with the **make for data** tool (tuttle)[github.com/lexman/tuttle].
Install all dependencies :

    pip install jinja2
    pip install -r requirements.txt

You can also work on a [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) .

NB : under debian-based distributions you might need to be able to compile and install the messytables dependencies : ``sudo apt-get install libxml2-dev libxslt-dev python-dev lib32z1-dev``

	
## Run the scripts

    cd scripts
	tuttle run
	
Now you have updated the datapackage on your github repository !