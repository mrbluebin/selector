import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          selector project.
        </p>
        <a
          className="App-link"
          href="/" //주소
          target="_blank"
          rel="noopener noreferrer"
        >
          버튼
        </a>
      </header>
    </div>
  );
}

export default App;
