import React, { useEffect,useState } from 'react';
import {Link} from 'react-router-dom';
import axios from "axios";
import ReactDOM from 'react-dom';

function Mainpage () {
  const [typelist ,settp] = useState([]);

    useEffect(()=>{
      axios.get("http://127.0.0.1:8000/type/")
      .then((res) => {
        return(res.data)
      }).then(data => {
        settp(data)
        console.log(data)
      })
    },[]);

    return (
      <div>
      {typelist.map((item,index)=>(
        <span key={index}>
        <Link to={`/selector/${item.name}`}>
        <button >{item.name}</button></Link></span>
      ))}
      </div>
  );
}


export default Mainpage;


