import React, { useState, useEffect } from 'react';
import './charts.css';
import FusionCharts from 'fusioncharts';
import charts from 'fusioncharts/fusioncharts.charts';
import ReactFusionCharts from 'react-fusioncharts';

const DataBinding = ({chart}) => {

  console.log(chart);

  useEffect(() => {
    console.log(document.getElementsByTagName("select")[0][document.getElementsByTagName("select")[0].selectedIndex].innerText);
  }, [document.getElementsByTagName("select")[0][document.getElementsByTagName("select")[0].selectedIndex].innerText])

  return (
    <div id = "data-binding">
      DataBinding
    </div>
  )
}

export default DataBinding