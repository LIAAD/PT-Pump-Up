import React from 'react';
import ReactDOM from 'react-dom/client';
import Homepage from './homepage/Homepage';
import './assets/css/index.css'
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import DatasetIndex from './datasets/Index';
import ModelIndex from './models/Index';
import { Helmet } from "react-helmet";
import favicon_16x16 from './assets/favicon/favicon-16x16.png';
import favicon_32x32 from './assets/favicon/favicon-32x32.png';
import safari_pinned_tab from './assets/favicon/safari-pinned-tab.svg';



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
    <Helmet>
      <meta charSet="utf-8" />
      <title>Portuguese NLP Resources</title>
      <meta name="description" content="Hub for Portuguese NLP Resources"></meta>
      <link rel="icon" type="image/png" sizes="32x32" href={favicon_32x32} />
      <link rel="icon" type="image/png" sizes="16x16" href={favicon_16x16} />
      <link rel="mask-icon" href={safari_pinned_tab} color="#5bbad5" />
      <meta name="msapplication-TileColor" content="#da532c" />
      <meta name="theme-color" content="#ffffff" />
    </Helmet>
    <RouterProvider router={router} />
  </React.StrictMode>
);