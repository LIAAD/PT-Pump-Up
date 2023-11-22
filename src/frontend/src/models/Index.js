import React from 'react'
import LayoutAdmin from '../assets/admin/LayoutAdmin'
import Grid from '@mui/material/Grid';
import TableModels from './components/TableModels';

const Index = (props) => {
    return (
        <LayoutAdmin
            main={
                <Grid container justifyContent="flex-start" alignItems="flex-start" className="container-content" sx={{ pl: 3 }}>
                    <Grid item xs={12}>
                        <h2>Models Index</h2>
                    </Grid>
                    <Grid item xs={12}>
                        <TableModels />
                    </Grid>
                </Grid>
            }
        />
    )
}

export default Index