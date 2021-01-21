# Zero to Streamlit (to Heroku)

1. Environment
2. Write/run app.py
3. Deploy to Heroku



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

## Another example app

For a more developed example, take a look at the `example-app` branch of this repository. This branch contains a built-out `app.py`. It's also deployed on [Heroku](https://streamlit-tutorial-app.herokuapp.com/).