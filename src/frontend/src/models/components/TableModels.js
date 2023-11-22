import React from 'react'
import Grid from '@mui/material/Grid';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import { useState, useEffect } from 'react';
import { sendGetRequest } from '../../utils/requests';
import { filterByNLPTask } from '../../utils/filterNLPTask';
import StatusTableRows from '../../assets/tables/StatusTableRows';


const TableModels = (props) => {

    const [state, setState] = useState({
        'models': [],
    })

    useEffect(() => {
        sendGetRequest('/api/models/').then((response) => {
            setState({
                ...state,
                'models': filterByNLPTask(response),
            })
        });
    }, [])

    return Object.keys(state.models).map((key) => (
        <Grid container>
            <Grid item xs={12}><h2>{key}</h2></Grid>
            <Grid item xs={10} lg={10} sx={{ m: "auto", mb: 5 }}>
                <Table stickyHeader className="table-resource">
                    <TableHead>
                        <TableRow>
                            <TableCell>Name</TableCell>
                            <TableCell align="center">Year</TableCell>
                            <TableCell align="center">Standardized</TableCell>
                            <TableCell align="center">Off the Shelf</TableCell>
                            <TableCell align="center">Preservation Rating</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {state.models[key].map((model, index) =>
                            <TableRow key={index}>
                                <TableCell scope="row" className="resource-name">
                                    {model.name}
                                </TableCell>
                                <TableCell scope="row" align="center">
                                    {model.year}
                                </TableCell>
                                <StatusTableRows status={model.status} />
                            </TableRow>
                        )}
                    </TableBody>
                </Table>
            </Grid>
        </Grid>
    ))
}

export default TableModels