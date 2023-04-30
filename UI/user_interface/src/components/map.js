import { useState, useMemo, useEffect } from "react";
import { GoogleMap, LoadScript, Marker} from "@react-google-maps/api";
import customMarkerIcon from './drone1.png';
import SelectedPoints from './points.js'
  
export default function Map(props) {

    const center_var = useMemo(()=>(props.position),[]);

    const [loadMarker, setLoadMarker] = useState(false);
    const [markers, setMarkers] = useState([]);

    useEffect(() => {
        const timer = setTimeout(() => {
        setLoadMarker(true);
        }, 1000); // wait for 1 second

        return () => clearTimeout(timer);
    }, []);
    
    return (
    <LoadScript
        googleMapsApiKey="to be added"
    >
        <GoogleMap
        mapContainerClassName="gmaps-container"
        center={center_var}
        zoom={17}
        onClick={(event)=>{
            props.visibleForm && setMarkers((prevItems)=>[...prevItems,
              {
                lat:event.latLng.lat(),
                lng:event.latLng.lng(),
                time: new Date(),
              },
            ]);
            // props.setSelected({lat:event.latLng.lat(), lng:event.latLng.lng()});
          }}
        >
         {loadMarker && <Marker 
            position={props.position} 
            icon={{
                url:customMarkerIcon,
                scaledSize: new window.google.maps.Size(60, 60)
                }}/>}

        {markers.map((marker, index) => (<Marker 
            label = {`${index}`}  
            position={{lat: marker.lat, lng: marker.lng}} 
            />)) }
        
        </GoogleMap>

        {props.visibleForm && 
        <div className="mision-waypoints">
            <SelectedPoints markers={markers} setMarkers={setMarkers}/>
        </div>
        }

    </LoadScript>
    )
}