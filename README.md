# Zero to Streamlit (to Render.com)

1. Environment
2. Write/test app.py using Streamlit
3. Deploy to Render.com

### An example app

For a very simple example, take a look at the application in the `main` branch here. It's doing nothing more than writing some text to the screen, and inserting text into a sidebar. The `example-app` branch contains a larger example, including showing some addtional functionality like inserting an image into the output.  This branch contains a built-out `app.py`. That more complicated example is also deployed on [Render.com](https://streamlit-demo.onrender.com).

## Environment

At minimum, you will need a `requirements.txt` file in your project's root directory, and it must include `streamlit`. Render.com will use this file to install everything using `pip`. That said, it must also include any other packages your app will use. 

Environment management can be a tricky thing in Python.  You can, for example, use the [Anaconda distribution](https://www.anaconda.com/products/individual). Typically, a conda environment is specified in a file called `environment.yml`, but one can install from `requirements.txt` with the command `conda create --name <my-env-name> --file requirements.txt --channel <NAME_OF_CHANNEL>`. You most likely want to substitute `conda-forge` for `<NAME_OF_CHANNEL>` , and whatever you want for `<my-env-name>` . You can activate the environment with `conda activate <my-env-name>`. 

Alternatively you can use [`pyenv`](https://github.com/pyenv/pyenv) to manage the version of Python you are using, and [Poetry](https://python-poetry.org) as a package management tool, or [`venv`](https://docs.python.org/3/library/venv.html) to create and manage virtual environments. 

## Streamlit

It's a strong convention to build a [Streamlit](https://streamlit.io/) application in a file called `app.py` in the root directory of your project, but you can name it something else if you'd like. You can write the entire contents of the app in this file, but as things get more complicated, it can be helpful to place some code (for example, generating charts) into functions in other scripts, then import these. 

As a general rule, I would recommend setting up your `app.py` like the following. This becomes particularly useful if you start building multi-page apps. 

```
import streamlit as st

def app():
"""All the code for your app (unless you import things from other files)"""

if __name__ == "__main__":
	app()
```
### Running the app locally

Once you have a `app.py` file, you can enter `streamlit run app.py` in the terminal to test/debug. Of course, make sure you're in the appropriate directory for your project. By default, Streamlit runs on port 8501, so you can access it in your web browser with the URL `localhost:8501` (Streamlit will, be default, try to open your browser to that URL.) You can change this port, if you'd like, but that should only be necessary if that port is already in use for some reason.

## Deploy to Render.com

### Overview

Once your app is working locally, you probably want to share it. [Render.com](https://render.com/) is a relatively simple and free way to deploy a web app (this will require you to sign up for an account). 

To deploy anything to Render, we need a text file called `requirements.txt`. This should include any packages that you will need for your application. Render will use `pip` to install all packages listed in this `requirements.txt` file.   

### Deploying
1. Put your code in a git repository, if you haven't already! Render is set up to deploy code from these repositories (github.com, for example).
2. Make a Render account if you haven't already!
3. Log in to the [Render Dashboard](https://dashboard.render.com/) on their website (make sure you have signed in).  
4. Click the box near the top rightthat says **New +**, then select **Web Service**.
5. Name your app.  Render will use this name to create a URL.  
6. You need to tell Render which repository to use for your deployment. This can be your own repository, or any publicly available repository (Render will clone it). You can connect your GitHub or GitLab account if you want, but that's not necessary (as long as the repository is publicly readable).  
7. Make sure you're deploying from the right branch. This is probably going to be your **main** branch or **master** branch, but it might not. The tutorial app is deployed from a branch called `example-app`. 
8. Render will, by default, use Python version 3.7. You can tell it to use another version if you want by defining an environmental variable called `PYTHON_VERSION` and specifying a value there (we are using 3.9.0, which we know this example runs correctly in that version).  
9. **Important:** You need to tell Render what command to use to start your application. This is another option available to set.  Assuming your application is in `app.py` in the main subdirectory of the repository, the command you want is `streamlit run --server.port=$PORT --server.headless=true` as this binds the internal port in Render to your application (so it can communicate with the outside world) and tells the application to **not** load a web browser in the computer it is deployed to (which is no help in this case).   
9. The initial build and deployment process can take 10-15 minutes (Render will give you feedback as it's downloading and installing packages, etc.)  
10.  Once deployed, you can find the URL for your application near the top left of the screen.  
