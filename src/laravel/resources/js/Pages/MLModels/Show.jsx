import React from 'react'

import PTPumpUpLayout from '@/Layouts/PTPumpUpLayout'
import ShowResource from '@/Components/ShowResource'
import Grid from '@mui/material/Grid'
import { FormControl } from '@mui/material'
import TextField from '@mui/material/TextField'
import GenericDivider from '@/Components/GenericDivider'


const Show = (props) => {
    return (
        <PTPumpUpLayout
            main={
                <ShowResource elem={props.ml_model} delete_route="models.destroy" auth={props.auth}>
                    <GenericDivider label="Architecture" />
                    <Grid item xs={8}>
                        <FormControl fullWidth sx={{ mb: 3 }}>
                            <h3>Architecture</h3>
                            <TextField disabled value={props.ml_model.architecture} variant="outlined" />
                        </FormControl>
                    </Grid>
                </ShowResource>
            } />
    )
}

export default Show