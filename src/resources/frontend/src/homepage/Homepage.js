import React, { useState, useEffect } from 'react'
import LayoutAdmin from '../assets/admin/LayoutAdmin'
import Grid from '@mui/material/Grid';
import { sendGetRequest } from '../utils/requests';

console.log(process.env.REACT_APP_FETCH_URL);

const LanguagePlaceholder = (props) => {
    return (<></>)
}

const Homepage = (props) => {


    const [state, setState] = useState({
        'datasets': [],
    })

    useEffect(() => {
        sendGetRequest('/api/datasets').then((response) => {
            console.log(response.data)
            setState({ ...state, 'datasets': response.data })
        }).catch((error) => {
            console.log(error);
        })
    }, [])


    return (
        <LayoutAdmin
            main={
                <Grid container direction="column" justifyContent="flex-start" alignItems="flex-start" className="container-content">
                    <Grid item sx={{ ml: 4 }}>
                        <h1>PT-Pump-Up: Datasets</h1>
                    </Grid>
                    <Grid item sx={{ ml: 4 }}>
                        <h2>Dataset Index</h2>
                    </Grid>
                    <Grid item sx={{ ml: 4 }}>
                    </Grid>
                </Grid>
            }
        />
    )
}

export default Homepage