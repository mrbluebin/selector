import axios from "axios";
import { useParams } from "react-router-dom";
import { Link } from 'react-router-dom'
import React, { useEffect,useState } from 'react';
import ReactDOM, { render } from 'react-dom';


export default function StartSelector(tpyename){
    const { name } = useParams();
  
    const [typelist ,settp] = useState([]);
    const [quelist ,setque] = useState([]);
    const [quecount,setcount] = useState(0);
    const [anslist,setanslist] = useState([]);
    
    useEffect(()=>{
        if(quecount>0)
        {
            //console.log(quelist[quecount-1].que);
            
        }
    },[quecount]);
    
    function btnselect(getparm)
    {
        setanslist(anslist.concat(getparm));
        setcount(quecount+1) 
    }
    
    useEffect(()=>{
        axios.get("http://127.0.0.1:8000/pro/")
        .then((res) => {
          return(res.data)
        }).then(data => {
          settp(data)
          //console.log(data)
        })

        axios.get("http://127.0.0.1:8000/que/")
        .then((res) => {
          return(res.data)
        }).then(data => {
            setque(data)
          console.log(data)
        })
      },[]);

      const listview = anslist.map(item =>{
        return(
          <div>
            <li>{item}</li>
          </div>
        )
      })

      
    return(
      <>
        <div>
            <span>
            <button onClick={()=>{
            
                setcount(quecount+1)
            }}>{name} 선택 시작</button></span>

            {quelist[quecount] && <span><h1>{quelist[quecount].que}</h1>
            <button onClick={()=>{btnselect(quelist[quecount].ans1)}}>{quelist[quecount].ans1}</button>
          <button onClick={() => { btnselect(quelist[quecount].ans2) }}>{quelist[quecount].ans2}</button></span>}

          
        
        </div>
        <h2>선택 리스트</h2>
        {listview}
        
        
        
        </>
    )
   
}