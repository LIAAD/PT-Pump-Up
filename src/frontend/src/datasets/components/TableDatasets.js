import React from 'react'
import { useState } from 'react'
import Grid from '@mui/material/Grid';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import { sendGetRequest } from '../../utils/requests';
import { useEffect } from 'react';
import LinkIcon from '@mui/icons-material/Link';
import Button from '@mui/material/Button';
import CheckIcon from '@mui/icons-material/Check';
import ClearIcon from '@mui/icons-material/Clear';
import { filterByNLPTask } from '../../utils/filterNLPTask';
import StatusTableRows from '../../assets/tables/StatusTableRows';

const TableDatasets = (props) => {

    const [state, setState] = useState({
        'datasets': [],
        'searchTerm': '',
    })


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

    const obtainYearFromDate = (date) => {
        return date.split('/')[0]
    }

    // TODO: Add search bar

    // TODO: Add Capabilities of Automatic Testing Link Availability using Cron Jobs

    // TODO: Define Formula for Preservation Rating

    return Object.keys(state.datasets).map((key) => (

        <Grid container>
            <Grid item xs={12}><h2>{key}</h2></Grid>
            <Grid item xs={10} lg={10} sx={{ m: "auto", mb: 5 }}>
                <Table stickyHeader className="table-resource">
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
                                <TableCell scope="row" className="resource-name">
                                    {dataset.english_name}
                                </TableCell>
                                <TableCell scope="row" align="center">{obtainYearFromDate(dataset.introduction_date)}</TableCell>
                                <TableCell scope="row" align="center">
                                    <Button href={dataset.hrefs.link_source} target="_blank" rel="noopener noreferrer"><LinkIcon /></Button>
                                </TableCell>
                                <StatusTableRows status={dataset.status} />
                            </TableRow>
                        )}
                    </TableBody>
                </Table>
            </Grid>
        </Grid>
    ))
}

export default TableDatasets