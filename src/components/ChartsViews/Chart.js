import React, { useState, useEffect } from 'react';
import './charts.css';
import { Simple, Gauge, WorldMap, DataBinding } from '../../components/';

const Chart = (props) => {

  console.log(props.chart);
  console.log(props.type);
  console.log(props.chart.toLowerCase().replaceAll(" ", "_"));

  useEffect(() => {

  })

  return (
    <div>
      { (props.type === "Simple Chart") ? <Simple /> : (props.type === "Gauge") ? <Gauge /> : (props.type === "Data Binding") ? <DataBinding /> : (props.type === "World Map") ? <WorldMap type = { props.type } chart = { props.chart } /> : <div>1</div> }
    </div>
  )
}

export default Chart