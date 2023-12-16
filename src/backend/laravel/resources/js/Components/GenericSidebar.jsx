import React from 'react'
import SwipeableDrawer from '@mui/material/SwipeableDrawer'
import ListItemButton from '@mui/material/ListItemButton';
import List from '@mui/material/List';

const GenericSidebar = (props) => {
    const menus = [
        ['Home', '/'],
        ['Datasets', '/datasets'],
        ['Models', '/models'],
    ]

    return (
        <SwipeableDrawer open={props.showDrawer} onOpen={props.toggleDrawer} onClose={props.toggleDrawer}>
            <List>
                {menus.map((menu, index) => (
                    <ListItemButton key={index}>
                        {menu[0]}
                    </ListItemButton>
                ))}
            </List>
        </SwipeableDrawer>
    )
}

export default GenericSidebar