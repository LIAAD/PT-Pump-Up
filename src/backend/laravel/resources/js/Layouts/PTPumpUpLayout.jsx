import React from 'react'
import GenericHeader from '@/Components/GenericHeader'
import GenericSidebar from '@/Components/GenericSidebar'
import GenericFooter from '@/Components/GenericFooter'
import Box from '@mui/material/Box'

const PTPumpUpLayout = (props) => {
    return (
        <Box fullWidth sx={{ m: 5 }}>
            <header>
                {props.header ? props.header : <GenericHeader />}
            </header>
            <aside>
                {props.aside ? props.aside : <GenericSidebar />}
            </aside>
            <main>
                {props.main}
            </main>
            <footer>
                {props.footer ? props.footer : <GenericFooter />}
            </footer>
        </Box>
    )
}

export default PTPumpUpLayout