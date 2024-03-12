import React, { useState } from 'react';
import Box from '@mui/material/Box'
import GenericHeader from '@/Components/header/GenericHeader';
import GenericAside from '@/Components/aside/GenericAside';

const PTPumpUpLayout = (props) => {

    const [state, setState] = useState({
        showDrawer: false,
    })

    const toggleDrawer = () => {
        setState({ ...state, showDrawer: !state.showDrawer })
    }

    return (
        <Box fullwidth sx={{ m: 5 }}>
            <header>
                {props.header ? props.header : <GenericHeader toggleDrawer={toggleDrawer} />}
            </header>
            <aside>
                {props.aside ? props.aside : <GenericAside showDrawer={state.showDrawer} toggleDrawer={toggleDrawer} {...props} />}
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