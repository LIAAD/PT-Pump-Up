import PTPumpUpLayout from '@/Layouts/PTPumpUpLayout'
import { filterByNLPTask } from '@/Utils'
import React, { useState } from 'react'
import { useEffect } from 'react'
import Grid from '@mui/material/Grid'
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Button from '@mui/material/Button';
import LinkIcon from '@mui/icons-material/Link';
import CheckIcon from '@mui/icons-material/Check';
import ClearIcon from '@mui/icons-material/Clear';
import AddIcon from '@mui/icons-material/Add';



const TableDataset = (props) => {
    return (
        <Grid container>
            <Grid item xs={12}>
                <h2>{props.task}</h2>
            </Grid>
            <Grid item xs={12}>
                <Table stickyHeader className="table-resource">
                    <TableHead>
                        <TableRow>
                            <TableCell>Name</TableCell>
                            <TableCell align="center">Year</TableCell>
                            <TableCell align="center">Source URL</TableCell>
                            <TableCell align="center">Standardized</TableCell>
                            <TableCell align="center">Off the Shelf</TableCell>
                            <TableCell align="center">Preservation Rating</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {props.datasets.map((dataset, index) =>
                            <TableRow key={index}>
                                <TableCell scope="row" className="resource-name">
                                    {dataset.english_name}
                                </TableCell>
                                <TableCell scope="row" align="center">{dataset.year}</TableCell>
                                <TableCell scope="row" align="center">
                                    <Button href={dataset.hrefs.link_source} target="_blank" rel="noopener noreferrer"><LinkIcon /></Button>
                                </TableCell>
                                <TableCell scope="row" align="center">
                                    {dataset.dataset_stats.standard_format ? <ClearIcon /> : <CheckIcon />}
                                </TableCell>
                                <TableCell scope="row" align="center">
                                    {dataset.dataset_stats.off_the_shelf ? <ClearIcon /> : <CheckIcon />}
                                </TableCell>
                                <TableCell scope="row" align="center" className={`label-${dataset.dataset_stats.preservation_rating}`}>
                                    {dataset.dataset_stats.preservation_rating.replace(dataset.dataset_stats.preservation_rating[0], dataset.dataset_stats.preservation_rating[0].toUpperCase())}
                                </TableCell>
                            </TableRow>
                        )}
                    </TableBody>
                </Table>
            </Grid>
        </Grid>
    )
}

const Index = (props) => {
    const [state, setState] = useState({
        datasets: [],
    })

    useEffect(() => {
        setState({ ...state, datasets: filterByNLPTask(props.datasets) })
    }, [])

    return (
        <PTPumpUpLayout
            main={
                <Grid container>
                    <Grid container alignItems="center">
                        <Grid item>
                            <h2>Dataset Index</h2>
                        </Grid>
                        {props.auth.user &&
                            <Grid item sx={{ ml: "auto" }}>
                                <Button variant="contained" href={route("datasets.create")}>Add New Dataset<AddIcon /> </Button>
                            </Grid>
                        }
                    </Grid>
                    {Object.keys(state.datasets).map((key) =>
                        <TableDataset task={key} datasets={state.datasets[key]} />
                    )}
                </Grid>
            }
        />
    )
}

export default Index
