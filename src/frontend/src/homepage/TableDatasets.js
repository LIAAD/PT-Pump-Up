import React from 'react'
import { useState } from 'react'
import Grid from '@mui/material/Grid';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import TableContainer from '@mui/material/TableContainer';
import { sendGetRequest } from '../utils/requests';
import { useEffect } from 'react';

const TableDatasets = (props) => {

    const [state, setState] = useState({
        'datasets': [],
        'searchTerm': '',
    })

    const filterByNLPTask = (response) => {
        const datasetsByTask = {}

        response.forEach(element => {
            element.nlp_task.forEach(task => {
                if (task.name in datasetsByTask) {
                    datasetsByTask[task.name].push(element)
                } else {
                    datasetsByTask[task.name] = [element]
                }
            })
        });

        console.log(datasetsByTask);

        return datasetsByTask
    }

    useEffect(() => {
        sendGetRequest('/api/datasets/').then((response) => {
            setState({
                ...state,
                'datasets': filterByNLPTask(response),
            })
        }).catch((error) => {
            console.log(error);
        })
    }, [])


    return (
        <Grid item xs={12} sx={{ mx: "auto" }}>
            <TableContainer >
                <Table stickyHeader>
                    <TableHead>
                        <TableRow>
                            <TableCell>
                                Name
                            </TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {Object.keys(state.datasets).map((key) => (
                            state.datasets[key].map((dataset, index) =>
                                <TableRow key={index}>
                                    <TableCell component="th" scope="row">
                                        {dataset.name}
                                    </TableCell>
                                </TableRow>
                            )))}
                    </TableBody>
                </Table>
            </TableContainer>
        </Grid>
    )
}

export default TableDatasets