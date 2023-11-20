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
import MonitorIcon from '@mui/icons-material/Monitor';
import Button from '@mui/material/Button';


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

    /*
    */


    return Object.keys(state.datasets).map((key) => (

        <Grid container>
            <Grid item xs={12}><h2>{key}</h2></Grid>
            <Grid item xs={10} lg={8} sx={{m:"auto", mb:5}}>
                <Table stickyHeader className="table-datasets">
                    <TableHead>
                        <TableRow>
                            <TableCell>Name</TableCell>
                            <TableCell align="center">Year</TableCell>
                            <TableCell align="center">Source URL</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {state.datasets[key].map((dataset, index) =>
                            <TableRow key={index}>
                                <TableCell scope="row">
                                    {dataset.name}
                                </TableCell>
                                <TableCell scope="row" align="center">{dataset.year}</TableCell>
                                <TableCell scope="row" align="center">
                                    <Button href={dataset.hrefs.link_source}><MonitorIcon /></Button>
                                </TableCell>
                            </TableRow>
                        )}
                    </TableBody>
                </Table>
            </Grid>
        </Grid>
    ))
}

export default TableDatasets