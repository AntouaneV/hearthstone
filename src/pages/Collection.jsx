import axios from 'axios';
import React from 'react';
import { useState } from 'react';
import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import HomeButtons from '../components/Buttons/HomeButtons';

function Collection() {
  const navigate = useNavigate();
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/cards').then((response) => {
      setData(response.data);
      console.log(response.data)
    });
  },[])

  const goBack = () => {
    navigate('/');
  };
  return (
    <div className="collection">
      <div className="absolute top-0 right-0 z-10">
        <div className="w-14 h-14 mt-6 mr-6 z-10 cursor-pointer">
          <img src="logout.png" alt="pipe wrench" height={60} width={60} />
        </div>
      </div>
      <div className="absolute top-0 left-0 z-10">
        <div
          className="w-14 h-14 mt-6 ml-6 z-10 cursor-pointer"
          onClick={goBack}
        >
          <img src="previous.png" alt="pipe wrench" height={60} width={60} />
        </div>
      </div>
      {/* BLABLA */}
      <img
        className="absolute top-0 left-0 w-full h-full object-cover opacity-95 -z-10"
        src="background.jpeg"
        alt="background"
      />
      {/* BLABLA */}
      {/* <div className="relative w-full max-h-screen flex flex-row text-center items-center justify-center overflow-y-scroll mt-4 mb-4">
        <div className="flex flex-col bg-slate-800 opacity-70 rounded p-6 m-2">
          <h1 className="">ERARZE</h1>
          <HomeButtons />
          <HomeButtons />
          <HomeButtons />
        </div>
      </div> */}
      <div className="relative w-screen h-screen flex flex-col text-center items-center justify-center p-4">
        <div className="bg-slate-800 opacity-70 rounded h-screen overflow-y-scroll p-4">
          <div className="flex text-center items-center justify-center">
            <img
              className=""
              src="logo.png"
              height="100%"
              width={250}
              alt="logo images"
            />
          </div>
          <div className="flex flex-row flex-wrap text-center items-center justify-start">
            {
              data.map((data_unit) => 
              <div key={data_unit.id} className="w-56 h-72 bg-green-200 m-2 rounded-sm text-left p-2">
                <h1>name : {data_unit.name}</h1>
                <h1>playerClass : {data_unit.playerClass}</h1>
                <h1>type : {data_unit.type}</h1>
                <h1>text : {data_unit.text}</h1>
                </div>
              )
            }
          </div>
        </div>
      </div>
    </div>
  );
}

export default Collection;
