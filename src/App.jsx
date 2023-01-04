import HomeButtons from './components/Buttons/HomeButtons';

function App() {
  return (
    <div className="App ">
      <div className="absolute top-0 right-0 z-10">
        <div className="w-14 h-14 mt-6 mr-6 z-10 cursor-pointer">
          <img src="shutdown.png" alt="pipe wrench" height={60} width={60} />
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
              width={350}
              alt="logo images"
            />
          </div>

          <HomeButtons />
        </div>
      </div>
    </div>
  );
}

export default App;
