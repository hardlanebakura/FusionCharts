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
  var chart = "";
  for (const char of props.chart.toLowerCase().replaceAll(" ", "_").split("_")) chart += char[0];
  
  ReactFC.fcRoot(FusionCharts, Maps, World, FusionTheme);
  const [gradients, setGradients] = useState([]);
  const [values, setValues] = useState([]);
  const gradientOneColor = "4682b4";
  console.log("1");

  useEffect(() => {
    const getData = async () => {
      const data = await axios.get("http://127.0.0.1:5000/continents")
      const response = await data.data;
      console.log(response);
      console.log(response[chart]["gradients"]);
      setGradients(Object.values(response[chart]["gradients"]));
      var d = [];
      for (const item of Object.values(response[chart]["values"])) d.push({ "id": item["continent"], "value": item[chart], "showLabel": "1" });
      setValues(d);
      console.log(d);
    }
    getData();
    if (gradients.length > 0) gradients.sort((a, b) => a - b);
  }, [gradients.length === 0, props.chart])

  const getChartsConfig = () => {
    console.log(chartConfig.dataSource.data);
    console.log(values);
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
          "code": gradientOneColor,
          "gradient": "1",
          "color": [
            {
              "minvalue": gradients[0],
              "maxvalue": gradients[1],
              "color": "#ffa32f"
            },
            {
              "minvalue": gradients[1],
              "maxvalue": gradients[2],
              "color": "#E65100" //red
            },
            {
              "minvalue": gradients[2],
              "maxvalue": gradients[3],
              "color": gradientOneColor
            }
          ]
        },
        "data": values
      }
  }

  return (
    <div>
        { getChartsConfig() }
    </div>
  )
}

export default WorldMap;