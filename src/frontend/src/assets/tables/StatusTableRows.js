import React from 'react'
import TableCell from '@mui/material/TableCell';
import CheckIcon from '@mui/icons-material/Check';
import ClearIcon from '@mui/icons-material/Clear';


const StatusTableRows = (props) => {
    return (
        <>
            <TableCell scope="row" align="center">
                {props.status.standard_format ? <ClearIcon /> : <CheckIcon />}
            </TableCell>
            <TableCell scope="row" align="center">
                {props.status.off_the_shelf ? <ClearIcon /> : <CheckIcon />}
            </TableCell>
            <TableCell scope="row" align="center" className={`label-${props.status.preservation_rating}`}>
                {props.status.preservation_rating.replace(props.status.preservation_rating[0], props.status.preservation_rating[0].toUpperCase())}
            </TableCell>
            {/*<TableCell scope="row" align="center">
                                    {dataset.status.broken_link ? <ClearIcon /> : <CheckIcon />}
                                </TableCell>
                                <TableCell scope="row" align="center">
                                    {dataset.status.backup ? <ClearIcon /> : <CheckIcon />}
            </TableCell>*/}
        </>
    )
}

export default StatusTableRows