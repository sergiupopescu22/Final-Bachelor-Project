import React from 'react';

function SelectedPoints(props) {
  const rows = props.items.map((item, index) => {
    return (
      <tr key={index}>
        <td>{index}</td>
        <td>{item.lat}, {item.lng}</td>
        <td>
            <button  onClick={() => erasePoint({index})}>Erase</button>
        </td>
      </tr>
    );
  });

  const erasePoint = (index) => {
    const updatedItems = [...props.items];
    updatedItems.splice(index, 1);
    props.setMarkers(updatedItems);
  };

  return (
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
  );
}

export default SelectedPoints;