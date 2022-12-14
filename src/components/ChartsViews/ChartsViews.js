import React, { useState } from 'react';
import './charts.css';
import Chart from './Chart';
import SelectOptions from './SelectOptions';
import './charts.css';
import axios from 'axios';
import { useEffect } from 'react';
import gaugeData from './companies_with_highest_rating_indexes.json';

const ChartsViews = () => {

    const [selectedItem, setSelectedItem] = useState("Simple Chart");
    const [selected, setSelected] = useState("fragile_states_indexes");

    const activeClass = (e) => {
      e.target.classList.add("active");
      const arr = Array.from(document.getElementById("charts-row").getElementsByTagName("div"));
      for (const item of arr) if (item.innerText !== e.target.innerText) item.classList.remove("active");
      setSelectedItem(e.target.innerText);
    }

    const activeSelect = (e) => {
      setSelected(e.target.options[e.target.selectedIndex].value);
    }
  
    return (
        <div id = "chart">
          <div id = "charts-row">
            <div className = "charts-row__display-item active" onClick = { activeClass } >
              Simple Chart
            </div>
            <div className = "charts-row__display-item" onClick = { activeClass } >
              Gauge
            </div>
            <div className = "charts-row__display-item" onClick = { activeClass } >
              World Map
            </div>
            <div className = "charts-row__display-item" onClick = { activeClass } >
              Data Binding
            </div>
          </div>
          <select id = "world-select" onChange = { activeSelect } >
            <SelectOptions type = { selectedItem } gaugeData = { gaugeData } />
          </select>
          <Chart type = { selectedItem } chart = { selected } gaugeData = { gaugeData } />
        </div>
    );
}

export default ChartsViews