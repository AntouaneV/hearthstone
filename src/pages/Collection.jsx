import React from 'react';
import { useNavigate } from 'react-router-dom';
import HomeButtons from '../components/Buttons/HomeButtons';

function Collection() {
  const navigate = useNavigate();
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
            <div className="w-56 h-72 bg-green-200 m-2 rounded-sm"></div>
            <div className="w-56 h-72 bg-green-200 m-2 rounded-sm"></div>
            <div className="w-56 h-72 bg-green-200 m-2 rounded-sm"></div>
            <div className="w-56 h-72 bg-green-200 m-2 rounded-sm"></div>
            <div className="w-56 h-72 bg-green-200 m-2 rounded-sm"></div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Collection;
