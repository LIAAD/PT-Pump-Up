import React, { useState } from 'react'
import Table from '@mui/material/Table'
import TableHead from '@mui/material/TableHead'
import TableBody from '@mui/material/TableBody'
import TableRow from '@mui/material/TableRow'
import TableCell from '@mui/material/TableCell'
import { ToProperCase } from '@/utils'
import ClearIcon from '@mui/icons-material/Clear';
import Button from '@mui/material/Button';
import LinkIcon from '@mui/icons-material/Link';
import ModalLoad from '../modal/ModalLoad'
import CloudDownloadIcon from '@mui/icons-material/CloudDownload';



const TableModel = (props) => {
    //TODO: I hate this duplication with TableDataset
    const [state, setState] = useState({
        open: false,
        elem: null
    })

    const handleClose = () => {
        setState({ ...state, 'open': false })
    }

    props.models.sort((a, b) => (a.year > b.year) ? -1 : 1)

    return (
        <>
            {state.elem && <ModalLoad open={state.open} handleClose={handleClose} model={state.elem} />}
            <Table stickyHeader className="table-resource">
                <TableHead>
                    <TableRow>
                        <TableCell>Name</TableCell>
                        <TableCell align="center">Year</TableCell>
                        <TableCell align="center">Website</TableCell>
                        <TableCell align="center">Paper URL</TableCell>
                        <TableCell align="center">Off the Shelf</TableCell>
                        <TableCell align="center">Preservation Rating</TableCell>
                    </TableRow>
                </TableHead>
                {props.expanded &&
                    <TableBody>
                        {props.models.map((model, key) =>
                            <TableRow key={key} hover={true}>
                                <TableCell>
                                    {model.short_name}
                                </TableCell>
                                <TableCell align="center">
                                    {model.year}
                                </TableCell>
                                <TableCell align="center">
                                    {model.link.website ? <Button href={model.link.website} target="_blank" rel="noopener noreferrer"><LinkIcon /></Button> : "?"}
                                </TableCell>
                                <TableCell align="center">
                                    {model.link.paper_url ? <Button href={model.link.paper_url} target="_blank" rel="noopener noreferrer"><LinkIcon /></Button> : "?"}
                                </TableCell>
                                <TableCell align="center">
                                    {model.link.hugging_face_url ?
                                        <Button onClick={(e) => setState({ ...state, 'open': true, 'elem': model })}>
                                            <CloudDownloadIcon />
                                        </Button> : <ClearIcon />
                                    }
                                </TableCell>
                                <TableCell align="center">
                                    {ToProperCase(model.resource_stats.preservation_rating) ?? '?'}
                                </TableCell>
                            </TableRow>
                        )}
                    </TableBody>
                }
            </Table>
        </>
    )
}

export default TableModel