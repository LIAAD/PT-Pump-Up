import React from 'react';
import ReactDOM from 'react-dom/client';
import Homepage from './homepage/Homepage';
import './assets/css/index.css'


const root = ReactDOM.createRoot(document.getElementById('root'));

const handleInputChange = (e, setState) => {
  const { name, value } = e.target;
  setState((prevData) => ({
    ...prevData,
    [name]: value,
  }));
};

root.render(
  <React.StrictMode>
    <Homepage handleInputChange={handleInputChange} />
  </React.StrictMode>
);