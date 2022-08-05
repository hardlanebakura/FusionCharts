import React, { useState, useEffect } from 'react';
import './charts.css';
import FusionCharts from 'fusioncharts';
import Maps from 'fusioncharts/fusioncharts.maps';
import World from 'fusioncharts/maps/fusioncharts.world';
import ReactFC from 'react-fusioncharts';
import FusionTheme from 'fusioncharts/themes/fusioncharts.theme.fusion';
import axios from 'axios';
import { getConfig } from '@testing-library/react';

const WorldMap = (props) => {

  console.log(props.chart);
  console.log(props.type);
  console.log(props.chart.toLowerCase().replaceAll(" ", "_"));
  const chart = props.chart.toLowerCase();
  
  ReactFC.fcRoot(FusionCharts, Maps, World, FusionTheme);
  const [gradients, setGradients] = useState([]);
  const [allValues, setAllValues] = useState([]);

  useEffect(() => {
    const getData = async () => {
      const data = await axios.get("http://127.0.0.1:5000/continents")
      const response = await data.data;
      setGradients(Object.values(response["fsi"]["gradients"]));
    }
    getData();
    if (gradients.length > 0) gradients.sort((a, b) => a - b);
  }, [gradients.length === 0])

  const getChartsConfig = () => {
    return (
      <>
        { gradients.length === 0 ? <></> : <ReactFC {...chartConfig} /> }
      </>
    )
  }

  const chartConfig = {
    type: "world",
    width: 600,
    height: 400,
    dataFormat: "json",
    dataSource: {
        "chart": {
          "caption": props.type,
          "subcaption": props.chart,
          "numbersuffix": "",
          "includevalueinlabels": "1",
          "labelsepchar": ": ",
          "entityFillHoverColor": "#FFF9C4",
          "theme": "fusion"
        },
        "colorrange": {
          "minvalue": gradients[0],
          "code": "#FFE0B2",
          "gradient": "1",
          "color": [
            {
              "minvalue": gradients[0],
              "maxvalue": gradients[1],
              "color": "#FFD74D"
            },
            {
              "minvalue": gradients[1],
              "maxvalue": gradients[2],
              "color": "#FB8C00"
            },
            {
              "minvalue": gradients[2],
              "maxvalue": gradients[3],
              "color": "#E65100"
            }
          ]
        },
        "data": [
          {
            "id": "NA",
            "value": ".82",
            "showLabel": "1"
          },
          {
            "id": "SA",
            "value": "2.04",
            "showLabel": "1"
          },
          {
            "id": "AS",
            "value": "1.78",
            "showLabel": "1"
          },
          {
            "id": "EU",
            "value": ".40",
            "showLabel": "1"
          },
          {
            "id": "AF",
            "value": "2.58",
            "showLabel": "1"
          },
          {
            "id": "AU",
            "value": "1.30",
            "showLabel": "1"
          }
        ]
      }
  }

  return (
    <div>
        { getChartsConfig() }
    </div>
  )
}

export default WorldMap;