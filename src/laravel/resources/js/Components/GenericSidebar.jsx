import React from 'react'
import SwipeableDrawer from '@mui/material/SwipeableDrawer'
import ListItemButton from '@mui/material/ListItemButton';
import List from '@mui/material/List';
import { usePage } from '@inertiajs/react'
import { router } from '@inertiajs/react'

const GenericSidebar = (props) => {

    const { auth } = usePage().props

    const menus = [
        ['Home', route('home')],
        ['Datasets', route('datasets.index_web')],
        ['Models', route('models.index_web')],
        ['Login', route('login')],
        ['Profile', route('dashboard')],
        ['Logout', route('logout')],
    ]
    const handleClick = (e, link) => {
        if (link === route('logout'))
            return router.post(link)

        router.get(link)
    }

    // Remove login from sidebar
    if (auth.user)
        menus.splice(3, 1)
    else
        menus.splice(4, 2)

    return (
        <SwipeableDrawer open={props.showDrawer} onOpen={props.toggleDrawer} onClose={props.toggleDrawer}>
            <List id="sidebar-list">
                {menus.map((menu, index) => (
                    <ListItemButton key={index} className="sidebar-button" onClick={(e) => handleClick(e, menu[1])} sx={{ my: 2 }}>
                        {menu[0]}
                    </ListItemButton>
                ))}
            </List>
        </SwipeableDrawer>
    )
}

export default GenericSidebar