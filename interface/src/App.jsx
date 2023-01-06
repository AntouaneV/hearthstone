import HomeButtons from './components/Buttons/HomeButtons';
import Lottie from 'react-lottie';
import animationData from './lotties/lf30_editor_tgrcz2aj.json';

function App() {
  const defaultOptions = {
    loop: true,
    autoplay: true,
    animationData: animationData,
    // rendererSettings: {
    //   preserveAspectRatio: 'xMidYMid slice',
    // },
  };

  return (
    <div className="App ">
      <div className="absolute top-0 right-0 z-10">
        <div className="w-14 h-14 mt-6 mr-6 z-10 cursor-pointer">
          <img src="logout.png" alt="pipe wrench" height={60} width={60} />
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

          <div className="flex flex-row mt-2 text-center items-center">
            <div className="text-left">
              <Lottie
                options={defaultOptions}
                height={100}
                width={100}
                isClickToPauseDisabled={true}
              />
            </div>

            <div className="flex flex-col text-left ml-4">
              <p className="text-white font-bold">
                <span className="text-orange-300 font-bold">
                  Hearthstone credentials{' '}
                </span>
              </p>
              <p className="text-white font-bold">
                <span className="text-orange-300 font-bold">Pseudo : </span>
                Guizmo
              </p>
              <p className="text-white font-bold">
                <span className="text-orange-300 font-bold">ID : </span>
                #VLG93
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
