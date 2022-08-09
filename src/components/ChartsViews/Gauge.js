import React, { useState, useEffect } from 'react';
import './charts.css';
import axios from 'axios';
import FusionCharts from 'fusioncharts';
import Widgets from 'fusioncharts/fusioncharts.widgets';
import ReactFC from 'react-fusioncharts';
import FusionTheme from 'fusioncharts/themes/fusioncharts.theme.fusion';

const Gauge = ({chart, gaugeData}) => {

  var selectedItem = document.getElementsByTagName("select")[0][document.getElementsByTagName("select")[0].selectedIndex].innerText;
  const [values, setValues] = useState((chart in gaugeData[0]) ? gaugeData.filter((item) => item.company === chart)[0]["satisfaction_percentage"] : []);
  const [selected, setSelected] = useState(selectedItem);

  ReactFC.fcRoot(FusionCharts, Widgets, FusionTheme);

  const getChartsConfig = () => {
    return <ReactFC {...chartConfig} />
  }

  useEffect(() => {
    //console.log(document.getElementsByTagName("select")[0][document.getElementsByTagName("select")[0].selectedIndex].innerText);
    setSelected(document.getElementsByTagName("select")[0][document.getElementsByTagName("select")[0].selectedIndex].innerText)
    setValues([gaugeData.filter((item) => item.company === document.getElementsByTagName("select")[0][document.getElementsByTagName("select")[0].selectedIndex].innerText)[0]["satisfaction_percentage"]])
  }, [selectedItem]);

  const chartConfig = {
    type: 'angulargauge',
    width: 600,
    height: 400,
    dataFormat: 'json',
    dataSource: {
      "chart": {
        "caption": `${selected}'s Rating Satisfaction Score`,
        "lowerLimit": "0",
        "upperLimit": "100",
        "showValue": "1",
        "numberSuffix": "%",
        "theme": "fusion",
        "showToolTip": "0"
      },
      "colorRange": {
        "color": [
          {
            "minValue": "0",
            "maxValue": "50",
            "code": "#F2726F"
          },
          {
            "minValue": "50",
            "maxValue": "75",
            "code": "#FFC533"
          },
          {
            "minValue": "75",
            "maxValue": "100",
            "code": "#62B58F"
          }
        ]
      },
      "dials": {
        "dial": [
          {
            "value": values
          }
        ]
      }
    }
    
  };

  return (
    <div id = "gauge">
      { getChartsConfig() }
    </div>
  )
}

export default Gauge