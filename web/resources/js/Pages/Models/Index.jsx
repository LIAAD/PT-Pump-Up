import React from 'react'
import PTPumpUpLayout from '@/Layouts/PTPumpUpLayout'
import Grid from '@mui/material/Grid'
import ColapsibleTable from '@/Components/table/ColapsibleTable'

const Index = (props) => {
    return (
        <PTPumpUpLayout
            main={
                <Grid container>
                    <Grid container alignItems="center">
                        <Grid item><h2>Model Index</h2></Grid>
                    </Grid>
                    {props.nlp_tasks.map((elem, key) => {
                        return <ColapsibleTable key={key} order={key} type={"model"} nlp_task={elem} entries={props.models} />
                    })}
                </Grid>
            }
        />
    )
}

export default Index