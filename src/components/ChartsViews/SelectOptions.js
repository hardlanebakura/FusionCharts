import React from 'react';
import axios from 'axios';

const SelectOptions = ({type, gaugeData}) => {
  
  const getSimpleChartOptions = () => {
        return (
            <>
                <option>Oil reserves</option>
                <option>Least Stable Countries</option>
                <option>Most Stable Countries</option>
            </>
          )
  }
    
  const getGaugeOptions = () => {
        
        console.log(gaugeData);

        return (
            <>
              { gaugeData.map((item) => {
                return (
                 <option>{ item["company"] }</option>   
                )
              }) } 
            </>
          )
  }

  const getWorldMapOptions = () => {
    return (
        <>
            <option>Fragile States Indexes</option>
            <option>Factionalized Elites Indexes</option>
            <option>Group Grievances Indexes</option>
            <option>Military Spendings Indexes</option>
            <option>Military Spendings Percentages Indexes</option>
        </>
      )
  }

  const getDataBindingOptions = () => {
    return (
        <>
            <option>Average temperatures in US</option>
            <option>TV times in US</option>
            <option>Depression rates in US</option>
            <option>Uninsurance rates in US</option>
        </>
      )
  }

  return (type === "Simple Chart") ? getSimpleChartOptions() : (type === "Gauge") ? getGaugeOptions() : (type === "World Map") ? getWorldMapOptions() : getDataBindingOptions();
  
}

export default SelectOptions