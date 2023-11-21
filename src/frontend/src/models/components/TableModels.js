import React from 'react'
import Grid from '@mui/material/Grid';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import { useState } from 'react';


const TableModels = (props) => {

    const state = useState({
        'models': [],
    })

    return (
        <Grid container>
            <Grid item xs={12}>
                <h2>Models</h2>
            </Grid>
            <Grid item xs={10} lg={10} sx={{ m: "auto", mb: 5 }}>
                <Table stickyHeader className="table-resource">
                    <TableHead>
                        <TableRow>
                            <TableCell>Name</TableCell>
                            <TableCell align="center">Year</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        <TableRow>
                            <TableCell scope="row" className="resource-name">
                                BERT-CRF
                            </TableCell>
                            <TableCell scope="row" align="center">
                                2017
                            </TableCell>
                        </TableRow>
                    </TableBody>
                </Table>
            </Grid>
        </Grid>
    )
}

export default TableModels