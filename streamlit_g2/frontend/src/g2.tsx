import React, { useEffect } from 'react';
import {
  Streamlit,
  withStreamlitConnection,
  ComponentProps,
} from 'streamlit-component-lib';
import { Chart } from '@berryv/g2-react';

const G2Component: React.FC<ComponentProps> = (props) => {
  const { style, options } = props.args

  return (
    <Chart
      style={{width: '100%', height: 400, ...style}} 
      options={options}
      onInit={() => Streamlit.setFrameHeight()}
    />
  )
};

export const G2 = withStreamlitConnection(G2Component)
