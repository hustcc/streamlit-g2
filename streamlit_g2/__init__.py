import os
import streamlit.components.v1 as components
from streamlit_g2.spec import JS, json_dump_options

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
# Set _RELEASE = False to debug.
_RELEASE = True

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if not _RELEASE:
    _component_func = components.declare_component(
        "g2",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("g2", path=build_dir)


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def g2(options, style=None, key=None):
    """Create a new instance of "g2".

    Parameters
    ----------
    options: dict
        Required. The options/spec of g2 to be visualized.
    style: dict
        The style of dom container.
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.
    Returns
    -------
    none
        shows the visualization

    """
    # Call through to our private component function. Arguments we pass here
    # will be sent to the frontend, where they'll be available in an "args"
    # dictionary.
    #
    # "default" is a special argument that specifies the initial return
    # value of the component before the user has interacted with it.
    # Loop to change pd.DataFrame to JSON Object.
    o = json_dump_options(options)
    component_value = _component_func(options=o, style=style, key=key)
    return component_value

def st_g2(options, style=None, key=None):
    return g2(options, style, key=key)


# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit app.
#
# In frontend, `$ npm run start`
# `$ streamlit run streamlit_g2/__init__.py`
if not _RELEASE:
    import streamlit as st
    import pandas as pd

    df = pd.DataFrame(
        [["Sports", 275], ["Strategy", 115], ["Action", 120], ["Shooter", 350], ["Other", 150]],
        columns=["genre", "sold"],
    )

    options = {
        "autoFit": True,
        "type": "spaceFlex",
        "children": [
            {
                "type": "interval",
                "data": [
                    { "genre": "Sports", "sold": 275 },
                    { "genre": "Strategy", "sold": 115 },
                    { "genre": "Action", "sold": 120 },
                    { "genre": "Shooter", "sold": 350 },
                    { "genre": "Other", "sold": 150 },
                ],
                "encode": {
                    "x": "genre",
                    "y": "sold",
                    "color": JS('''(d) => d.sold > 200 ? "red" : "green"'''),
                },
                "scale": {
                    "color": { "type": "identity" }
                }
            },
            {
                "type": "line",
                "data": df,
                "encode": {
                    "x": "genre",
                    "y": "sold",
                    "shape": "smooth"
                },
                "style": {
                    "lineWidth": 2,
                }
            }
        ]
    }

    g2(options=options, style={ "height": "400px" }, key="streamlit-g2")
