import React, { useState } from 'react'
import Grid from '@mui/material/Grid'
import ButtonExpand from '../button/ButtonExpand'
import TableDataset from './TableDataset'
import TableModel from './TableModel'


const ColapsibleTable = (props) => {
    const [state, setState] = useState({
        expanded: props.order === 0 ? true : false
    })

    // If any of the nlp_tasks.short_name is equal to the nlp_task, then return the element
    const elems = props.entries.filter(elem => elem.nlp_tasks.some(task => task.full_name === props.nlp_task || task.short_name === props.nlp_task))

    return (
        <Grid container alignItem="center" justifyContent="center">
            <Grid container>
                <Grid item xs={11}><h2>{props.nlp_task}</h2></Grid>
                <Grid item><ButtonExpand state={state} setState={setState} /></Grid>
            </Grid>
            <Grid item xs={12} lg={11} alignItem="center" sx={{ mb: 5 }}>
                {props.type === "dataset" && <TableDataset expanded={state.expanded} nlp_task={props.nlp_task} datasets={elems} />}
                {props.type === "model" && <TableModel expanded={state.expanded} nlp_task={props.nlp_task} models={elems} />}
            </Grid>
        </Grid>
    )
}

export default ColapsibleTable