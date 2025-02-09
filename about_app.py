import streamlit as st

## page setting
st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed",
)
### insert external css
@st.cache_data
def insert_css(css_file:str):
    with open(css_file) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

insert_css("css_files/settings.css")

@st.cache_data
def insert_html(html_file:str):
    with open(html_file) as f:
        return f.read()





about_col = st.columns([2,8,2],gap="small")

### blank columns
with about_col[0]:
    pass
with about_col[2]:
    pass

### main app column
with about_col[1]:

    ## inserting about 
    st.markdown(insert_html("html_files/about.html"),unsafe_allow_html=True)