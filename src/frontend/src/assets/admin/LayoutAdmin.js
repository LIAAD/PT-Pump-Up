import React from 'react'
import Box from '@mui/material/Box';


const LayoutAdmin = (props) => {
    return (
        <Box fullWidth sx={{ m: 5 }}>
            <header>
                {props.header}
            </header>
            <main>
                {props.main}
            </main>
            <footer>
                {props.footer}
            </footer>
        </Box>
    )
}

export default LayoutAdmin