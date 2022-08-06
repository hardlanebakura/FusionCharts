import React from 'react'

const SelectOptions = ({type}) => {
  
  const getSimpleChartOptions = () => {
        return (
            <>
                <option>Least Stable Countries</option>
                <option>Most Stable Countries</option>
            </>
          )
  }
    
  const getGaugeOptions = () => {
        return (
            <>
                <option>Least Stable Countries</option>
                <option>Most Stable Countries</option>
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
            <option>Fragile States Indexes</option>
            <option>Factionalized Elites Indexes</option>
            <option>Group Grievances Indexes</option>
            <option>Military Spendings Indexes</option>
            <option>Military Spendings Percentages Indexes</option>
        </>
      )
  }

  return (type === "Simple Chart") ? getSimpleChartOptions() : (type === "Gauge") ? getGaugeOptions() : (type === "World Map") ? getWorldMapOptions() : getDataBindingOptions();
  
}

export default SelectOptions