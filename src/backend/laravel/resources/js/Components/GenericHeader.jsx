import React from 'react'
import Grid from '@mui/material/Grid'
import Button from '@mui/material/Button'
import IconButton from '@mui/material/IconButton'
import MenuIcon from '@mui/icons-material/Menu'
import Box from '@mui/material/Box'
import inescLogo from '@/images/inesc-logo.png'


const GenericHeader = (props) => {
    return (
        <Grid container alignItems="center">
            <Grid item xs={"auto"}>
                <Button>
                    <img src={inescLogo} />
                </Button>
            </Grid>
            <Grid item xs={"auto"} lg={6}>
                <h1>PT-Pump-Up
                    <Box>Hub for Portuguese NLP Resources</Box>
                </h1>
            </Grid>
            <Grid item xs={1}>
                <IconButton onClick={props.toggleDrawer}><MenuIcon /></IconButton>
            </Grid>
        </Grid>
    )
}

export default GenericHeader