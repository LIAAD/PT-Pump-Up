import React from 'react'
import Box from '@mui/material/Box';


const LayoutAdmin = (props) => {
    return (
        <Box fullWidth sx={{ m: 5 }}>
            {props.header}
            {props.main}
            {props.footer}
        </Box>
    )
}

export default LayoutAdmin