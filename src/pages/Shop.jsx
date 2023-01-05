import React from 'react';
import { useNavigate } from 'react-router-dom';

function Shop() {
  const navigate = useNavigate();
  const goBack = () => {
    navigate('/');
  };
  return (
    <div className="shop">
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
      <img
        className="absolute top-0 left-0 w-full h-full object-cover opacity-95 -z-10"
        src="background.jpeg"
        alt="background"
      />
      <div className="absolute w-full h-full flex flex-row text-center items-center justify-center">
        <div className="flex flex-col bg-slate-800 opacity-70 rounded p-6">
          <div className="flex text-center items-center justify-center">
            <img
              className=""
              src="logo.png"
              height="100%"
              width={250}
              alt="logo images"
            />
          </div>

          <div className="flex flex-row flex-wrap text-center items-center justify-center">
            <div className="m-2 flex flex-col">
              <p className="font-bold text-white text-left">Pack Faible</p>
              <img
                className="opacity-100"
                src="pack_1.png"
                width={240}
                height={480}
                alt=""
              />
              <h1 className="font-bold text-white text-left">€ 10.00</h1>
              <button className="bg-orange-300 mt-2 rounded shadow p-4 text-white hover:bg-orange-400">
                Acheter
              </button>
            </div>

            <div className="m-2 flex flex-col">
              <p className="font-bold text-white text-left">Pack Moyen</p>
              <img
                className="opacity-100"
                src="pack_2.png"
                width={240}
                height={480}
                alt=""
              />
              <h1 className="font-bold text-white text-left">€ 30.00</h1>
              <button className="bg-orange-300 mt-2 rounded shadow p-4 text-white hover:bg-orange-400">
                Acheter
              </button>
            </div>

            <div className="m-2 flex flex-col">
              <p className="font-bold text-white text-left">Pack Fort</p>
              <img
                className="opacity-100"
                src="pack_3.png"
                width={240}
                height={480}
                alt=""
              />
              <h1 className="font-bold text-white text-left">€ 50.00</h1>
              <button className="bg-orange-300 mt-2 rounded shadow p-4 text-white hover:bg-orange-400">
                Acheter
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Shop;
