import React from 'react';
import {
  Streamlit,
  withStreamlitConnection,
  ComponentProps,
  Theme,
} from 'streamlit-component-lib';
import { Chart } from '@berryv/g2-react';

/**
 * G2 Theme follow streamlit.
 */
function getDefaultTheme(theme: Theme | undefined): 'dark' | 'light' {
  return theme?.base === 'dark' ? 'dark' : 'light';
}

const G2Component: React.FC<ComponentProps> = (props) => {
  const { theme, args } = props;
  const { style, options } = args;

  return (
    <Chart
      style={{width: '100%', height: 400, ...style}} 
      options={{ theme: getDefaultTheme(theme), ...options }}
      onInit={() => Streamlit.setFrameHeight()}
    />
  )
};

export const G2 = withStreamlitConnection(G2Component)
