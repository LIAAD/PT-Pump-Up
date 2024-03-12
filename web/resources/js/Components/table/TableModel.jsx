import React from 'react'
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


const TableModel = (props) => {
    props.models.sort((a, b) => (a.year > b.year) ? -1 : 1)

    return (
        <Table stickyHeader className="table-resource">
            <TableHead>
                <TableRow>
                    <TableCell>Name</TableCell>
                    <TableCell align="center">Year</TableCell>
                    <TableCell align="center">Source URL</TableCell>
                    <TableCell align="center">Hugging Face URL</TableCell>
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
                                {model.link.hugging_face_url ? <Button href={model.link.hugging_face_url} target="_blank" rel="noopener noreferrer"><LinkIcon /></Button> : "?"}
                            </TableCell>
                            <TableCell align="center">
                                {model.link.paper_url ? <Button href={model.link.paper_url} target="_blank" rel="noopener noreferrer"><LinkIcon /></Button> : "?"}
                            </TableCell>
                            <TableCell align="center">
                                {model.resource_stats.off_the_shelf ? <ClearIcon /> : <CheckIcon />}
                            </TableCell>
                            <TableCell align="center">
                                {ToProperCase(model.resource_stats.preservation_rating) ?? '?'}
                            </TableCell>
                        </TableRow>
                    )}
                </TableBody>
            }
        </Table>
    )
}

export default TableModel