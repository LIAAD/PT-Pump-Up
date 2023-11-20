import React, { useState, useEffect } from 'react'
import LayoutAdmin from '../assets/admin/LayoutAdmin'
import Grid from '@mui/material/Grid';
import { sendGetRequest } from '../utils/requests';
import TableDatasets from './TableDatasets';

const Homepage = (props) => {

    return (
        <LayoutAdmin
            main={
                <Grid container justifyContent="flex-start" alignItems="flex-start" className="container-content" sx={{ pl: 3 }}>
                    <Grid item xs={12}>
                        <h1>PT-Pump-Up</h1>
                    </Grid>
                    <Grid item xs={12}>
                        <h2>Dataset Index</h2>
                    </Grid>
                    <TableDatasets />
                </Grid>
            }
        />
    )
}

export default Homepage