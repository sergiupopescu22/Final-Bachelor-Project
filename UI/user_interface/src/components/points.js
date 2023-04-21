import React from 'react';
import axios from 'axios';

function SelectedPoints(props) {

  const rows = props.markers.map((item, index) => {
    return (
      <tr key={index}>
        <td>{index}</td>
        <td>{item.lat}, {item.lng}</td>
        <td>
            <button  onClick={() => erasePoint(index)}>Erase</button>
        </td>
      </tr>
    );
  });

  const erasePoint = (index) => {
    const updatedItems = [...props.markers];
    console.log(index)
    updatedItems.splice(index, 1);
    props.setMarkers(updatedItems);
  };

  const handleClick = (command) => {

    const data = {
      type: command,
      waypoints: props.markers
    };

    console.log(props.markers);

    // 'http://192.168.88.233:8000/command/'

    axios.post('http://192.168.88.15:8000/command/', data)
      .then(response => {
        // setData(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  };

  return (
    <div>
      {rows.length === 0 ? <p className="select_text">
        Please select on the map the desired waypoints for the mission</p> : 
      <div>
      <table>
        <thead>
          <tr>
          <th>Number</th>
          <th>Position</th>
          <th>Delete</th>
          </tr>
        </thead>
        <tbody>
          {rows}
        </tbody>
      </table>
      <div style={{textAlign:'center'}}>
      <button className="start_mission_button" onClick={() => handleClick(7)}>Start Mission</button>
      </div>
      </div>
    }
    </div>
  );
}

export default SelectedPoints;