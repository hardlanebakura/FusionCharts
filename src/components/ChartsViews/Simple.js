import React, { useState, useEffect } from 'react';
import './charts.css';
import axios from 'axios';
import FusionCharts from 'fusioncharts';
import Charts from 'fusioncharts/fusioncharts.charts';
import ReactFC from 'react-fusioncharts';
import FusionTheme from 'fusioncharts/themes/fusioncharts.theme.fusion';

const Simple = ({chart}) => {

  chart = chart.toLowerCase().replaceAll(" ", "_");
  if (document.getElementsByTagName("select")[0] !== undefined) var caption = document.getElementsByTagName("select")[0][document.getElementsByTagName("select")[0].selectedIndex].innerText; 
  
  ReactFC.fcRoot(FusionCharts, Charts, FusionTheme);
  const [values, setValues] = useState([]);
  const subcaptions = {"Oil reserves": "In MMbbl = One Million barrels", "Least Stable Countries": "Instability index", "Most Stable Countries": "Instability index"};

  const getDataForMultiColumns = (response) => {
    var arr = response[chart].map((item) => Object.values(item));
    const countryNames = arr.map((item) => item[item.length - 1]);
    var values = [];
    for (const country of arr) {
      var sum = 0;
      for (const item of country) {
        if (!isNaN(parseInt(item))) sum += parseInt(item);
      }
      values.push((sum/4).toFixed(2));
    }
    var d = [];
    const map = new Map();
    for (let i = 0; i < countryNames.length; i++) map.set(countryNames[i], values[i]);
    arr = Object.entries(Object.fromEntries(map));
    for (const item of arr) d.push({"label": item[0], "value": item[1]});
    setValues(d);
    d.sort((a, b) => b.value - a.value);
    console.log(d);
    return d;
  }

  const getDataForOneColumn = (response) => {
    console.log(response[chart]);
    var d = [];
    for (const country of response[chart]) d.push({"label": country["country"], "value": country["index"]}); 
    setValues(d);
    return d;
  }

  const getData = async () => {
    const data = await axios.get("http://127.0.0.1:5000/countries");
    const response = await data.data;                    
    if (typeof(response[chart]) === "undefined") return false;

    return (Object.keys(response[chart][0]).length > 2) ? getDataForMultiColumns(response) : getDataForOneColumn(response);
  }

  useEffect(() => {
    getData()
    .then(response => { chart = document.getElementsByTagName("select")[0][document.getElementsByTagName("select")[0].selectedIndex].innerText.toLowerCase().replaceAll(" ", "_"); 
      if (response === false) { 
      getData(); } })
  }, [values.length === 0, chart])

  const getChartsConfig = () => {
    console.log(values);
    return <ReactFC {...chartConfig} />
  }

  const chartConfig = {
    type: 'column2d',
    width: 600,
    height: 400,
    dataFormat: 'json',
    dataSource: {
      "chart": {
        "caption": caption,
        "subCaption": subcaptions[caption],
        "xAxisName": "Country",
        "yAxisName": "",
        "numberSuffix": "",
        "theme": "fusion"
      },
      "data": values
    }
  };

  return (
    <div>
      { getChartsConfig() }
    </div>
  )
}

export default Simple