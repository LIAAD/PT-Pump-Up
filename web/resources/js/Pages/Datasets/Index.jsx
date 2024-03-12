import React from 'react'
import ColapsibleTable from '@/Components/table/ColapsibleTableDataset'
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
                        const entries = props.datasets.filter(dataset => dataset.nlp_tasks.some(task => task.short_name === props.nlp_task))
                        return <ColapsibleTable key={key} order={key} nlp_task={elem} datasets={props.datasets} table={<TableDataset entries={entries} />} />
                    })}
                </Grid>
            }
        />
    )
}

export default Index