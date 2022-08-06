import React, { useState, useEffect } from 'react';
import './charts.css';
import axios from 'axios';

const Simple = ({chart}) => {

  chart = chart.toLowerCase().replaceAll(" ", "_");

  const getData = () => {
    axios.get("http://127.0.0.1:5000/countries")
    .then(response => response.data)
    .then(response => console.log(response[chart]))
    .catch((error) => console.log(error));
  }

  getData();

  return (
    <div>Simple</div>
  )
}

export default Simple