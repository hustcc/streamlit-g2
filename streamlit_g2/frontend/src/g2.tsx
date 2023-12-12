import React, { useEffect } from 'react';
import {
  Streamlit,
  withStreamlitConnection,
  ComponentProps,
} from 'streamlit-component-lib';
import { Chart } from '@berryv/g2-react';

const G2Component: React.FC<ComponentProps> = (props) => {
  const { style, options } = props.args
  useEffect(() => {
    Streamlit.setFrameHeight()
  }, []);
  return (
    <Chart style={style} options={options} />
  )
};

export const G2 = withStreamlitConnection(G2Component)
