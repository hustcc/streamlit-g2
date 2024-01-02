import React from 'react';
import {
  Streamlit,
  withStreamlitConnection,
  ComponentProps,
  Theme,
} from 'streamlit-component-lib';
import { Chart } from '@berryv/g2-react';

const SEP = '!!-_-____-_-!!';

/**
 * G2 Theme follow streamlit.
 */
function getDefaultTheme(theme: Theme | undefined): 'dark' | 'light' {
  return theme?.base === 'dark' ? 'dark' : 'light';
}

function processJSString(options: any): any {
  if (typeof options === 'string' && options.includes(SEP)) return eval(options.replaceAll('!!-_-____-_-!!', ''));
  if (Array.isArray(options)) {
    return options.map((o) => processJSString(o));
  }
  if (typeof options === 'object') {
    const o = { ...options };
    for (const key in options) {
      if (Object.prototype.hasOwnProperty.call(options, key)) {
        o[key] = processJSString(options[key])
      }
    }
    return o;
  }
  return options;
}

const G2Component: React.FC<ComponentProps> = (props) => {
  const { theme, args } = props;
  const { style, options } = args;

  const o = processJSString(options);

  return (
    <Chart
      style={{width: '100%', height: 400, ...style}} 
      options={{ theme: getDefaultTheme(theme), ...o }}
      onInit={() => Streamlit.setFrameHeight()}
    />
  )
};

export const G2 = withStreamlitConnection(G2Component)
