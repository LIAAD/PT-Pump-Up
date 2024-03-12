import React, { useState } from 'react'
import Grid from '@mui/material/Grid'
import IconButton from '@mui/material/IconButton'
import ExpandMoreIcon from '@mui/icons-material/ExpandMore'
import ExpandLessIcon from '@mui/icons-material/ExpandLess'
import Table from '@mui/material/Table'
import TableRow from '@mui/material/TableRow'
import TableDataset from './TableDataset'

const ButtonExpand = (props) => {
    return (
        <>
            {!props.state.expanded &&
                <IconButton size="large" onClick={() => props.setState({ ...props.state, expanded: !props.state.expanded })}>
                    <ExpandMoreIcon fontSize="large" />
                </IconButton>
            }
            {props.state.expanded &&
                <IconButton size="large" onClick={() => props.setState({ ...props.state, expanded: !props.state.expanded })}>
                    <ExpandLessIcon fontSize="large" />
                </IconButton>
            }
        </>
    )
}

const ColapsibleTable = (props) => {

    const [state, setState] = useState({
        expanded: props.order === 0 ? true : false
    })

    return (
        <Grid container>
            <Grid container>
                <Grid item xs={11}><h2>{props.nlp_task}</h2></Grid>
                <Grid item><ButtonExpand state={state} setState={setState} /></Grid>
            </Grid>
            <Grid item xs={12} lg={11} alignItem="center" sx={{ mb: 5 }}>
                <TableDataset expanded={state.expanded} datasets={props.datasets} />
            </Grid>
        </Grid>
    )
}

export default ColapsibleTable