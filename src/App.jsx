function App() {
  const playBtn = () => {
    console.log('Hello');
  };

  return (
    <div className="App ">
      <div className="absolute top-0 right-0 z-10">
        <div className="w-14 h-14 mt-6 mr-6 z-10 bg-orange-400"></div>
        <div className="w-14 h-14 mt-6 mr-6 z-10 bg-orange-400"></div>
        <div className="w-14 h-14 mt-6 mr-6 z-10 bg-orange-400"></div>
      </div>
      <img
        className="absolute top-0 left-0 w-full h-full object-cover opacity-95 -z-10"
        src="background2.jpeg"
        alt="background"
      />
      <div className="absolute w-full h-full flex flex-row text-center items-center justify-center">
        <div className="flex flex-col bg-slate-800 opacity-70 rounded p-6">
          <div className="flex text-center items-center justify-center">
            <img
              className=""
              src="logo.png"
              height="100%"
              width={350}
              alt="logo images"
            />
          </div>

          <div className="flex flex-col">
            <button
              className="font-mono mt-4 bg-slate-600 rounded pt-4 pb-4 text-white pl-40 pr-40 hover:border-solid hover:border hover:border-orange-400"
              onClick={playBtn}
            >
              Jouer
            </button>
            <button className="font-mono mt-4 bg-slate-600 rounded pt-4 pb-4 text-white hover:border hover:border-orange-400">
              Aventure
            </button>
            <button className="font-mono mt-4 bg-slate-600 rounded pt-4 pb-4 text-white hover:border hover:border-orange-400">
              Arène
            </button>
          </div>
          <div className="flex flex-row mt-6 justify-between">
            <button className="font-mono bg-orange-400 rounded p-6">
              Ouvrir des <br /> paquets
            </button>
            <button className="font-mono bg-orange-400 rounded p-6">
              Ma collection
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
