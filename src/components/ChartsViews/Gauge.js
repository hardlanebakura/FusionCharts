import React, { useState } from 'react'

const Gauge = (properties) => {

  return (
    <div id = "gauge" onClick = { properties.activeClass } >Gauge</div>
  )
}

export default Gauge