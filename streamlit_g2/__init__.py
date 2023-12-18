import os
import streamlit.components.v1 as components

parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "frontend/build")
_component_func = components.declare_component("g2", path=build_dir)

def g2(options, style=None, key=None):
    component_value = _component_func(options=options, style=style, key=key)
    return component_value

def st_g2(options, style=None, key=None):
    return g2(options, style, key=key)
