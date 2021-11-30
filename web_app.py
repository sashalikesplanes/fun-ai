import streamlit as st
from fastbook import *


path = Path.cwd()
print(path)
@st.cache()
def get_jokes():
    return pd.read_excel(path/'data'/'key.xlsx', header=None)

jokes = get_jokes()

joke_text = st.empty()
if 'joke_id' not in st.session_state:
    st.session_state['joke_id'] = 0
#print()
if st.button('Next Joke'):
    st.session_state['joke_id'] += 1
    joke_text.caption(jokes.loc[st.session_state['joke_id']][0])
elif st.button("Prev Joke"):
    st.session_state['joke_id'] -= 1
    joke_text.caption(jokes.loc[st.session_state['joke_id']][0])
def update_joke():
    st.session_state['joke_id'] += 1
    joke_text.caption(jokes.loc[st.session_state['joke_id']][0])
age = st.slider('How old are you?', 0., 130., 25., on_change=update_joke())
st.write("I'm ", age, 'years old')