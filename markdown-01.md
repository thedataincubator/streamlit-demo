```python
  def insert_markdown_file(filepath):
    '''filepath might be something like markdown-01.md'''
    with open(filepath, 'r') as f:
      contents = f.read()
      
    return contents

  st.markdown(insert_markdown_file("markdown-01.md"))
  ```

  Want to create an expandable section like this one? 
  It's easy! You can define an `st.beta_expander` and reference it like the following:

  ```python
  expandable = st.beta_expander("Some label"):
  with expandable:
    st.write("It's nice to use a context manager like the one above when creating content inside these kinds of streamlit containers.)
  ```