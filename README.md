# Zero to Streamlit (to Heroku)

1. Environment
2. Write/run app.py
3. Deploy to Heroku

### An example app

For a more developed example (and a Streamlit tutorial), take a look at the `example-app` branch of this repository. This branch contains a built-out `app.py`. It's also deployed on [Heroku](https://streamlit-tutorial-app.herokuapp.com/).

## Environment

At minimum, you will need a `requirements.txt` file in your project's root directory, and it must include `streamlit`. Heroku will use this file to install everything using `pip`. That said, it must also include any other packages your app will use. 



I recommend using this file to build a virtual environment for local development, as well. There are a few libraries for this, but I tend to prefer `conda`. If you don't have conda or a Python distribution, you can install both with the [Anaconda distribution](https://www.anaconda.com/products/individual). Typically, a conda environment is specified in a file called `environment.yml`, but one can install from `requirements.txt` with the command `conda create --name <my-env-name> --file requirements.txt --channel <NAME_OF_CHANNEL>`. You most likely want to substitute `conda-forge` for `<NAME_OF_CHANNEL>` , and whatever you want for `<my-env-name>` . You can activate the environment with `conda activate <my-env-name>`. 



## Write/run app.py

It's a strong convention to build a Streamlit app in a file called `app.py` in the root directory of your project, but you can name it something else if you'd like. You can write the entire contents of the app in this file, but as things get more complicated, it can be helpful to place some code (for example, generating charts) into functions in other scripts, then import these. As we'll see later, this approach can be used to generate multi-page apps, as well.

As a general rule, I would recommend setting up your `app.py` like the following. This becomes particularly useful if you start building multi-page apps. 

```
import streamlit as st

def app():
"""All the code for your app (unless you import things from other files)"""

if __name__ == "__main__":
	app()
```



### Running the app locally

Once you have a working `app.py`, you can enter `streamlit run app.py` in the terminal. Of course, make sure you're in the appropriate directory for your project. By default, Streamlit runs on port 8501, so you can access it in your web browser with the URL `localhost:8501`. You can change this port, if you'd like, but I don't think that's immediately necessary to cover.



## Deploy to Heroku

### Overview

So your app is working locally. That's great, but you probably want to share it. [Heroku](heroku.com) is a simple and free way to deploy a simple web app. Let's take a look.

To deploy anything to Heroku, we need a text file called `Procfile`. I'm not going to get into it in too much detail, but this tells Heroku what services are necessary for the app to run, and potentially what commands to use to get started.

To deploy a Streamlit app, we need a setup script, which we have here: `setup.sh`. This creates some configuration files necessary for Streamlit. Again, I won't get into too many details. Instead, just copy those files (or fork this repository) to start creating your own app.

### Deploying
1. Put your code in a git repository, if you haven't already! There are multiple ways to deploy from Heroku, but using automatic deploys based on GitHub repo is a simple way to ensure that your app matches your code.
2. Make a Heroku account if you haven't already!
3. Log in to the [Heroku Dashboard](https://dashboard.heroku.com/apps)
4. In the top right corner, click the box that says **New**, then select **Create new app**.
5. Name your app. It has to be a completely unique name due to the way Heroku creates URLs. If you leave the name field blank, Heroku will create a random name for you. Go to the next page.
6. The second section, **Deployment Method**, has an option for connecting to GitHub. If you haven't done this before, it should prompt you to log in.
7. Search for the name of your repo. This one, for example, is `heroku-demo`. Once it shows up, click **Connect**.
8. Make sure you're deploying from the right branch. This is probably going to be your **main** branch, but it might not. My tutorial app is deployed from a branch called `example-app`. In a real production setting, it's common to have two (or more) versions of a website deployed from different branches. For instance, you might have the production site deployed from `main`, and a dev site deployed from `dev`. I would recommend enabling automatic deploys. This re-builds the app any time you push to the branch.
9. You should be all set!
