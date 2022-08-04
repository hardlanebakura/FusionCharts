import React from 'react'

const DataBinding = (properties) => {
  return (
    <div id = "data-binding" onClick = { properties.activeClass } >DataBinding</div>
  )
}

export default DataBinding