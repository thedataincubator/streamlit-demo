"""Small example streamlit application."""
import streamlit as st
import pandas as pd
import altair as alt

def insert_markdown_file(filepath):
  '''filepath might be something like markdown-01.md'''
  with open(filepath, 'r') as f:
    contents = f.read()
  return contents



def app():

  st.title("A very meta Streamlit demo")
  
  st.sidebar.header("Some things we'll cover:")
  st.sidebar.markdown("""
* Markdown
* Pandas
* Altair""")
  
  st.markdown("""This is a Streamlit app that introduces how to use Streamlit. Hence the title. Let's get right into it.
* If you want to display something in the app, use things like:
  * `st.title("A very meta Streamlit demo")`
  * `st.sidebar.header("Some things we'll cover:")`
  * `st.write(some_object)`. Lots of objects work with this function!
  * `st.altair_chart(), st.plotly_chart(), st.bokeh_chart()`. 
    * Usually, you can use `st.write()` for this sort of thing, but sometimes you need these specific functions.
    * This happens when a multi-page app, but I'm getting ahead of myself!

Want to render a code block like below? Use `st.code("x = 1 + 1"`.)""")
  st.code("x = 1 + 1")

  st.markdown("Or, as I typically prefer, just use Markdown.")

  st.markdown('''## Markdown
That's right, you can write Markdown in Streamlit by calling `st.markdown(text)`. I like to do this and write chunks of text with multi-line strings. 
Some things to note:
* As usual, you need two newlines separating paragraphs.
  * This means you can use a single newline to wrap your text without breaking the paragraph.
  That's kind of nice if your IDE doesn't have a line wrapping option. 
* We can put Markdown in the sidebar, too.
  * Try something like `st.sidebar.markdown("""* Ah, yes... bullet points""")`
* By default, `st.markdown` won't render html. 
  * You can change this by adding the argument `unsafe_allow_html=True`.
* If you have lots of text, it might get unwieldy to write it all in one file. You might consider writing Markdown in separate files and importing it. Maybe that would look something like this:''')
  
  ex_1 = st.beta_expander("Click to see code!")
  with ex_1:
    st.markdown(insert_markdown_file('markdown-01.md'))
 
  # Pandas example
  st.markdown("""## Pandas
Streamlit is made to render lots of Python objects such as Pandas DataFrames. Let's create a simple DataFrame and render it.
  """)
  df = pd.DataFrame({'x':[1,2,3], 'y':[40, 20, 30], 'z':[100, 40, 33]})
  st.write(df)
  st.markdown("""Remember that Streamlit will run any Python code you give it, so you can of course manipulate your DataFrame. Also, you can use Streamlit widgets for simple control flow and interactivity! Let's put some of these in the sidebar. We'll use the following code:
  
  ```python
  func = st.sidebar.selectbox("Aggregate:", ['Sum', 'Mean', 'Median'])
  
  # We can reference func and use the currently selected value in the box.
  if func == 'Sum':
    st.write(df.sum())
  elif func == 'Mean':
    st.write(df.mean())
  elif func == 'Median':
    st.write(df.median)
  ```
  
  """)
  st.sidebar.subheader("Select an aggregator for the DataFrame")
  func = st.sidebar.selectbox("Aggregate:", ['Sum', 'Mean', 'Median'])
  
  if func == 'Sum':
    out = df.sum()
  elif func == 'Mean':
    out = df.mean()
  elif func == 'Median':
    out = df.median()
    
  col_df, col_out, col_text = st.beta_columns((3, 2, 3))
  with col_df:
    st.write("**Original**")
    st.write(df)
  with col_out:
    st.write("**Aggregated**")
    st.write(out)
  with col_text:
    st.markdown("""
  **Description:**
  * By the way, I'm using columns here. 
  * See below for details.""")
    
  st.markdown("""**Note:** When you change the value of a widget, like our `selectbox`, the *entire* app will re-run. If your app makes any slow computations, this can result in inefficient performance. One major speedup: put the decorator `@st.cache` above all function definitions. This will cache the results of function calls and reload them instead of running the function again. This is particularly useful if you load a large data file or make an API call. For example, you may use something like:
  
  ```python
@st.cache
def load_df_from_url(url):
  df = pd.read_csv(url)
  return df
  ```
  """)
  
  # Altair in Streamlit
  st.markdown("""## Altair
As you might expect, it's easy to use Streamlit with plotting libraries. Let's run a quick example using Altair. 

Let's also create some `selectbox` selectors to modify our chart encoding. Just for fun, let's make some columns here. 

Streamlit lets use create content in columns using `st.beta_columns`, which takes a tuple of relative column widths as arguments. In other words,
we can write something like this to create 2 columns, with the right-hand column twice as wide as the left.

```python

left_col, right_col = st.beta_columns((1, 2))

with left_col:
  st.write("stuff goes here")
with right_col:
  st.write("stuff also goes here")

```
We then place content in these columns using a *context manager* like the one we saw for the expander.
  """)

  left_col, right_col = st.beta_columns((2, 1))

  with right_col:
    xaxis = st.selectbox("X axis encoding:", ['x', 'y'])
    yaxis = st.selectbox("Y axis encoding:", ['y', 'x'])
    mark = st.selectbox("Mark", ["Line", "Bar"])

    st.markdown("""
* Nothing to see here, folks, just some text to fill space
* Oh no, everything is overlapping...
      """)


  with left_col:
    if mark == "Line":
      chart = alt.Chart(df, title="A chart. Nice.").mark_line().encode(x=xaxis, y=yaxis)
      chart_wide = alt.Chart(df, width=1000, height=210).mark_line().encode(x=xaxis, y=yaxis)
      chart_right = alt.Chart(df, width=200, height=190).mark_line().encode(x=xaxis, y=yaxis)
    if mark == "Bar":
      chart = alt.Chart(df, title="A chart. Nice.").mark_bar().encode(x=xaxis, y=yaxis)
      chart_wide = alt.Chart(df, width=1000, height=210).mark_bar().encode(x=xaxis, y=yaxis)
      chart_right = alt.Chart(df, width=200, height=190).mark_bar().encode(x=xaxis, y=yaxis)
    st.write(chart)
    st.markdown("""By the way, the default Streamlit app width is 698px. 
      That's good to keep in mind when creating plots, especially when displaying them in the left column.""")

  with right_col:
    st.write(chart_right)

  with left_col:
    st.write(chart_wide)

  st.markdown('''## One last note
If you look at the code, I defined the selector values in the left column,
 but I defined the charts in the right column. I didn't have to do it this way, but it's a good example.
 To make this work, I had to reference the left column twice. The whole block looks like this:

 ```python

with right_col:
    st.write("Here's our right column")
    xaxis = st.selectbox("X axis encoding:", ['x', 'y'])
    yaxis = st.selectbox("Y axis encoding:", ['y', 'x'])
    mark = st.selectbox("Mark", ["Line", "Bar"])

    st.markdown("""
* Nothing to see here, folks, just some text to fill space
* Oh no, it's overlapping with the chart....
      """)


 with left_col:
    if mark == "Line":
      chart = alt.Chart(df, title="A chart. Nice.").mark_line().encode(x=xaxis, y=yaxis)
      chart_wide = alt.Chart(df, width=1000, height=210).mark_line().encode(x=xaxis, y=yaxis)
      chart_right = alt.Chart(df, width=200, height=190).mark_line().encode(x=xaxis, y=yaxis)
    if mark == "Bar":
      chart = alt.Chart(df, title="A chart. Nice.").mark_bar().encode(x=xaxis, y=yaxis)
      chart_wide = alt.Chart(df, width=1000, height=210).mark_bar().encode(x=xaxis, y=yaxis)
      chart_right = alt.Chart(df, width=200, height=190).mark_bar().encode(x=xaxis, y=yaxis)
    st.write(chart)
    st.markdown("""By the way, the default Streamlit app width is 698px. 
      That's good to keep in mind when creating plots, especially when displaying them in the left column.""")

  with right_col:
    st.write(chart_right)

  with left_col:
    st.write(chart_wide)

 ```
    ''')

  
if __name__ == '__main__':
    app()

