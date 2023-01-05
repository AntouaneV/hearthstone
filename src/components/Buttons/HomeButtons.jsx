import React from 'react';
import { useNavigate } from 'react-router-dom';

const HomeButtons = () => {
  const navigate = useNavigate();

  const goShop = () => {
    navigate('/shop');
  };
  const playBtn = () => {
    console.log('Hello');
  };
  return (
    <div className="flex flex-col">
      <button
        className="font-mono mt-4 bg-slate-600 rounded pt-4 pb-4 text-white pl-40 pr-40 hover:border-solid hover:bg-slate-700 shadow"
        onClick={playBtn}
      >
        Jouer
      </button>
      <button
        className="font-mono mt-4 bg-slate-600 rounded pt-4 pb-4 text-white hover:bg-slate-700 shadow"
        onClick={() => {
          navigate('/collection');
        }}
      >
        Ma Collection
      </button>
      <button
        className="font-mono mt-4 bg-slate-600 rounded pt-4 pb-4 text-white hover:bg-slate-700 shadow"
        onClick={goShop}
      >
        Boutique
      </button>
    </div>
  );
};

export default HomeButtons;
