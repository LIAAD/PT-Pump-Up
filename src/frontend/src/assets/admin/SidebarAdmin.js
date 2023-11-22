import React from 'react'
import SwipeableDrawer from '@mui/material/SwipeableDrawer';
import List from '@mui/material/List';
import ListItemButton from '@mui/material/ListItemButton';
import ListItem from '@mui/material/ListItem';

const SidebarAdmin = (props) => {

    const menus = [
        ['Home', '/'],
        ['Datasets', '/datasets'],
        ['Models', '/models'],
        //['Team', '/team'],
        //['About Us', '/about-us']
    ]

    return (
        <SwipeableDrawer open={props.showDrawer} onOpen={props.toggleDrawer} onClose={props.toggleDrawer}>
            <List id="sidebar" >
                {menus.map((menu, index) => (
                    <ListItemButton className="sidebar-button" href={`${menu[1]}`} sx={{ my: 2 }}>
                        {menu[0]}
                    </ListItemButton>
                ))}
            </List>
        </SwipeableDrawer>
    )
}

export default SidebarAdmin