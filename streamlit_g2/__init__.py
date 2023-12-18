import os
import streamlit.components.v1 as components

_RELEASE = True
NAME = "g2"

if not _RELEASE:
    _component_func = components.declare_component(
        NAME,
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component(NAME, path=build_dir)

def g2(options, style=None, key=None):
    component_value = _component_func(options=options, style=style, key=key)
    return component_value

def st_g2(options, style=None, key=None):
    return g2(options, style, key=key)


# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run streamlit_g2/__init__.py`
if not _RELEASE:
    import streamlit as st

    options = {
        "autoFit": True,
        "theme": "dark",
        "type": "interval",
        "data": [
            { "genre": 'Sports', "sold": 275 },
            { "genre": 'Strategy', "sold": 115 },
            { "genre": 'Action', "sold": 120 },
            { "genre": 'Shooter', "sold": 350 },
            { "genre": 'Other', "sold": 150 },
        ],
        "encode": {
            "x": "genre",
            "y": "sold",
            "color": "genre",
        }
    }
    
    g2(options=options, style=None, key="streamlit_g2")
