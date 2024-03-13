import React, { useState } from 'react'
import Table from '@mui/material/Table'
import TableHead from '@mui/material/TableHead'
import TableBody from '@mui/material/TableBody'
import TableRow from '@mui/material/TableRow'
import TableCell from '@mui/material/TableCell'
import { ToProperCase } from '@/utils'
import ClearIcon from '@mui/icons-material/Clear';
import CheckIcon from '@mui/icons-material/Check';
import Button from '@mui/material/Button';
import LinkIcon from '@mui/icons-material/Link';
import CloudDownloadIcon from '@mui/icons-material/CloudDownload';
import ModalLoad from '../modal/ModalLoad'
import Tooltip from '@mui/material/Tooltip';

const TableDataset = (props) => {

    const [state, setState] = useState({
        open: false,
        elem: null
    })

    const handleClose = () => {
        setState({ ...state, 'open': false })
    }

    props.datasets.sort((a, b) => (a.year > b.year) ? -1 : 1)

    return (
        <>
            {state.elem && <ModalLoad open={state.open} handleClose={handleClose} dataset={state.elem} />}
            <Table stickyHeader className="table-resource">
                <TableHead>
                    <TableRow>
                        <TableCell>Name</TableCell>
                        <TableCell align="center">Year</TableCell>
                        <TableCell align="center">Website</TableCell>
                        <TableCell align="center">Paper URL</TableCell>
                        <TableCell align="center">Standardized <Tooltip></Tooltip></TableCell>
                        <TableCell align="center">Off the Shelf</TableCell>
                        <TableCell align="center">Preservation Rating</TableCell>
                    </TableRow>
                </TableHead>
                {props.expanded &&
                    <TableBody>
                        {props.datasets.map((dataset, key) =>
                            <TableRow key={key} hover={true}>
                                <TableCell>
                                    {dataset.short_name}
                                </TableCell>
                                <TableCell align="center">
                                    {dataset.year}
                                </TableCell>
                                <TableCell align="center">
                                    {dataset.link.website ? <Button href={dataset.link.website} target="_blank" rel="noopener noreferrer"><LinkIcon /></Button> : "?"}
                                </TableCell>
                                <TableCell align="center">
                                    {dataset.link.paper_url ? <Button href={dataset.link.paper_url} target="_blank" rel="noopener noreferrer"><LinkIcon /></Button> : "?"}
                                </TableCell>
                                <TableCell align="center">
                                    {dataset.resource_stats.standardized ? <ClearIcon /> : <CheckIcon />}
                                </TableCell>
                                <TableCell align="center">
                                    {dataset.link.hugging_face_url ?
                                        <Button onClick={(e) => setState({ ...state, 'open': true, 'elem': dataset })}>
                                            <CloudDownloadIcon />
                                        </Button> : <ClearIcon />
                                    }
                                </TableCell>
                                <TableCell align="center">
                                    {ToProperCase(dataset.resource_stats.preservation_rating) ?? '?'}
                                </TableCell>
                            </TableRow>
                        )}
                    </TableBody>
                }
            </Table>
        </>
    )
}
export default TableDataset