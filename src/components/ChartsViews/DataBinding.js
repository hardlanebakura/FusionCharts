import React, { useState, useEffect } from 'react';
import './charts.css';
import axios from 'axios';
import FusionCharts from 'fusioncharts';
import Maps from 'fusioncharts/fusioncharts.maps';
import USA from 'fusioncharts/maps/fusioncharts.usa';
import ReactFC from 'react-fusioncharts';
import FusionTheme from 'fusioncharts/themes/fusioncharts.theme.fusion';

const DataBinding = ({chart}) => {

  const [values, setValues] = useState([]);
  const [gradients, setGradients] = useState(["20", "40", "60", "80"]);
  const options = { "Average temperatures in US": "temperatures", "TV times in US": "tv_times", "Depression rates in US": "depression_rates", "Uninsurance rates in US": "uninsurance_rates"};
  var activeOption = Object.values(options)[Object.keys(options).indexOf(document.getElementsByTagName("select")[0][document.getElementsByTagName("select")[0].selectedIndex].innerText)];
  const getChart = (string) => { chart = ""; for (const char of string.toLowerCase().replaceAll(" ", "_").split("_")) chart += char[0]; return chart; }
  var fusionChart = document.getElementsByTagName("select")[0][document.getElementsByTagName("select")[0].selectedIndex].innerText;

  ReactFC.fcRoot(FusionCharts, Maps, USA, FusionTheme);
  
  const getData = async () => {
    const data = await axios.get("http://127.0.0.1:5000/states");
    const response = await data.data;
    return response;
  }

  const getChartsConfig = () => {
    activeOption = Object.values(options)[Object.keys(options).indexOf(document.getElementsByTagName("select")[0][document.getElementsByTagName("select")[0].selectedIndex].innerText)];
    console.log(Object.keys(options).indexOf(document.getElementsByTagName("select")[0][document.getElementsByTagName("select")[0].selectedIndex].innerText) === -1);
    console.log(activeOption);
    console.log(values);
    var d = {
      type: "USA",
      width: 600,
      height: 400,
      dataFormat: "json",
      dataSource: dataSource
    }
    if (values.length > 0) 
        return (
          <ReactFC {...d} />
    )
  }

  const dataSource = {
      chart: {
        caption: fusionChart,
        subcaption: "",
        entityfillhovercolor: "#F8F8E9",
        numbersuffix: (activeOption === "temperatures") ? "°F" : "",
        showlabels: "1",
        borderthickness: "0.4",
        theme: "fusion",
        entitytooltext:
          "<b>$lname</b> has an average temperature of <b>$datavalue</b>"
      },
      colorrange: {
        minvalue: gradients[0],
        code: "4682b4",
        gradient: "1",
        color: [
          {
            minvalue: gradients[0],
            maxvalue: gradients[1],
            code: "#EFD951"
          },
          {
            minvalue: gradients[1],
            maxvalue: gradients[2],
            code: "#FD8963"
          },
          {
            minvalue: gradients[2],
            maxvalue: gradients[3],
            code: "#D60100"
          }
        ]
      },
      data: values
    };

  const setAllGradients = (arr) => {
    const arr1 = arr.map((item) => item["value"]);
    const min = Math.min(...arr1);
    const max = Math.max(...arr1);
    const gradientOne = min + (max - min) * 0.33;
    const gradientTwo = min + (max - min) * 0.67;
    setGradients([min, gradientOne, gradientTwo, max]);
  }

  useEffect(() => {
    console.log(document.getElementsByTagName("select")[0][document.getElementsByTagName("select")[0].selectedIndex].innerText);
    getData()
    .then(response => { 
      var d = response[options[document.getElementsByTagName("select")[0][document.getElementsByTagName("select")[0].selectedIndex].innerText]];
      var states = [];
      for (const item of d) { 
        states.push({ "id": item["state_id"], "value": (item["value"].toString().includes("%")) ? item["value"].split("%")[0] : item["value"] });
      }
      setAllGradients(states)
      setValues(states); 
    })
    .catch((error) => console.log(error));
  }, [document.getElementsByTagName("select")[0][document.getElementsByTagName("select")[0].selectedIndex].innerText], chart)

  return (
    <div id = "data-binding">
      { getChartsConfig() }
    </div>
  )
}

export default DataBinding