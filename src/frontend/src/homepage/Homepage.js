import React, { useState, useEffect } from 'react'
import LayoutAdmin from '../assets/admin/LayoutAdmin'
import Grid from '@mui/material/Grid';
import { sendGetRequest } from '../utils/requests';
import TableDatasets from './TableDatasets';

const Homepage = (props) => {

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
                    <TableDatasets />
                </Grid>
            }
        />
    )
}

export default Homepage