import React, { useState } from 'react'
import GenericHeader from '@/Components/GenericHeader'
import GenericSidebar from '@/Components/GenericSidebar'
import Box from '@mui/material/Box'

const PTPumpUpLayout = (props) => {

    const [state, setState] = useState({
        showDrawer: false,
    })

    const toggleDrawer = () => {
        setState({ ...state, showDrawer: !state.showDrawer })
    }

    return (
        <Box fullWidth sx={{ m: 5 }}>
            <header>
                {props.header ? props.header : <GenericHeader toggleDrawer={toggleDrawer} />}
            </header>
            <aside>
                {props.aside ? props.aside : <GenericSidebar showDrawer={state.showDrawer} toggleDrawer={toggleDrawer} {...props} />}
            </aside>
            <main>
                {props.main}
            </main>
            <footer>
                {props.footer}
            </footer>
        </Box>
    )
}

export default PTPumpUpLayout