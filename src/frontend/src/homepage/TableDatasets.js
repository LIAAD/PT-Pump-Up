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
import CheckIcon from '@mui/icons-material/Check';
import ClearIcon from '@mui/icons-material/Clear';

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

    // TODO: Add search bar

    // TODO: Add Capabilities of Automatic Testing Link Availability using Cron Jobs

    // TODO: Define Formula for Preservation Rating

    return Object.keys(state.datasets).map((key) => (

        <Grid container>
            <Grid item xs={12}><h2>{key}</h2></Grid>
            <Grid item xs={10} lg={10} sx={{ m: "auto", mb: 5 }}>
                <Table stickyHeader className="table-datasets">
                    <TableHead>
                        <TableRow>
                            <TableCell>Name</TableCell>
                            <TableCell align="center">Year</TableCell>
                            <TableCell align="center">Source URL</TableCell>
                            <TableCell align="center">Standardized</TableCell>
                            {/*<TableCell align="center">Link Avaiability</TableCell>
                            <TableCell align="center">Backup Done</TableCell>*/}
                            <TableCell align="center">Off the Shelf</TableCell>
                            <TableCell align="center">Preservation Rating</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {state.datasets[key].map((dataset, index) =>
                            <TableRow key={index}>
                                <TableCell scope="row" className="dataset-name">
                                    {dataset.name}
                                </TableCell>
                                <TableCell scope="row" align="center">{dataset.year}</TableCell>
                                <TableCell scope="row" align="center">
                                    <Button href={dataset.hrefs.link_source} target="_blank" rel="noopener noreferrer"><MonitorIcon /></Button>
                                </TableCell>
                                <TableCell scope="row" align="center">
                                    {dataset.status.standardized ? <ClearIcon /> : <CheckIcon />}
                                </TableCell>
                                <TableCell scope="row" align="center">
                                    {dataset.status.off_the_shelf ? <ClearIcon /> : <CheckIcon />}
                                </TableCell>
                                {/*<TableCell scope="row" align="center">
                                    {dataset.status.broken_link ? <ClearIcon /> : <CheckIcon />}
                                </TableCell>
                                <TableCell scope="row" align="center">
                                    {dataset.status.backup ? <ClearIcon /> : <CheckIcon />}
                        </TableCell>*/}
                                <TableCell scope="row" align="center">
                                    {dataset.status.preservation_rating}%
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