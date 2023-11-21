import React from 'react';
import ReactDOM from 'react-dom/client';
import Homepage from './homepage/Homepage';
import './assets/css/index.css'
import { createBrowserRouter, RouterProvider, Route, Link } from "react-router-dom";
import DatasetIndex from './datasets/Index';
import ModelIndex from './models/Index';

const handleInputChange = (e, setState) => {
  const { name, value } = e.target;
  setState((prevData) => ({
    ...prevData,
    [name]: value,
  }));
};

const router = createBrowserRouter([
  {
    path: "/",
    element: <Homepage />,
  },
  {
    path: "models",
    element: <ModelIndex />,
  },
  {
    path: "datasets",
    element: <DatasetIndex />,
  }
]);


const root = ReactDOM.createRoot(document.getElementById('root'));


root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);