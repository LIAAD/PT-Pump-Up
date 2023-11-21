import React from 'react'
import Grid from '@mui/material/Grid';
import TableDatasets from './components/TableDatasets';

const Index = () => {
    return (
        <Grid container justifyContent="flex-start" alignItems="flex-start" className="container-content" sx={{ pl: 3 }}>
            <Grid item xs={12}>
                <h1>PT-Pump-Up</h1>
            </Grid>
            <Grid item xs={12}>
                <h2>Dataset Index</h2>
            </Grid>
            <TableDatasets />
        </Grid>
    )
}

export default Index