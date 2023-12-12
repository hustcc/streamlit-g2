<h1 align="center">
  <b>streamlit G2</b>
</h1>

<div align="center">

[G2](https://github./com/antvis/G2) is a visualization grammar for dashboard building, data exploration and storytelling.

This project was created to allow us to render [G2](https://github./com/antvis/G2) charts in streamlit.

![examples](https://mdn.alipayobjects.com/huamei_qa8qxu/afts/img/A*_GfqQoRCqQkAAAAAAAAAAAAADmJ7AQ/fmt.webp)

[![Build Status](https://github.com/antvis/g2/workflows/build/badge.svg?branch=v5)](https://github.com/antvis//actions)
[![Coverage Status](https://img.shields.io/coveralls/github/antvis/g2/v5.svg)](https://coveralls.io/github/antvis/g2?branch=v5)
[![npm Version](https://img.shields.io/npm/v/@antv/g2.svg)](https://www.npmjs.com/package/@antv/g2)
[![npm Download](https://img.shields.io/npm/dm/@antv/g2.svg)](https://www.npmjs.com/package/@antv/g2)
[![npm License](https://img.shields.io/npm/l/@antv/g2.svg)](https://www.npmjs.com/package/@antv/g2)

</div>


## Installation

```
pip install streamlit-g2 
```


## Usage

```py
import streamlit as st
from streamlit_g2 import g2

options = {
    "type": "interval",
    "data": [
        { "genre": 'Sports', "sold": 275 },
        { "genre": 'Strategy', "sold": 115 },
        { "genre": 'Action', "sold": 120 },
        { "genre": 'Shooter', "sold": 350 },
        { "genre": 'Other', "sold": 150 },
    ],
    "encoding": {
        "x": "genre",
        "y": "sold",
        "color": "genre",
    }
}

g2(options=options, style={"width": "100%", "height": "300px"}, key="streamlit_g2")
```

<img src="https://mdn.alipayobjects.com/huamei_qa8qxu/afts/img/A*XqCnTbkpAkQAAAAAAAAAAAAADmJ7AQ/fmt.webp" width="640" alt="example">


## API

Now, There is only one API for `streamlit-g2`, named `g2`, see the `options` in [G2 Spec API](https://g2.antv.antgroup.com/manual/core/api).

| Property | Description                                                                                                     | Type                  | Default |
| -------- | --------------------------------------------------------------------------------------------------------------- | --------------------- | ------- |
| options  | the [options](https://g2.antv.antgroup.com/manual/core/api) for the visualization, say `chart.options(options)` | `G2options` \| `null` | -       |
| style    | the style of the container                                                                                      | `CSSProperties`       | -       |


## License

MIT@[hustcc](https://github.com/hustcc).
