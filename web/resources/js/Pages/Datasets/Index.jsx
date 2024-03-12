import React from 'react'
import ColapsibleTable from '@/Components/table/ColapsibleTable'
import PTPumpUpLayout from '@/Layouts/PTPumpUpLayout'
import Grid from '@mui/material/Grid'
import TableDataset from '@/Components/table/TableDataset'

const Index = (props) => {

    return (
        <PTPumpUpLayout
            main={
                <Grid container>
                    <Grid container alignItems="center">
                        <Grid item><h2>Dataset Index</h2></Grid>
                    </Grid>
                    {props.nlp_tasks.map((elem, key) => {
                        return <ColapsibleTable key={key} order={key} type={"dataset"} nlp_task={elem} entries={props.datasets} />
                    })}
                </Grid>
            }
        />
    )
}

export default Index