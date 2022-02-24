import React, { useState } from "react";
import axios from "axios";
import "./RestAPI.css";

function test(_tmp)
{
  console.log(_tmp);
}

function RestAPI() {
    const [productlist, setText] = useState([]);
    
    console.log(111);
    return (
      <>
        
        <div className="btn-all">
          <button
            onClick={() => {
              axios
                .get("http://127.0.0.1:8000/pro/")
                .then((response) => {
                  setText([...response.data]);
                  console.log(response.data);
                })
                .catch(function (error) {
                  console.log(error);
                });
            }}
          >
            Start
          </button>
        </div>

        {productlist.map((e,index)=>(
          <div>
            {index}번째 데이터
            <div>
              <span>
                이름:{e.name} > 리스트:{e.taglist}
              </span>
            </div>
          </div>
        ))}
        
        <span>

       {productlist.map(item => (
         <button>{item.name}</button>
       ))}</span>


        {/*
        <div className="testbtn">
          <button onClick={() => {
            test(productlist[0]);
          }}>콘솔 텍스트</button>
        </div>*/}

        
        {/*text.map((e,index) => (
          <div>
            {" "}
            <div key = {index} className={index}>
              <span key ={e.idx}>
                idx = {e.idx} -> con = {e.con}
              </span>
            </div>
          </div>
        ))}

        <div className="sdf">
          <button onClick={()=>{
            
            axios.get("http://127.0.0.1:8000/tt/2").then((response)=>{
              setgj(response.data).catch(function (error) {
                console.log(error);
              });
            })
          }}>2 data get</button>
        </div>

        <div className="regf">
          <button onClick={()=>{
            setidx(gj.idx);
          }}>idx print</button>
        </div>

        <div className="regf">
          <button onClick={()=>{
            setcon(gj.con);
          }}>con print</button>
        </div>

        <h>idx > {gidx}</h>
        <h>con > {gcon}</h>*/}
        
        
      
      </>
    );
  }
  
  export default RestAPI;

