import React from 'react'
import Box from '@mui/material/Box';
import HeaderAdmin from './HeaderAdmin';
import { useState } from 'react'
import SwipeableDrawer from '@mui/material/SwipeableDrawer';
import List from '@mui/material/List';
import ListItemButton from '@mui/material/ListItemButton';
import ListItem from '@mui/material/ListItem';
import SidebarAdmin from './SidebarAdmin';

const LayoutAdmin = (props) => {

    const [state, setState] = useState({
        'showDrawer': false,
    })

    const toggleDrawer = () => {
        setState({
            ...state,
            'showDrawer': !state.showDrawer,
        })
    }

    return (
        <Box fullWidth sx={{ m: 5 }}>
            <header>
                {props.header ? props.header : <HeaderAdmin toggleDrawer={toggleDrawer} />}
            </header>
            <aside>
                <SidebarAdmin showDrawer={state.showDrawer} toggleDrawer={toggleDrawer} />
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

export default LayoutAdmin